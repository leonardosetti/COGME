"""Geração do PDF da invoice (spec backend-mvp-v1, §6; REQ-04).

A simulação é sempre recalculada no servidor. Nomes, documentos e endereços só existem durante
a chamada: não são gravados nem registrados em log. Os logs trazem apenas o tipo da falha.

O WeasyPrint é importado sob demanda, para a API subir mesmo sem Pango, e roda em thread, pois
a renderização é pesada e bloquearia o laço de eventos.
"""

from __future__ import annotations

import asyncio
import logging
from datetime import date, datetime
from decimal import ROUND_HALF_EVEN, Decimal
from functools import lru_cache
from pathlib import Path
from typing import Any, Final

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from src.backend.errors import PdfUnavailableError
from src.backend.services.rate_service import RateService
from src.backend.services.simulation_service import simulate
from src.shared.schemas import InvoiceRequest, RateSource, Regime

logger = logging.getLogger(__name__)

# Resolvido a partir deste arquivo (src/backend/services), nunca do diretório de trabalho.
TEMPLATES_DIR: Final[Path] = Path(__file__).resolve().parents[2] / "frontend" / "templates"
_TEMPLATE_NAME: Final[str] = "invoice.html"

_REGIME_LABELS: Final[dict[Regime, str]] = {
    Regime.HOURLY: "Por hora",
    Regime.DAILY: "Por dia",
    Regime.WEEKLY: "Por semana",
    Regime.MONTHLY: "Por mês",
    Regime.FIXED: "Valor fixo",
}
_QUANTITY_LABELS: Final[dict[Regime, str]] = {
    Regime.HOURLY: "Horas",
    Regime.DAILY: "Dias",
    Regime.WEEKLY: "Semanas",
    Regime.MONTHLY: "Meses",
    Regime.FIXED: "",
}
_SOURCE_LABELS: Final[dict[RateSource, str]] = {
    RateSource.FRANKFURTER: "Frankfurter",
    RateSource.PTAX: "PTAX (Banco Central do Brasil)",
}

_CENTS: Final[Decimal] = Decimal("0.01")
# Troca os separadores do padrão en-US pelos do pt-BR, sem depender de locale do sistema.
_BR_SEPARATORS: Final[dict[int, str]] = str.maketrans({",": ".", ".": ","})


class _RefusingUrlFetcher:
    """Recusa toda URL: a invoice não pode buscar recurso algum, remoto ou local.

    O WeasyPrint 70 lê ``_fail_on_errors`` do fetcher ao tratar uma falha; ``False`` faz a
    recusa virar apenas um aviso, sem interromper a renderização.
    """

    _fail_on_errors = False

    def __call__(self, url: str) -> Any:
        """Recusa a busca.

        Args:
            url: URL pedida pelo documento; não é usada nem registrada.

        Raises:
            ValueError: Sempre.
        """
        raise ValueError("Busca de recurso externo recusada.")


def _number_br(value: Decimal | int | str, places: int) -> str:
    """Formata um número no padrão brasileiro, com milhar em ponto e decimal em vírgula.

    Args:
        value: Valor numérico.
        places: Casas decimais (arredonda com ``ROUND_HALF_EVEN``).

    Returns:
        O texto, por exemplo ``23.430,62``.
    """
    step = Decimal(1).scaleb(-places)
    rounded = Decimal(value).quantize(step, rounding=ROUND_HALF_EVEN)
    return format(rounded, ",f").translate(_BR_SEPARATORS)


def brl(value: Decimal | int | str) -> str:
    """Formata um valor em reais, por exemplo ``R$ 23.430,62``.

    Args:
        value: Valor em BRL.

    Returns:
        O texto formatado.
    """
    return f"R$ {_number_br(value, 2)}"


def money_br(value: Decimal | int | str) -> str:
    """Formata um valor monetário com 2 casas, sem símbolo, por exemplo ``4.800,00``.

    Args:
        value: Valor monetário.

    Returns:
        O texto formatado.
    """
    return _number_br(value, 2)


