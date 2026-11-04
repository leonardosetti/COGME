"""Invoice em PDF: rota, recálculo no servidor e template (spec backend-mvp-v1, §6; REQ-04).

``_render_pdf`` é substituído por um dublê que captura o contexto do template, pois o WeasyPrint
não carrega sem Pango (Windows, por exemplo). O template é renderizado com o ambiente real do
projeto. Só o teste de PDF real depende do WeasyPrint, e é o único com skip.
"""

from __future__ import annotations

import logging
import sys
from datetime import timedelta
from decimal import Decimal
from typing import Any

import pytest
from fastapi.testclient import TestClient

from src.backend.main import app
from src.backend.services import invoice_service
from src.shared.schemas import NOTICE, RateSource

from .fakes import (
    SPEC_EXAMPLE_BODY,
    SYNTHETIC_NOW,
    FixedClock,
    MemoryRepository,
    ScriptedProvider,
    build_service,
    failing_provider,
    stored_quote,
)

INVOICE = "/v1/invoice"
FAKE_PDF = b"%PDF-1.7 documento sintetico"
UNAVAILABLE_PDF_MESSAGE = "Geração de PDF indisponível no momento. Tente novamente mais tarde."
ISSUER_NAME = "Pessoa Fictícia da Silva"


def _payload(**simulation_overrides: Any) -> dict[str, Any]:
    """Monta uma invoice sintética; a simulação padrão é o exemplo da §2.

    Args:
        **simulation_overrides: Campos da simulação a trocar.

    Returns:
        O corpo JSON da requisição.
    """
    return {
        "simulation": {**SPEC_EXAMPLE_BODY, **simulation_overrides},
        "issuer": {
            "name": ISSUER_NAME,
            "tax_id": "000.000.000-00",
            "address": "Rua Exemplo, 123, Cidade Fictícia",
        },
        "client": {
            "name": "Example Fictional LLC",
            "tax_id": None,
            "address": "1 Sample Street, Nowhere",
        },
        "invoice_number": "INV-0001",
        "issue_date": "2026-01-15",
        "description": "Serviços fictícios de desenvolvimento de software.",
    }


@pytest.fixture
def captured(monkeypatch: pytest.MonkeyPatch) -> dict[str, list[dict[str, Any]]]:
    """Troca ``_render_pdf`` por um dublê que guarda o contexto de cada renderização."""
    contexts: list[dict[str, Any]] = []

    def fake_render(context: dict[str, Any]) -> bytes:
        contexts.append(context)
        return FAKE_PDF

    monkeypatch.setattr(invoice_service, "_render_pdf", fake_render)
    return {"contexts": contexts}


def _html_of(context: dict[str, Any]) -> str:
    """Renderiza o template real da invoice com o contexto capturado.

    Args:
        context: Contexto que ``render_invoice`` enviaria ao WeasyPrint.

    Returns:
        O HTML gerado.
    """
    template = invoice_service._get_environment().get_template("invoice.html")
    return template.render(context)


