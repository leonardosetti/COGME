"""Circuit breaker em memória, um por provedor de cotação (spec backend-mvp-v1, §4; REQ-01).

Fechado, admite tudo. Abre após ``failure_threshold`` falhas consecutivas e bloqueia por
``reset_seconds``. Vencido o prazo (inclusive), fica meio-aberto: admite uma tentativa por vez,
cujo resultado fecha ou reabre o circuito.

A classe não usa travas: foi feita para um único event loop, em que nenhum método cede o
controle. Quem recebe ``True`` de :meth:`CircuitBreaker.allow` deve registrar o desfecho, mesmo
em cancelamento, com :meth:`CircuitBreaker.record_release`; do contrário o estado meio-aberto
bloqueia o provedor para sempre.
"""

from __future__ import annotations

import time
from collections.abc import Callable


class CircuitBreaker:
    """Decide se um provedor pode ser chamado, conforme as falhas recentes."""

    def __init__(
        self,
        failure_threshold: int = 3,
        reset_seconds: float = 60.0,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        """Cria o circuito fechado.

        Args:
            failure_threshold: Falhas consecutivas que abrem o circuito.
            reset_seconds: Tempo aberto antes de admitir uma tentativa.
            clock: Relógio monotônico, em segundos.
        """
        self._failure_threshold = failure_threshold
        self._reset_seconds = reset_seconds
        self._clock = clock
        self._failures = 0
        self._opened_at: float | None = None
        self._probing = False

    def allow(self) -> bool:
        """Informa se uma chamada pode seguir.

        No estado meio-aberto, a chamada que recebe ``True`` reserva a única tentativa.

        Returns:
            ``True`` se a chamada foi admitida.
        """
        if self._opened_at is None:
            return True
        if self._probing or self._clock() - self._opened_at < self._reset_seconds:
            return False
        self._probing = True
        return True

    def record_success(self) -> None:
        """Registra um sucesso: fecha o circuito e zera a contagem.

        Com o circuito aberto e sem tentativa em curso, o resultado é de uma chamada admitida
        antes da abertura e é ignorado: só a tentativa pode fechar o circuito.
        """
        if self._opened_at is not None and not self._probing:
            return
        self._failures = 0
        self._opened_at = None
        self._probing = False

    def record_failure(self) -> None:
        """Registra uma falha: conta rumo à abertura ou reabre após a tentativa.

        Com o circuito aberto e sem tentativa em curso, o resultado é de uma chamada admitida
        antes da abertura e é ignorado, para não prolongar o bloqueio.
        """
        if self._probing:
            self._probing = False
            self._opened_at = self._clock()
        elif self._opened_at is None:
            self._failures += 1
            if self._failures >= self._failure_threshold:
                self._opened_at = self._clock()

    def record_release(self) -> None:
        """Encerra uma chamada que não teve veredito, como em cancelamento.

        Libera a tentativa meio-aberta, se houver, sem mudar contagem nem prazo: o provedor não
        falhou e também não provou que voltou, então a próxima chamada pode tentar de imediato.
        """
        self._probing = False