def rate_br(value: Decimal | int | str) -> str:
    """Formata uma cotação com 6 casas, por exemplo ``5,432500``.

    Args:
        value: Cotação em BRL.

    Returns:
        O texto formatado.
    """
    return _number_br(value, 6)


def percent_br(value: Decimal | int | str) -> str:
    """Formata um percentual com 2 a 4 casas, por exemplo ``2,00 %`` ou ``0,0125 %``.

    Args:
        value: Percentual de 0 a 100.

    Returns:
        O texto formatado, sem zeros finais além das 2 casas mínimas.
    """
    text = _number_br(value, 4)
    minimum = text.index(",") + 3
    return f"{text[:minimum]}{text[minimum:].rstrip('0')} %"


def date_br(value: date) -> str:
    """Formata uma data como ``dd/mm/aaaa``.

    Args:
        value: Data a formatar.

    Returns:
        O texto formatado.
    """
    return value.strftime("%d/%m/%Y")


def datetime_br(value: datetime) -> str:
    """Formata um instante como ``dd/mm/aaaa hh:mm UTC``.

    Args:
        value: Instante com fuso (já em UTC pelo contrato).

    Returns:
        O texto formatado.
    """
    return f"{value:%d/%m/%Y %H:%M} UTC"


@lru_cache(maxsize=1)
def _get_environment() -> Environment:
    """Monta o ambiente Jinja2 da invoice, uma única vez por processo.

    Returns:
        O ambiente, com autoescape ativo e carregador restrito a ``TEMPLATES_DIR``.
    """
    environment = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=True,
        undefined=StrictUndefined,
    )
    environment.filters.update(
        brl=brl,
        money_br=money_br,
        rate_br=rate_br,
        percent_br=percent_br,
        date_br=date_br,
        datetime_br=datetime_br,
    )
    return environment


def _render_pdf(context: dict[str, Any]) -> bytes:
    """Renderiza o HTML e converte para PDF; roda em thread.

    Args:
        context: Variáveis do template.

    Returns:
        Os bytes do PDF.

    Raises:
        PdfUnavailableError: Se o WeasyPrint ou o Pango faltarem, ou se a renderização falhar.
    """
    try:
        import weasyprint  # tardio: a API sobe mesmo sem Pango

        html = _get_environment().get_template(_TEMPLATE_NAME).render(context)
        pdf: bytes = weasyprint.HTML(string=html, url_fetcher=_RefusingUrlFetcher()).write_pdf()
    except Exception as error:  # OSError/ImportError (sem Pango) ou qualquer falha de render
        # Só o tipo: a mensagem pode trazer trechos do documento, ou seja, dados pessoais.
        logger.error("invoice_render_failed cause=%s", type(error).__name__)
        raise PdfUnavailableError from None
    return pdf


async def render_invoice(request: InvoiceRequest, rate_service: RateService) -> bytes:
    """Recalcula a simulação e gera o PDF da invoice.

    Args:
        request: Entrada validada pelo contrato; os valores calculados nunca vêm do cliente.
        rate_service: Fonte da cotação.

    Returns:
        Os bytes do PDF.

    Raises:
        RatesUnavailableError: Sem fonte de cotação disponível e sem cache.
        PdfUnavailableError: WeasyPrint/Pango ausente ou falha de renderização.
    """
    simulation = await simulate(request.simulation, rate_service)
    regime = request.simulation.regime
    context: dict[str, Any] = {
        "issuer": request.issuer,
        "client": request.client,
        "invoice_number": request.invoice_number,
        "issue_date": request.issue_date,
        "description": request.description,
        "regime_label": _REGIME_LABELS[regime],
        "quantity_label": _QUANTITY_LABELS[regime],
        "unit_amount": request.simulation.amount,
        "quantity": request.simulation.quantity,
        "source_label": _SOURCE_LABELS[simulation.quote.source],
        "sim": simulation,
        "quote": simulation.quote,
        "stale": simulation.quote.stale,
        "notice": simulation.notice,
    }
    return await asyncio.to_thread(_render_pdf, context)