def test_invoice_pdf_has_attachment_and_no_store_headers_req04(
    client: TestClient, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-04: 200 application/pdf, anexo invoice.pdf e Cache-Control no-store (§6)."""
    response = client.post(INVOICE, json=_payload())
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.headers["content-disposition"] == 'attachment; filename="invoice.pdf"'
    assert response.headers["cache-control"] == "no-store"
    assert response.content == FAKE_PDF


def test_server_recalculates_the_simulation_req04(
    client: TestClient, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-04: o servidor recalcula a simulação; o contexto traz os valores da §2 (§6)."""
    client.post(INVOICE, json=_payload())
    context = captured["contexts"][0]
    sim = context["sim"]
    assert sim.gross_brl == Decimal("24000.00")
    assert sim.spread_brl == Decimal("480.00")
    assert sim.iof_brl == Decimal("89.38")
    assert sim.net_brl == Decimal("23430.62")
    assert context["quote"].rate == Decimal("5.000000")
    assert context["regime_label"] == "Por hora"
    assert context["quantity_label"] == "Horas"
    assert context["source_label"] == "Frankfurter"
    assert context["notice"] == NOTICE


@pytest.mark.parametrize(
    "smuggled",
    [
        {"net_brl": "99999.00"},
        {"effective_rate": "9.999999"},
    ],
    ids=["net_brl_pronto", "taxa_efetiva_pronta"],
)
def test_client_cannot_send_precomputed_values_req04(
    client: TestClient, captured: dict[str, list[dict[str, Any]]], smuggled: dict[str, str],
) -> None:
    """REQ-04: valores calculados não são aceitos do cliente: campo extra vira 400 (§6, §8.1)."""
    body = _payload()
    body["simulation"].update(smuggled)
    response = client.post(INVOICE, json=body)
    assert response.status_code == 400
    error = response.json()["error"]
    assert error["key"] == "validation_error"
    assert error["details"] == [{"field": "body", "message": "Campo não permitido."}]
    assert captured["contexts"] == []


def test_rates_unavailable_blocks_invoice_req01(
    serve_rates: Any, clock: FixedClock,
) -> None:
    """REQ-01: sem cotação, a invoice responde 503 rates_unavailable e não renderiza (§3)."""
    serve_rates(
        build_service(
            providers=[failing_provider(RateSource.FRANKFURTER),
                       failing_provider(RateSource.PTAX)],
            clock=clock,
        ),
    )
    response = TestClient(app).post(INVOICE, json=_payload())
    assert response.status_code == 503
    assert response.json()["error"]["key"] == "rates_unavailable"


def test_missing_weasyprint_is_503_pdf_unavailable_req04(
    client: TestClient, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture,
) -> None:
    """REQ-04: WeasyPrint ausente vira 503 pdf_unavailable; o log traz só o tipo da falha (§6).

    ``sys.modules['weasyprint'] = None`` faz o ``import`` tardio falhar, em qualquer ambiente.
    """
    monkeypatch.setitem(sys.modules, "weasyprint", None)
    with caplog.at_level(logging.ERROR):
        response = client.post(INVOICE, json=_payload())

    assert response.status_code == 503
    assert response.json() == {
        "error": {"key": "pdf_unavailable", "message": UNAVAILABLE_PDF_MESSAGE, "details": []},
    }
    assert "invoice_render_failed cause=ModuleNotFoundError" in caplog.text
    # LGPD: nome da parte e documento nunca vão para o log (§5, §6).
    assert ISSUER_NAME not in caplog.text
    assert "000.000.000-00" not in caplog.text


def test_script_in_party_name_is_escaped_req04(
    client: TestClient, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-04: nome com <script> é escapado pelo autoescape; nenhuma tag ativa sai no HTML."""
    body = _payload()
    body["client"]["name"] = "Cliente <script>alert('x')</script> Fictício"
    client.post(INVOICE, json=body)
    html = _html_of(captured["contexts"][0])
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


def test_stale_quote_shows_warning_req01(
    serve_rates: Any, clock: FixedClock, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-01: cotação de cache vencido mostra o aviso de desatualização; a fresca não (§6)."""
    old_row = stored_quote(fetched_at=SYNTHETIC_NOW - timedelta(hours=5))
    stale_repository = MemoryRepository([old_row])
    serve_rates(
        build_service(
            repository=stale_repository,
            providers=[failing_provider(RateSource.FRANKFURTER),
                       failing_provider(RateSource.PTAX)],
            clock=clock,
        ),
    )
    response = TestClient(app).post(INVOICE, json=_payload())
    assert response.status_code == 200
    assert "Atenção: esta cotação está desatualizada" in _html_of(captured["contexts"][-1])


def test_fresh_quote_has_no_stale_warning_req01(
    client: TestClient, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-01: cotação obtida agora não mostra aviso de desatualização."""
    client.post(INVOICE, json=_payload())
    assert "desatualizada" not in _html_of(captured["contexts"][0])


def test_ptax_quote_shows_bulletin_and_source_req04(
    serve_rates: Any, clock: FixedClock, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-04: fonte PTAX aparece com o boletim; a Frankfurter não tem linha de boletim (§6)."""
    serve_rates(
        build_service(
            providers=[
                failing_provider(RateSource.FRANKFURTER),
                ScriptedProvider(RateSource.PTAX, rate="5.420600", bulletin="Fechamento"),
            ],
            clock=clock,
        ),
    )
    TestClient(app).post(INVOICE, json=_payload())
    html = _html_of(captured["contexts"][-1])
    assert "PTAX (Banco Central do Brasil)" in html
    assert "<th>Boletim</th><td>Fechamento</td>" in html


def test_frankfurter_quote_has_no_bulletin_row_req04(
    client: TestClient, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-04: sem boletim (Frankfurter), a linha de boletim não é impressa."""
    client.post(INVOICE, json=_payload())
    assert "Boletim" not in _html_of(captured["contexts"][0])


def test_money_is_formatted_pt_br_req04(
    client: TestClient, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-04: valores saem no padrão brasileiro: R$ 23.430,62, data dd/mm/aaaa (§6)."""
    client.post(INVOICE, json=_payload())
    html = _html_of(captured["contexts"][0])
    assert "R$ 23.430,62" in html
    assert "R$ 24.000,00" in html
    assert "- R$ 480,00" in html
    assert "Spread (2,00 %)" in html
    assert "IOF (0,38 %)" in html
    assert "R$ 5,000000" in html
    assert "15/01/2026" in html
    assert "30/10/2026 00:00 UTC" in html


def test_notice_text_is_rendered_req04(
    client: TestClient, captured: dict[str, list[dict[str, Any]]],
) -> None:
    """REQ-04: o aviso constante da §2 aparece no rodapé da invoice (§6)."""
    client.post(INVOICE, json=_payload())
    assert NOTICE in _html_of(captured["contexts"][0])


def test_real_pdf_is_generated_with_weasyprint_req04(client: TestClient) -> None:
    """REQ-04: PDF real com WeasyPrint; roda de verdade no CI, onde há Pango.

    Skip apenas quando ``import weasyprint`` levanta ``OSError`` (biblioteca nativa ausente,
    como o libgobject no Windows). Qualquer outra falha de importação derruba o teste.
    """
    try:
        import weasyprint  # noqa: F401
    except OSError as error:
        pytest.skip(f"WeasyPrint sem bibliotecas nativas neste ambiente ({type(error).__name__})")

    response = client.post(INVOICE, json=_payload())
    assert response.status_code == 200
    assert response.content.startswith(b"%PDF-")


def test_brl_and_percent_formats_req04() -> None:
    """REQ-04: formatação pt-BR de reais e percentuais, com arredondamento ROUND_HALF_EVEN (§6)."""
    assert invoice_service.brl(Decimal("1000000")) == "R$ 1.000.000,00"
    assert invoice_service.brl(Decimal("0.5")) == "R$ 0,50"
    assert invoice_service.brl(Decimal("2.345")) == "R$ 2,34"
    assert invoice_service.percent_br(Decimal("0.0125")) == "0,0125 %"
    assert invoice_service.percent_br(Decimal("2.0000")) == "2,00 %"
