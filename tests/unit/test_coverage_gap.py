"""Testes focados para cobrir linhas missing do relatório de cobertura."""

import pytest

from src.backend.config import Settings
from src.backend.main import _message_for
from src.backend.middleware.session import SessionData


def test_config_log_level_not_string():
    with pytest.raises(ValueError, match="O nível de log deve ser um texto"):
        Settings.model_validate({
            "database_url": "postgresql+asyncpg://localhost/db",
            "log_level": 123})


def test_config_log_level_invalid():
    with pytest.raises(ValueError, match="Nível de log inválido"):
        Settings.model_validate({
            "database_url": "postgresql+asyncpg://localhost/db",
            "log_level": "BOGUS"})


def test_message_for_custom_message():
    assert _message_for("meu_tipo_personalizado", "erro customizado") == "erro customizado"


def test_rate_service_repository_timeout_budget():
    from src.backend.services.rate_service import RateService
    with pytest.raises(ValueError, match="orçamento do repositório"):
        RateService(
            repository=None,
            providers=[],
            ttl_seconds=60,
            now=None,
            repository_timeout=10,
            total_timeout=20,
        )


def test_accept_rate_rejects():
    from decimal import Decimal
    from src.backend.services.rate_providers import _accept_rate
    assert _accept_rate(Decimal("5.5")) == Decimal("5.5")
    with pytest.raises(Exception):
        _accept_rate("não é decimal")
    with pytest.raises(Exception):
        _accept_rate(Decimal("Infinity"))
    with pytest.raises(Exception):
        _accept_rate(Decimal("999999999"))


def test_accept_bulletin_rejects():
    from src.backend.services.rate_providers import _accept_bulletin
    assert _accept_bulletin("2024-01-15") == "2024-01-15"
    with pytest.raises(Exception):
        _accept_bulletin(123)
    with pytest.raises(Exception):
        _accept_bulletin("x" * 200)
    with pytest.raises(Exception):
        _accept_bulletin("\x00")


def test_brasilia_to_utc():
    from src.backend.services.rate_providers import _brasilia_to_utc
    from datetime import datetime
    result = _brasilia_to_utc("2024-01-15T10:00:00")
    assert isinstance(result, datetime)
    with pytest.raises(Exception):
        _brasilia_to_utc("2024-01-15T10:00:00+00:00")


def test_handle_http_error_400():
    import asyncio
    from starlette.exceptions import HTTPException
    from src.backend.main import _handle_http_error
    from starlette.requests import Request
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/x",
        "headers": [],
        "query_string": b"",
        "client": None,
        "server": None,
    }
    req = Request(scope)
    resp = asyncio.run(_handle_http_error(req, HTTPException(status_code=400, detail="bad")))
    assert resp.status_code == 400


def test_gross_period_requires_quantity():
    from decimal import Decimal
    from src.backend.services.calculator import _gross
    with pytest.raises(ValueError, match="Regime por período exige quantidade"):
        _gross("periodo", Decimal("10"), None)


def test_refusing_url_fetcher():
    from src.backend.services.invoice_service import _RefusingUrlFetcher
    with pytest.raises(ValueError, match="Busca de recurso externo recusada"):
        _RefusingUrlFetcher()("http://example.com/x")


def test_as_utc_naive_rejected():
    from datetime import datetime
    from src.shared.schemas import _as_utc
    with pytest.raises(Exception):
        _as_utc(datetime(2024, 1, 15, 10, 0, 0))


# ---------- Routers: common.py (corpo JSON com Decimal e limite) ----------


def _json_request(body: bytes | None, headers: list | None = None):
    """Monta uma DecimalJsonRequest sintética com corpo fixo."""
    from src.backend.routers.common import DecimalJsonRequest

    pending = [body] if body is not None else []

    async def receive():
        if pending:
            data = pending.pop(0)
            return {"type": "http.request", "body": data, "more_body": bool(pending)}
        return {"type": "http.disconnect"}

    scope = {"type": "http", "method": "POST", "path": "/", "headers": headers or []}
    return DecimalJsonRequest(scope, receive)


def test_get_rate_service_devolve_o_servico_do_app_state():
    from types import SimpleNamespace

    from src.backend.routers.common import get_rate_service

    servico = object()
    request = SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace(rate_service=servico)))
    assert get_rate_service(request) is servico


