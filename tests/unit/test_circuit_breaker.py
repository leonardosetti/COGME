"""Testes unitários de services/circuit_breaker.py (spec backend-mvp-v1, §4; REQ-01).

Regra: abre após 3 falhas consecutivas, fica aberto por 60 s e depois admite uma
tentativa; uma nova falha nessa tentativa reabre o circuito. O relógio é falso.
"""

from __future__ import annotations

import inspect
from typing import Any

import pytest

from src.backend.services.circuit_breaker import CircuitBreaker


@pytest.fixture
def breaker(mono_clock: Any) -> CircuitBreaker:
    """Circuito com os parâmetros da §8.1 e relógio falso.

    Args:
        mono_clock: Relógio monotônico falso da conftest.

    Returns:
        Um CircuitBreaker novo para o teste.
    """
    return CircuitBreaker(failure_threshold=3, reset_seconds=60.0, clock=mono_clock)


def _trip(breaker: CircuitBreaker) -> None:
    """Leva o circuito ao estado aberto com três falhas consecutivas.

    Args:
        breaker: Circuito a abrir.
    """
    for _ in range(3):
        breaker.record_failure()


def test_starts_closed(breaker: CircuitBreaker) -> None:
    """Circuito novo admite tentativas (fechado)."""
    assert breaker.allow() is True


def test_opens_on_third_consecutive_failure(breaker: CircuitBreaker) -> None:
    """Duas falhas ainda admitem; a terceira consecutiva abre o circuito."""
    breaker.record_failure()
    breaker.record_failure()
    assert breaker.allow() is True
    breaker.record_failure()
    assert breaker.allow() is False


def test_success_resets_failure_count(breaker: CircuitBreaker) -> None:
    """Sucesso zera a contagem: duas falhas, sucesso e duas falhas não abrem o circuito."""
    breaker.record_failure()
    breaker.record_failure()
    breaker.record_success()
    breaker.record_failure()
    breaker.record_failure()
    assert breaker.allow() is True
    breaker.record_failure()
    assert breaker.allow() is False


def test_blocks_for_sixty_seconds(breaker: CircuitBreaker, mono_clock: Any) -> None:
    """Aberto, bloqueia durante os 60 s de reset; aos 59 s ainda está bloqueado."""
    _trip(breaker)
    mono_clock.advance(59)
    assert breaker.allow() is False


def test_admits_attempt_after_reset_period(breaker: CircuitBreaker, mono_clock: Any) -> None:
    """Passados os 60 s, o circuito admite uma tentativa."""
    _trip(breaker)
    mono_clock.advance(60)
    assert breaker.allow() is True


def test_failure_on_probe_reopens_the_circuit(breaker: CircuitBreaker, mono_clock: Any) -> None:
    """Nova falha na tentativa reabre o circuito por mais 60 s."""
    _trip(breaker)
    mono_clock.advance(60)
    assert breaker.allow() is True
    breaker.record_failure()
    assert breaker.allow() is False
    mono_clock.advance(59)
    assert breaker.allow() is False
    mono_clock.advance(1)
    assert breaker.allow() is True


def test_success_on_probe_closes_the_circuit(breaker: CircuitBreaker, mono_clock: Any) -> None:
    """Sucesso na tentativa fecha o circuito; a contagem recomeça do zero."""
    _trip(breaker)
    mono_clock.advance(60)
    assert breaker.allow() is True
    breaker.record_success()
    breaker.record_failure()
    breaker.record_failure()
    assert breaker.allow() is True


def test_default_parameters_match_spec_section8_1() -> None:
    """Padrões da §8.1: 3 falhas e 60 s de reset."""
    params = inspect.signature(CircuitBreaker.__init__).parameters
    assert params["failure_threshold"].default == 3
    assert params["reset_seconds"].default == 60.0