def test_get_session_factory_entrega_fabrica_chamavel():
    from types import SimpleNamespace

    from src.backend.routers.common import get_session_factory

    request = SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace(engine=object())))
    assert callable(get_session_factory(request))


def test_decimal_json_request_recusa_content_length_acima_do_limite():
    import asyncio

    from src.backend.routers.common import MAX_BODY_BYTES, BodyTooLargeError

    request = _json_request(
        b"", headers=[(b"content-length", str(MAX_BODY_BYTES + 1).encode())]
    )
    with pytest.raises(BodyTooLargeError):
        asyncio.run(request.body())


def test_decimal_json_request_ler_chunks_e_recusa_excedente_no_stream():
    import asyncio

    from src.backend.routers.common import MAX_BODY_BYTES, BodyTooLargeError, DecimalJsonRequest

    excedente = [b"x" * (MAX_BODY_BYTES // 2 + 1), b"x" * MAX_BODY_BYTES]

    async def receive():
        if excedente:
            data = excedente.pop(0)
            return {"type": "http.request", "body": data, "more_body": bool(excedente)}
        return {"type": "http.disconnect"}

    request = DecimalJsonRequest(
        {"type": "http", "method": "POST", "path": "/", "headers": []}, receive
    )
    with pytest.raises(BodyTooLargeError):
        asyncio.run(request.body())


def test_decimal_json_request_json_com_decimal_exato():
    import asyncio
    from decimal import Decimal

    request = _json_request(b'{"valor": 30.1000000000000000000001}')
    parsed = asyncio.run(request.json())
    assert parsed["valor"] == Decimal("30.1000000000000000000001")


def test_decimal_json_request_recusa_nan():
    import asyncio
    import json

    request = _json_request(b'{"valor": NaN}')
    with pytest.raises(json.JSONDecodeError):
        asyncio.run(request.json())


def test_decimal_json_request_recusa_inteiro_gigante():
    import asyncio
    import json

    request = _json_request(b'{"valor": ' + b"9" * 5000 + b"}")
    with pytest.raises(json.JSONDecodeError):
        asyncio.run(request.json())


def test_decimal_json_request_recusa_refuse_constant():
    import json

    from src.backend.routers.common import _refuse_constant

    with pytest.raises(json.JSONDecodeError):
        _refuse_constant("NaN")


def test_decimal_json_route_via_testclient():
    from decimal import Decimal

    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from pydantic import BaseModel

    from src.backend.routers.common import DecimalJsonRoute

    class Eco(BaseModel):
        valor: Decimal

    app = FastAPI()
    app.router.route_class = DecimalJsonRoute

    @app.post("/eco")
    async def eco(item: Eco) -> dict[str, str]:
        return {"valor": str(item.valor)}

    cliente = TestClient(app)
    excedente = b'{"valor": "' + b"1" * 65536 + b'"}'
    resposta = cliente.post(
        "/eco", content=excedente, headers={"Content-Type": "application/json"}
    )
    assert resposta.status_code == 422
    assert "body_too_large" in resposta.text

    ok = cliente.post(
        "/eco", content=b'{"valor": 30.10}', headers={"Content-Type": "application/json"}
    )
    assert ok.status_code == 200
    assert ok.json()["valor"] == "30.10"


# ---------- Routers: invoices.py (listagem, finalize, clone, erase, PDF) ----------


def _make_stored_invoice(**overrides):
    """Invoice persistida sintética para os repositórios falsos dos routers."""
    from datetime import UTC, date, datetime
    from decimal import Decimal

    from src.backend.models.invoice_repository import StoredInvoice

    base = dict(
        id=1,
        owner_user_id=1,
        client_id=None,
        simulation_id=None,
        invoice_number="INV-0001",
        status="draft",
        locale="pt-BR",
        client_country_code="BR",
        issuer_name="Emitente Fictício",
        issuer_tax_id_digits="00000000000000",
        issuer_address=None,
        client_name="Cliente Fictício",
        client_tax_id_digits="00000000000001",
        client_address=None,
        banco=None,
        agencia=None,
        conta_com_digito=None,
        pix_key=None,
        periodo_inicio=date(2026, 1, 1),
        periodo_fim=date(2026, 1, 31),
        description="Serviço fictício",
        regime="hourly",
        currency="USD",
        amount=Decimal("30"),
        quantity=Decimal("160"),
        spread_pct=Decimal("2"),
        iof_pct=Decimal("0.38"),
        gross_foreign=Decimal("4800"),
        gross_brl=Decimal("24576"),
        spread_brl=Decimal("480"),
        iof_brl=Decimal("93.90"),
        net_brl=Decimal("24002.10"),
        effective_rate=Decimal("5.0004375"),
        quote_rate=Decimal("5.12"),
        quote_source="frankfurter",
        quote_bulletin=None,
        quoted_at=datetime(2026, 1, 31, 12, 0, 0, tzinfo=UTC),
        stale=False,
        finalized_at=None,
        supersedes_invoice_id=None,
        created_at=datetime(2026, 1, 31, 12, 0, 0, tzinfo=UTC),
        updated_at=datetime(2026, 1, 31, 12, 0, 0, tzinfo=UTC),
    )
    base.update(overrides)
    return StoredInvoice(**base)


class FakeInvoiceRepository:
    """Repositório de invoices em memória, sem banco (contrato InvoiceRepository)."""

    def __init__(self, invoices: list | None = None) -> None:
        self.invoices = list(invoices or [])
        self.deleted: list[tuple[int, int]] = []

    def _find(self, invoice_id: int, owner_user_id: int):
        for invoice in self.invoices:
            if invoice.id == invoice_id and invoice.owner_user_id == owner_user_id:
                return invoice
        return None

    async def get_by_id(self, invoice_id: int, owner_user_id: int):
        return self._find(invoice_id, owner_user_id)

    async def list_by_owner(
        self, owner_user_id: int, status: str | None = None,
        page: int = 1, page_size: int = 50,
    ):
        rows = [inv for inv in self.invoices if inv.owner_user_id == owner_user_id]
        if status is not None:
            rows = [inv for inv in rows if inv.status == status]
        return rows, len(rows)

    async def update_status(self, invoice_id: int, owner_user_id: int, new_status: str, when):
        from dataclasses import replace

        invoice = self._find(invoice_id, owner_user_id)
        if invoice is None:
            return None
        atualizada = replace(invoice, status=new_status, updated_at=when)
        self.invoices[self.invoices.index(invoice)] = atualizada
        return atualizada

    async def delete(self, invoice_id: int, owner_user_id: int) -> bool:
        invoice = self._find(invoice_id, owner_user_id)
        if invoice is None:
            return False
        self.invoices.remove(invoice)
        self.deleted.append((invoice_id, owner_user_id))
        return True

    async def clone(self, invoice_id: int, owner_user_id: int):
        original = self._find(invoice_id, owner_user_id)
        novo = _make_stored_invoice(
            id=original.id + 100,
            invoice_number="INV-CLONE",
            status="draft",
            supersedes_invoice_id=invoice_id,
        )
        self.invoices.append(novo)
        return novo


class _RepoSemUpdate(FakeInvoiceRepository):
    """Variante cujo update_status falha (cobre o 404 pós-consulta do finalize)."""

    async def update_status(self, invoice_id: int, owner_user_id: int, new_status: str, when):
        return None


def test_get_invoice_repo_empacota_o_repositorio():
    from src.backend.routers.invoices import get_invoice_repo

    assert get_invoice_repo(object()) is not None


def test_list_invoices_sem_e_com_filtro_de_status():
    import asyncio

    from src.backend.routers.invoices import list_invoices

    rascunho = _make_stored_invoice(id=1, status="draft")
    finalizada = _make_stored_invoice(id=2, status="finalized")
    repo = FakeInvoiceRepository([rascunho, finalizada])

    tudo = asyncio.run(
        list_invoices(object(), session=SessionData(1, 1), limit=50, offset=0, status=None, repo=repo)
    )
    assert [inv["id"] for inv in tudo] == [1, 2]

    filtrada = asyncio.run(
        list_invoices(
            object(), session=SessionData(1, 1), limit=50, offset=0, status="finalized", repo=repo
        )
    )
    assert [inv["id"] for inv in filtrada] == [2]


def test_finalize_invoice_fluxos_404_409_e_sucesso():
    import asyncio

    from fastapi import HTTPException

    from src.backend.routers.invoices import finalize_invoice

    with pytest.raises(HTTPException) as erro:
        asyncio.run(finalize_invoice(99, session=SessionData(1, 1), repo=FakeInvoiceRepository()))
    assert erro.value.status_code == 404

    finalizada = _make_stored_invoice(id=1, status="finalized")
    with pytest.raises(HTTPException) as erro:
        asyncio.run(
            finalize_invoice(1, session=SessionData(1, 1), repo=FakeInvoiceRepository([finalizada]))
        )
    assert erro.value.status_code == 409

    repo = FakeInvoiceRepository([_make_stored_invoice(id=1, status="draft")])
    resultado = asyncio.run(finalize_invoice(1, session=SessionData(1, 1), repo=repo))
    assert resultado["status"] == "finalized"

    repo_falho = _RepoSemUpdate([_make_stored_invoice(id=1, status="draft")])
    with pytest.raises(HTTPException) as erro:
        asyncio.run(finalize_invoice(1, session=SessionData(1, 1), repo=repo_falho))
    assert erro.value.status_code == 404


def test_clone_invoice_fluxos_404_409_e_sucesso():
    import asyncio

    from fastapi import HTTPException

    from src.backend.routers.invoices import clone_invoice

    with pytest.raises(HTTPException) as erro:
        asyncio.run(clone_invoice(99, session=SessionData(1, 1), repo=FakeInvoiceRepository()))
    assert erro.value.status_code == 404

    rascunho = _make_stored_invoice(id=1, status="draft")
    with pytest.raises(HTTPException) as erro:
        asyncio.run(clone_invoice(1, session=SessionData(1, 1), repo=FakeInvoiceRepository([rascunho])))
    assert erro.value.status_code == 409

    repo = FakeInvoiceRepository([_make_stored_invoice(id=1, status="finalized")])
    resposta = asyncio.run(clone_invoice(1, session=SessionData(1, 1), repo=repo))
    assert resposta.status == "draft"
    assert resposta.supersedes_invoice_id == 1
    assert resposta.invoice_id == 101


def test_erase_invoice_fluxos_404_409_e_sucesso():
    import asyncio

    from fastapi import HTTPException

    from src.backend.routers.invoices import erase_invoice

    with pytest.raises(HTTPException) as erro:
        asyncio.run(erase_invoice(99, session=SessionData(1, 1), repo=FakeInvoiceRepository()))
    assert erro.value.status_code == 404

    finalizada = _make_stored_invoice(id=1, status="finalized")
    with pytest.raises(HTTPException) as erro:
        asyncio.run(erase_invoice(1, session=SessionData(1, 1), repo=FakeInvoiceRepository([finalizada])))
    assert erro.value.status_code == 409

    repo = FakeInvoiceRepository([_make_stored_invoice(id=1, status="draft")])
    resposta = asyncio.run(erase_invoice(1, session=SessionData(1, 1), repo=repo))
    assert resposta.status_code == 204
    assert repo.deleted == [(1, 1)]


def test_get_invoice_pdf_renderiza_com_monkeypatch(monkeypatch):
    import asyncio

    from fastapi import HTTPException

    from src.backend.routers import invoices

    repo = FakeInvoiceRepository([_make_stored_invoice(id=7, status="finalized")])

    async def _pdf_falso(invoice, rate_service):
        return b"%PDF-1.4 falso"

    monkeypatch.setattr(invoices, "render_pdf_from_stored", _pdf_falso)
    resposta = asyncio.run(
        invoices.get_invoice_pdf(7, object(), session=SessionData(1, 1), repo=repo)
    )
    assert resposta.status_code == 200
    assert resposta.body == b"%PDF-1.4 falso"
    assert "invoice_INV-0001.pdf" in resposta.headers["content-disposition"]

    with pytest.raises(HTTPException) as erro:
        asyncio.run(invoices.get_invoice_pdf(999, object(), session=SessionData(1, 1), repo=repo))
    assert erro.value.status_code == 404


def test_post_invoice_devolve_pdf_com_monkeypatch(monkeypatch):
    import asyncio

    from src.backend.routers import invoices
    from src.shared.schemas import InvoiceRequest

    exemplo = InvoiceRequest.model_config["json_schema_extra"]["examples"][0]
    payload = InvoiceRequest.model_validate(exemplo)

    async def _pdf_falso(payload, rate_service):
        return b"%PDF-1.4 falso"

    monkeypatch.setattr(invoices, "render_invoice", _pdf_falso)
    resposta = asyncio.run(invoices.post_invoice(payload, object()))
    assert resposta.status_code == 200
    assert resposta.body == b"%PDF-1.4 falso"
    assert resposta.headers["cache-control"] == "no-store"
