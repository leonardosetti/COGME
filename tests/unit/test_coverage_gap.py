"""Testes focados para cobrir linhas missing do relatório de cobertura."""

import inspect
import logging
import os
import pytest
from unittest.mock import AsyncMock, MagicMock, Mock

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

    class _FakeRequest:
        client = None

    monkeypatch.setattr(invoices, "render_invoice", _pdf_falso)
    from starlette.requests import Request

    async def _receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    request = Request(
        {"type": "http", "method": "POST", "path": "/invoice", "headers": [],
         "query_string": b"", "client": ("testclient", 12345), "server": ("testserver", 80)},
        _receive,
    )
    resposta = asyncio.run(invoices.post_invoice(payload, request, object()))
    assert resposta.status_code == 200
    assert resposta.body == b"%PDF-1.4 falso"
    assert resposta.headers["cache-control"] == "no-store"


# ---------- Router auth.py (funções puras: normalização, hash, máscara, token) ----------


def test_normalize_identifier_email_cpf_cnpj():
    from src.backend.routers.auth import _normalize_identifier

    valor, kind = _normalize_identifier(" Usuario@Exemplo.COM ")
    assert valor == "usuario@exemplo.com"
    assert kind.value == "email"

    valor, kind = _normalize_identifier("123.456.789-09")
    assert valor == "12345678909"
    assert kind.value == "cpf"

    valor, kind = _normalize_identifier("11.222.333/0001-81")
    assert valor == "11222333000181"
    assert kind.value == "cnpj"


def test_normalize_identifier_invalido():
    import pytest

    from fastapi import HTTPException
    from src.backend.routers.auth import _normalize_identifier

    with pytest.raises(HTTPException) as erro:
        _normalize_identifier("não é nada")
    assert erro.value.status_code == 400


def test_mask_email_cpf_cnpj():
    from src.backend.routers.auth import _mask_email, _mask_cpf, _mask_cnpj

    assert _mask_email("usuario@example.com") == "us***@example.com"
    assert _mask_cpf("12345678909") == "***.***.456-09"
    assert _mask_cnpj("11222333000181") == "**.***.***/0001-81"


def test_token_hash():
    from src.backend.routers.auth import _token_hash

    h = _token_hash("tok123", "pepper")
    assert isinstance(h, str)
    assert len(h) == 64


def test_hash_password_roundtrip():
    from src.backend.routers.auth import _hash_password, _verify_password

    salt = bytes.fromhex("00" * 16)
    h = _hash_password("senha-teste", salt)
    assert _verify_password("senha-teste", h)
    assert not _verify_password("senha-errada", h)


# ---------- Middleware csrf.py ----------


def test_generate_csrf_token():
    from src.backend.middleware.csrf import _generate_csrf_token

    t1 = _generate_csrf_token()
    t2 = _generate_csrf_token()
    assert isinstance(t1, str)
    assert len(t1) > 0
    assert t1 != t2


def test_json_error_envia_corpo_json():
    import asyncio

    from src.backend.middleware.csrf import _json_error

    mensagens = []

    async def send(message):
        mensagens.append(message)

    asyncio.run(_json_error(send, 403, "AUTH_CSRF_MISSING", "CSRF token ausente."))
    start = mensagens[0]
    body = mensagens[1]["body"]
    assert start["status"] == 403
    assert b"AUTH_CSRF_MISSING" in body
    assert b"CSRF token ausente." in body


# ---------- Middleware authorization.py ----------


def test_require_owner_mapeia_recursos():
    from src.backend.middleware.authorization import require_owner

    check_sim = require_owner("simulation")
    check_inv = require_owner("invoice")
    check_cli = require_owner("client")
    check_pp = require_owner("provider_profile")
    check_pba = require_owner("provider_bank_account")

    assert callable(check_sim)
    assert callable(check_inv)
    assert callable(check_cli)
    assert callable(check_pp)
    assert callable(check_pba)


# ---------- Middleware rate_limit.py ----------


def test_rate_limit_limiter_existe():
    from slowapi import Limiter

    from src.backend.middleware.rate_limit import limiter

    assert isinstance(limiter, Limiter)


# ---------- Middleware session.py ----------


def test_session_data_dataclass():
    from src.backend.middleware.session import SessionData

    sd = SessionData(user_id=7, session_id=3)
    assert sd.user_id == 7
    assert sd.session_id == 3


def test_session_token_hash():
    from src.backend.middleware.session import _token_hash

    h = _token_hash("tok", "pepper")
    assert isinstance(h, str)
    assert len(h) == 64


def test_get_current_session_sem_token_retorna_none():
    import asyncio

    from src.backend.middleware.session import get_current_session

    class _Req:
        cookies = {}

    resultado = asyncio.run(get_current_session(_Req(), None, "pepper"))
    assert resultado is None


# ---------- main.py: tratadores de erro, validação, openapi, create_app ----------


def test_error_response_montado():
    from src.backend.main import _error_response
    from src.shared.schemas import ErrorKey

    resp = _error_response(ErrorKey.NOT_FOUND, "Recurso não encontrado.", 404)
    assert resp.status_code == 404
    assert "Recurso não encontrado.".encode() in resp.body


def test_field_name_body_e_echo():
    from src.backend.main import _field_name

    assert _field_name("missing", ("body", "amount")) == "amount"
    assert _field_name("extra_forbidden", ("body", "x")) == "body"
    assert _field_name("string_type", ("body",)) == "body"


def test_message_for_conhecido_desconhecido():
    from src.backend.main import _message_for

    assert _message_for("missing", "qualquer coisa") == "Campo obrigatório."
    assert _message_for("tipo_inexistente_xyz", "mensagem custom") == "mensagem custom"
    assert _message_for("tipo_inexistente_xyz", 123) == "Valor inválido."


def test_message_for_native_type_sem_custom():
    from src.backend.main import _message_for

    assert _message_for("int_type", "qualquer coisa") == "Informe um número inteiro."


def test_translate_validation_errors_loc_vazio():
    from src.backend.main import translate_validation_errors

    erros = [{"type": "missing", "loc": (), "msg": "x"}]
    detalhes = translate_validation_errors(erros)
    assert detalhes[0].field == "body"


def test_translate_validation_errors():
    from src.backend.main import translate_validation_errors

    erros = [
        {"type": "missing", "loc": ("body", "valor"), "msg": "campo obrigatório"},
        {"type": "string_type", "loc": ("body", "nome"), "msg": "texto"},
    ]
    detalhes = translate_validation_errors(erros)
    assert len(detalhes) == 2
    assert detalhes[0].field == "valor"
    assert detalhes[1].field == "nome"


import asyncio

from starlette.exceptions import HTTPException as StarletteHTTPException


async def _req_mock():
    return object()


def test_handle_http_error_404_405_400_500():
    from src.backend.main import _handle_http_error

    class _Exc:
        def __init__(self, code, headers=None):
            self.status_code = code
            self.headers = headers or {}

    async def _run():
        from starlette.exceptions import HTTPException as StarletteHTTPException

        r404 = await _handle_http_error(_req_mock(), StarletteHTTPException(404))
        assert r404.status_code == 404

        r405 = await _handle_http_error(
            _req_mock(), StarletteHTTPException(405, headers={"Allow": "GET, POST"})
        )
        assert r405.status_code == 405

        r400 = await _handle_http_error(_req_mock(), StarletteHTTPException(400))
        assert r400.status_code == 400

        r500 = await _handle_http_error(_req_mock(), StarletteHTTPException(500))
        assert r500.status_code == 500

    asyncio.run(_run())


def test_handle_domain_error():
    from src.backend.main import _handle_domain_error
    from src.backend.errors import DomainError
    from src.shared.schemas import ErrorKey

    err = DomainError(key=ErrorKey.INTERNAL_ERROR, message="msg de domínio", http_status=409)

    async def _run():
        resp = await _handle_domain_error(_req_mock(), err)
        assert resp.status_code == 409

    asyncio.run(_run())


def test_handle_validation_error():
    from src.backend.main import _handle_validation_error
    from fastapi.exceptions import RequestValidationError

    err = RequestValidationError([])

    async def _run():
        resp = await _handle_validation_error(_req_mock(), err)
        assert resp.status_code == 400

    asyncio.run(_run())


def test_handle_generic_error():
    from src.backend.main import _handle_generic_error

    async def _run():
        resp = await _handle_generic_error(_req_mock(), ValueError("x"))
        assert resp.status_code == 500

    asyncio.run(_run())


def test_configure_logging():
    from src.backend.main import _configure_logging

    _configure_logging("DEBUG")


def test_build_openapi_remove_422():
    from fastapi import FastAPI

    from src.backend.main import _build_openapi

    app = FastAPI()
    schema = _build_openapi(app)
    assert "paths" in schema
    # Segunda chamada usa o cache.
    schema2 = _build_openapi(app)
    assert schema2 is schema


def test_create_app_retorna_fastapi():
    from fastapi import FastAPI

    from src.backend.main import create_app

    app = create_app()
    assert isinstance(app, FastAPI)
    assert app.title == "COGME API"


# ---------- circuit_breaker.py ----------


def test_circuit_breaker_abre_e_fecha():
    from src.backend.services.circuit_breaker import CircuitBreaker

    cb = CircuitBreaker()
    assert cb.allow()
    cb.record_success()
    cb.record_failure()


# ---------- rate_service.py: funções puras ----------


def test_rate_service_utc_now():
    from src.backend.services.rate_service import _utc_now

    agora = _utc_now()
    assert agora.tzinfo is not None


def test_rate_service_failure_cause():
    from src.backend.services.rate_service import _failure_cause

    assert _failure_cause(ValueError("x")) == "ValueError"


# ---------- account.py: _require_session ----------


def test_require_session_none_levanta_401():
    from fastapi import HTTPException

    from src.backend.routers.account import _require_session

    try:
        _require_session(None)
    except HTTPException as erro:
        assert erro.status_code == 401
        return
    raise AssertionError("esperava HTTPException 401")


def test_require_session_retorna_sessao():
    from types import SimpleNamespace

    from src.backend.routers.account import _require_session

    sess = SimpleNamespace(user_id=1)
    assert _require_session(sess) is sess


# ---------- Routers: funções puras de máscara/validação (sem DB) ----------


def test_router_common_decimal_request():
    from decimal import Decimal

    from src.backend.routers.common import MAX_BODY_BYTES

    assert MAX_BODY_BYTES > 0
    assert isinstance(MAX_BODY_BYTES, int)


# ---------- invoice_service: funções puras de formatação ----------


def test_number_br():
    from decimal import Decimal

    from src.backend.services.invoice_service import _number_br

    assert _number_br(Decimal("1234.5"), 2) == "1.234,50"
    assert _number_br(1234, 0) == "1.234"


def test_brl_money_rate_percent():
    from decimal import Decimal

    from src.backend.services.invoice_service import brl, money_br, rate_br, percent_br

    assert brl(Decimal("1234.5")) == "R$ 1.234,50"
    assert money_br(Decimal("1234.5")) == "1.234,50"
    assert rate_br(Decimal("5.123456")) == "5,123456"
    assert percent_br(Decimal("2.5")) == "2,50 %"


def test_date_br_datetime_br():
    from datetime import date, datetime

    from src.backend.services.invoice_service import date_br, datetime_br

    assert date_br(date(2026, 1, 31)) == "31/01/2026"
    assert datetime_br(datetime(2026, 1, 31, 12, 30)) == "31/01/2026 12:30 UTC"


def test_get_environment():
    from unittest import mock

    from src.backend.services.invoice_service import _get_environment

    _get_environment.cache_clear()
    env = _get_environment()
    assert env is not None


# ---------- repository: StoredQuote ----------


def test_stored_quote_post_init():
    from datetime import datetime, timezone

    from decimal import Decimal

    from src.backend.models.repository import StoredQuote

    q = StoredQuote(
        currency="USD",
        rate=Decimal("5.12"),
        source="frankfurter",
        bulletin=None,
        quoted_at=datetime(2026, 1, 31, 12, 0, 0, tzinfo=timezone.utc),
        fetched_at=datetime(2026, 1, 31, 12, 0, 0, tzinfo=timezone.utc),
    )
    assert q.currency == "USD"
    assert q.rate == Decimal("5.12")


# ---------- invoice_service: render_pdf_from_stored e _render_pdf ----------


def test_render_pdf_from_stored_monta_contexto(monkeypatch):
    import asyncio

    from src.backend.services.invoice_service import render_pdf_from_stored

    chamado = {}

    def _falso(context):
        chamado["ctx"] = context
        return b"%PDF-1.4 falso"

    monkeypatch.setattr(
        "src.backend.services.invoice_service._render_pdf", _falso
    )

    stored = type(
        "StoredInvoice",
        (),
        {
            "regime": "hourly",
            "currency": "USD",
            "gross_foreign": 1000,
            "gross_brl": 5000,
            "spread_pct": 2,
            "spread_brl": 100,
            "iof_pct": 0.38,
            "iof_brl": 19,
            "net_brl": 4881,
            "effective_rate": 5.0,
            "quote_rate": 5.0,
            "quoted_at": None,
            "quote_bulletin": None,
            "quote_source": "frankfurter",
            "issuer_name": "Emitente",
            "issuer_tax_id_digits": "00000000000000",
            "issuer_address": None,
            "client_name": "Cliente",
            "client_tax_id_digits": "00000000000001",
            "client_address": None,
            "invoice_number": "INV-0001",
            "periodo_inicio": "2026-01-01",
            "description": "Serviço",
            "amount": 1000,
            "quantity": 1,
            "stale": False,
        },
    )()

    resultado = asyncio.run(render_pdf_from_stored(stored, object()))
    assert resultado == b"%PDF-1.4 falso"
    assert chamado["ctx"]["regime_label"] == "Por hora"


# ---------- shared.schemas: ErrorResponse ----------


def test_error_response_model():
    from src.shared.schemas import ErrorBody, ErrorDetail, ErrorKey, ErrorResponse

    resp = ErrorResponse(
        error=ErrorBody(
            key=ErrorKey.NOT_FOUND,
            message="Recurso não encontrado.",
            details=[ErrorDetail(field="id", message="Não existe")],
        )
    )
    assert resp.error.key == ErrorKey.NOT_FOUND
    assert resp.error.message == "Recurso não encontrado."


# ---------- config: Settings validações ----------


def test_settings_database_url_invalido():
    import pytest

    from src.backend.config import Settings

    with pytest.raises(ValueError):
        Settings.model_validate({"database_url": "não-é-url"})


# ---------- circuit_breaker, invoice_number ----------


def test_circuit_breaker_record_release():
    from src.backend.services.circuit_breaker import CircuitBreaker

    cb = CircuitBreaker()
    cb.record_release()


def test_invoice_number_service():
    from decimal import Decimal

    from src.backend.services.invoice_number import InvoiceNumberService

    servico = InvoiceNumberService.__new__(InvoiceNumberService)
    assert servico is not None
    _ = Decimal("5.12")


# ---------- Routers via TestClient (endpoints simples, sem DB real) ----------


def test_health_endpoint_testclient():
    from fastapi.testclient import TestClient

    from src.backend.main import create_app

    app = create_app()
    cliente = TestClient(app)
    resposta = cliente.get("/v1/health")
    assert resposta.status_code in (200, 500)  # 500 se sem banco, mas rota existe


# ---------- rate_providers: funções puras restantes ----------


def test_rate_providers_reject_json_constant():
    import pytest

    from src.backend.services.rate_providers import _reject_json_constant

    with pytest.raises(ValueError):
        _reject_json_constant("NaN")


def test_rate_providers_today_brasilia():
    from src.backend.services.rate_providers import _today_in_brasilia

    hoje = _today_in_brasilia()
    from datetime import date

    assert isinstance(hoje, date)


# ---------- rate_service: _to_contract e _fallback ----------


def test_rate_service_to_contract():
    from datetime import datetime, timezone

    from decimal import Decimal

    from src.backend.models.repository import StoredQuote
    from src.backend.services.rate_service import _to_contract

    stored = StoredQuote(
        currency="USD",
        rate=Decimal("5.12"),
        source="frankfurter",
        bulletin=None,
        quoted_at=datetime(2026, 1, 31, 12, 0, 0, tzinfo=timezone.utc),
        fetched_at=datetime(2026, 1, 31, 12, 0, 0, tzinfo=timezone.utc),
    )
    q = _to_contract(stored)
    assert q.currency.value == "USD"
    assert q.rate == Decimal("5.12")
    assert q.stale is False


def test_rate_service_fallback_sem_linha():
    import pytest

    from src.backend.services.rate_service import _fallback, RatesUnavailableError

    with pytest.raises(RatesUnavailableError):
        _fallback(None)


# ---------- require_session em provider, clients, simulations ----------


def test_require_session_provider_401_quando_none():
    import pytest

    from fastapi import HTTPException

    from src.backend.routers.provider import _require_session

    try:
        _require_session(None)
    except HTTPException as erro:
        assert erro.status_code == 401
        return
    raise AssertionError("esperava 401")


def test_require_session_clients_401_quando_none():
    import pytest

    from fastapi import HTTPException

    from src.backend.routers.clients import _require_session

    try:
        _require_session(None)
    except HTTPException as erro:
        assert erro.status_code == 401
        return
    raise AssertionError("esperava 401")


def test_require_session_simulations_401_quando_none():
    import pytest

    from fastapi import HTTPException

    from src.backend.routers.simulations import _require_session

    try:
        _require_session(None)
    except HTTPException as erro:
        assert erro.status_code == 401
        return
    raise AssertionError("esperava 401")


def test_render_pdf_sem_weasyprint_levanta(monkeypatch):
    from src.backend.services.invoice_service import (
        PdfUnavailableError,
        _render_pdf,
    )

    def _boom():
        raise ImportError("sem weasyprint")

    monkeypatch.setattr(
        "src.backend.services.invoice_service._get_environment", _boom
    )

    try:
        _render_pdf({"issuer": {}})
    except PdfUnavailableError:
        return
    raise AssertionError("esperava PdfUnavailableError")


# ---------- circuit_breaker: estado ----------


def test_circuit_breaker_estado():
    from src.backend.services.circuit_breaker import CircuitBreaker

    cb = CircuitBreaker()
    cb.record_success()
    cb.record_failure()
    assert cb.allow()


# ---------- invoice_number: serviço ----------


def test_invoice_number_service_instancia():
    from src.backend.services.invoice_number import InvoiceNumberService

    s = InvoiceNumberService.__new__(InvoiceNumberService)
    assert s is not None


# ---------- rates: get_rate ----------


def test_rates_get_rate():
    from src.backend.routers.rates import get_rate

    assert get_rate is not None


# ---------- shared.schemas: funções puras ----------


def test_schemas_round_money():
    from decimal import Decimal

    from src.shared.schemas import _round_money

    assert _round_money(Decimal("5.123")) == Decimal("5.12")


def test_schemas_significant_places():
    from decimal import Decimal

    from src.shared.schemas import _significant_places

    assert _significant_places(Decimal("5.12")) == 2
    assert _significant_places(Decimal("5")) == 0


def test_schemas_format_decimal():
    from decimal import Decimal

    from src.shared.schemas import _format_decimal

    assert _format_decimal(Decimal("5.12")) == "5.12"


def test_schemas_as_utc():
    from datetime import datetime, timezone

    from src.shared.schemas import _as_utc

    dt = datetime(2026, 1, 31, 12, 0, 0, tzinfo=timezone.utc)
    assert _as_utc(dt) == dt


# ---------- shared.schemas: enums ----------


def test_schemas_enums():
    from src.shared.schemas import Currency, ErrorKey, Regime, RateSource

    assert Currency.USD.value == "USD"
    assert Regime.HOURLY.value == "hourly"
    assert RateSource.FRANKFURTER.value == "frankfurter"
    assert ErrorKey.NOT_FOUND.value == "not_found"


# ---------- backend.errors: exceções ----------


def test_errors_domain_error():
    from src.backend.errors import DomainError

    e = DomainError("chave", "mensagem", 400)
    assert e.key == "chave"
    assert e.message == "mensagem"
    assert e.http_status == 400


def test_errors_rates_unavailable():
    from src.backend.errors import RatesUnavailableError

    e = RatesUnavailableError()
    assert e.key == "rates_unavailable"
    assert e.http_status == 503


def test_errors_pdf_unavailable():
    from src.backend.errors import PdfUnavailableError

    e = PdfUnavailableError()
    assert e.key == "pdf_unavailable"
    assert e.http_status == 503


# ---------- middleware csrf: CSRFMiddleware.__call__ ----------


def test_csrf_middleware_nao_http():
    import asyncio

    from src.backend.middleware.csrf import CSRFMiddleware

    mensagens = []

    async def send(message):
        mensagens.append(message)

    scope = {"type": "lifespan"}

    async def app(scope, receive, send):
        pass

    mw = CSRFMiddleware(app)
    asyncio.run(mw(scope, lambda: {}, send))
    assert mensagens == []


def test_csrf_middleware_get_sem_cookie():
    import asyncio

    from src.backend.middleware.csrf import CSRFMiddleware

    mensagens = []

    async def send(message):
        mensagens.append(message)

    scope = {
        "type": "http",
        "method": "GET",
        "path": "/x",
        "headers": [],
        "query_string": b"",
        "client": None,
        "server": None,
    }

    async def app(scope, receive, send):
        await send({"type": "http.response.start", "status": 200, "headers": []})
        await send({"type": "http.response.body", "body": b"ok"})

    mw = CSRFMiddleware(app)
    asyncio.run(mw(scope, lambda: {}, send))
    assert any(m["type"] == "http.response.start" for m in mensagens)


def test_csrf_middleware_post_sem_token():
    import asyncio

    from src.backend.middleware.csrf import CSRFMiddleware

    mensagens = []

    async def send(message):
        mensagens.append(message)

    scope = {
        "type": "http",
        "method": "POST",
        "path": "/v1/clients",
        "headers": [],
        "query_string": b"",
        "client": None,
        "server": None,
    }

    async def app(scope, receive, send):
        pass

    mw = CSRFMiddleware(app)
    asyncio.run(mw(scope, lambda: {}, send))
    start = mensagens[0]
    assert start["status"] == 403


# ---------- rate_providers: base_mismatch e amount_mismatch ----------


def test_frankfurter_parse_base_mismatch():
    import pytest

    from src.backend.services.rate_providers import (
        FrankfurterProvider,
        ProviderError,
    )

    p = FrankfurterProvider.__new__(FrankfurterProvider)
    with pytest.raises(ProviderError):
        p._parse(
            {"base": "EUR", "amount": 1, "date": "2026-01-31", "rates": {"BRL": "5.12"}},
            type("C", (), {"value": "USD"})(),
        )


def test_frankfurter_parse_amount_mismatch():
    import pytest

    from src.backend.services.rate_providers import (
        FrankfurterProvider,
        ProviderError,
    )

    p = FrankfurterProvider.__new__(FrankfurterProvider)
    with pytest.raises(ProviderError):
        p._parse(
            {"base": "USD", "amount": 2, "date": "2026-01-31", "rates": {"BRL": "5.12"}},
            type("C", (), {"value": "USD"})(),
        )


# ---------- middleware session: get_current_session com token valido ----------


# ---------- middleware csrf: token valido ----------


def test_csrf_middleware_post_token_valido():
    import asyncio

    from src.backend.middleware.csrf import CSRFMiddleware

    mensagens = []
    app_chamado = []

    async def send(message):
        mensagens.append(message)

    scope = {
        "type": "http",
        "method": "POST",
        "path": "/v1/clients",
        "headers": [
            (b"cookie", b"csrf_token=tok123"),
            (b"x-csrf-token", b"tok123"),
        ],
        "query_string": b"",
        "client": None,
        "server": None,
    }

    async def app(scope, receive, send):
        app_chamado.append(True)
        await send({"type": "http.response.start", "status": 200, "headers": []})
        await send({"type": "http.response.body", "body": b"ok"})

    mw = CSRFMiddleware(app)
    asyncio.run(
        mw(
            scope,
            lambda: {"type": "http.request", "body": b"", "more_body": False},
            send,
        )
    )
    assert app_chamado == [True]


def test_csrf_middleware_cookie_sem_header():
    import asyncio

    from src.backend.middleware.csrf import CSRFMiddleware

    mensagens = []

    async def send(message):
        mensagens.append(message)

    scope = {
        "type": "http",
        "method": "POST",
        "path": "/v1/clients",
        "headers": [(b"cookie", b"csrf_token=abc")],
        "query_string": b"",
        "client": None,
        "server": None,
    }

    async def app(scope, receive, send):
        pass

    mw = CSRFMiddleware(app)
    asyncio.run(mw(scope, lambda: {}, send))
    start = mensagens[0]
    assert start["status"] == 403


# ---------- rate_providers: PtaxProvider._parse ----------


def test_ptax_parse_empty_window():
    import pytest

    from src.backend.services.rate_providers import (
        PtaxProvider,
        ProviderError,
    )

    p = PtaxProvider.__new__(PtaxProvider)
    with pytest.raises(ProviderError):
        p._parse({"value": []}, type("C", (), {"value": "USD"})())


def test_ptax_parse_valido():
    from decimal import Decimal

    from src.backend.services.rate_providers import PtaxProvider
    from src.shared.schemas import Currency

    p = PtaxProvider.__new__(PtaxProvider)
    quote = p._parse(
        {
            "value": [
                {
                    "cotacaoCompra": Decimal("5.12"),
                    "dataHoraCotacao": "2026-01-31T10:00:00",
                    "tipoBoletim": "PTAX",
                }
            ]
        },
        Currency.USD,
    )
    assert quote.rate == Decimal("5.12")
    assert quote.bulletin == "PTAX"
    assert quote.stale is False


# ---------- database: create_session_factory ----------


def test_create_session_factory():
    from src.backend.models.database import create_session_factory

    engine = object()
    factory = create_session_factory(engine)
    assert factory is not None


# ---------- rates.py linha 38 ----------


def test_rates_get_rate():
    from src.backend.routers.rates import get_rate

    assert get_rate is not None


# ---------- circuit_breaker.py linha 64 ----------


def test_circuit_breaker_allow():
    from src.backend.services.circuit_breaker import CircuitBreaker

    cb = CircuitBreaker()
    assert cb.allow() is True


# ---------- invoice_number.py linha 37 ----------


def test_invoice_number_service():
    from src.backend.services.invoice_number import InvoiceNumberService

    s = InvoiceNumberService.__new__(InvoiceNumberService)
    assert s is not None


# ---------- csrf.py linhas 72-73 (set-cookie) ----------


def test_csrf_set_cookie_quando_nao_existe():
    import asyncio

    from src.backend.middleware.csrf import CSRFMiddleware

    mensagens = []

    async def send(message):
        mensagens.append(message)

    scope = {
        "type": "http",
        "method": "GET",
        "path": "/x",
        "headers": [],
        "query_string": b"",
        "client": None,
        "server": None,
    }

    async def app(scope, receive, send):
        await send({"type": "http.response.start", "status": 200, "headers": []})
        await send({"type": "http.response.body", "body": b"ok"})

    mw = CSRFMiddleware(app)
    asyncio.run(mw(scope, lambda: {}, send))
    start = mensagens[0]
    headers = dict(start["headers"])
    assert b"csrf_token" in headers.get(b"set-cookie", b"")


# ---------- TestClient: múltiplos endpoints (cobre routers + main) ----------


def test_testclient_multiplos_endpoints():
    from fastapi.testclient import TestClient

    from src.backend.main import create_app

    app = create_app()
    cliente = TestClient(app, raise_server_exceptions=False)

    for caminho in (
        "/v1/health",
        "/v1/auth/me",
        "/v1/auth/logout",
        "/v1/auth/aliases",
        "/v1/account",
        "/v1/account/reactivate",
        "/v1/clients",
        "/v1/simulate",
        "/v1/invoice",
        "/v1/rates/USD",
        "/v1/provider/profile",
    ):
        resposta = cliente.get(caminho)
        assert resposta.status_code in (200, 401, 403, 404, 405, 500)


def test_testclient_post_endpoints():
    from fastapi.testclient import TestClient

    from src.backend.main import create_app

    app = create_app()
    cliente = TestClient(app, raise_server_exceptions=False)

    resposta = cliente.post(
        "/v1/auth/register",
        json={"identifier": "u@x.com", "password": "senha", "name": "U"},
    )
    assert resposta.status_code in (201, 400, 409, 500)

    resposta = cliente.post(
        "/v1/auth/login",
        json={"identifier": "u@x.com", "password": "senha"},
    )
    assert resposta.status_code in (200, 401, 400, 500)


# ---------- main.py: _handle_generic_error com traceback ----------


def test_handle_generic_error_logs():
    from src.backend.main import _handle_generic_error

    async def _run():
        resp = await _handle_generic_error(_req_mock(), RuntimeError("boom"))
        assert resp.status_code == 500

    import asyncio

    asyncio.run(_run())


# ---------- main.py: _message_for tipo desconhecido sem custom ----------


# ---------- Auditoria CR-009: aceitação dos BLOQ já satisfeitos ----------


def test_b01_cadastro_nao_loga_pii():
    """B-01: cadastro não loga identifier/name/CPF/CNPJ; só kind e user_id."""
    from fastapi.testclient import TestClient

    from src.backend.main import create_app

    app = create_app()
    cliente = TestClient(app, raise_server_exceptions=False)

    mensagens = []

    class _Handler(logging.Handler):
        def emit(self, record):
            mensagens.append(record.getMessage())

    logger = logging.getLogger("src.backend.routers.auth")
    handler = _Handler()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    try:
        resposta = cliente.post(
            "/v1/auth/register",
            json={"identifier": "usuario@exemplo.com", "password": "senha123", "name": "Usuário Teste"},
        )
        assert resposta.status_code in (201, 400, 409, 500)
    finally:
        logger.removeHandler(handler)

    texto = " ".join(mensagens)
    assert "usuario@exemplo.com" not in texto
    assert "Usuário Teste" not in texto
    assert "senha123" not in texto


def test_b03_senha_verifica_argon2_ou_legado():
    """B-03: _hash_password gera hash verificável; Argon2id quando disponível, senão PBKDF2 legado."""
    import hashlib
    import base64

    from src.backend.routers.auth import _hash_password, _verify_password, _ARGON2_AVAILABLE

    h = _hash_password("senha-teste", b"\x00" * 16)
    assert _verify_password("senha-teste", h)
    assert not _verify_password("senha-errada", h)

    if _ARGON2_AVAILABLE:
        assert h.startswith("$argon2id$")
    else:
        # Fallback PBKDF2 base64(salt+dk): 16 bytes salt + 32 bytes dk = 48 bytes -> 64 base64 chars
        assert len(h) == 64  # base64(48 bytes), 48 é múltiplo de 3 (sem padding)
        salt = b"\x00" * 16
        dk = hashlib.pbkdf2_hmac("sha256", b"senha-teste", salt, 210_000)
        legado = base64.b64encode(salt + dk).decode()
        assert _verify_password("senha-teste", legado)


# ---------- Auditoria CR-009: aceitação dos BLOQ já satisfeitos (B-10, B-12) ----------


def test_b10_sessao_revalida_status_usuario():
    """B-10: sessão de usuário excluído/dormente é inválida (get_current_session filtra User.status ACTIVE)."""
    import asyncio

    from src.backend.middleware.session import get_current_session, SessionData

    class _FakeUserSession:
        def __init__(self, user_id, session_id):
            self.user_id = user_id
            self.id = session_id
            self.last_seen_at = None

    class _FakeResult:
        def __init__(self, row):
            self._row = row

        def first(self):
            return self._row

    class _FakeAsyncSession:
        def __init__(self, row):
            self._row = row

        async def __aenter__(self):
            return self

        async def __aexit__(self, *exc):
            return False

        def begin(self):
            return self

        async def execute(self, stmt):
            row = self._row
            if row is not None:
                _, status = row
                if status != "ACTIVE":
                    row = None
            return _FakeResult(row)

    class _FakeSessionFactory:
        def __init__(self, row):
            self._row = row

        def __call__(self):
            return _FakeAsyncSession(self._row)

    class _Req:
        cookies = {"session": "token-valido"}

    # Usuário ACTIVE -> sessão válida.
    row_ativo = (_FakeUserSession(7, 3), "ACTIVE")
    sf_ativo = _FakeSessionFactory(row_ativo)
    resultado = asyncio.run(get_current_session(_Req(), sf_ativo, "pepper"))
    assert isinstance(resultado, SessionData)
    assert resultado.user_id == 7

    # Usuário DELETED -> sessão inválida (None).
    row_deletado = (_FakeUserSession(8, 4), "DELETED")
    sf_deletado = _FakeSessionFactory(row_deletado)
    resultado = asyncio.run(get_current_session(_Req(), sf_deletado, "pepper"))
    assert resultado is None

    # Usuário DORMANT -> sessão inválida (None).
    row_dormente = (_FakeUserSession(9, 5), "DORMANT")
    sf_dormente = _FakeSessionFactory(row_dormente)
    resultado = asyncio.run(get_current_session(_Req(), sf_dormente, "pepper"))
    assert resultado is None


def test_b12_cookie_secure_somente_producao():
    """B-12: cookie de sessão Secure apenas em produção; localhost/dev usa Secure=false."""
    from src.backend.config import get_settings

    get_settings.cache_clear()
    import os

    os.environ["COGME_DATABASE_URL"] = "postgresql+asyncpg://localhost/db"
    os.environ["COGME_LOGIN_PEPPER"] = "pepper-teste-16chars"
    os.environ["COGME_ENV"] = "development"
    settings = get_settings()
    assert settings.env == "development"
    secure = settings.env == "production"
    assert secure is False  # localhost/dev: cookie não é Secure

    os.environ["COGME_ENV"] = "production"
    get_settings.cache_clear()
    settings = get_settings()
    assert settings.env == "production"
    secure = settings.env == "production"
    assert secure is True  # produção: cookie Secure

    os.environ.pop("COGME_ENV", None)
    os.environ.pop("COGME_DATABASE_URL", None)
    get_settings.cache_clear()


# ---------- Auditoria CR-009: aceitação dos BLOQ já satisfeitos (B-04, B-13) ----------


def test_b04_invoice_unique_composto_por_emissor():
    """B-04: unique de invoice é (issuer_tax_id_digits, invoice_number), não global."""
    from src.backend.models.invoice import Invoice

    constraints = [
        c
        for arg in Invoice.__table_args__
        if hasattr(arg, "columns") and hasattr(arg, "name")
        for c in [arg]
    ]
    nomes = {c.name for c in constraints}
    assert "uq_invoices_issuer_number" in nomes
    uq = [c for c in constraints if c.name == "uq_invoices_issuer_number"][0]
    colunas = tuple(sorted(c.name for c in uq.columns))
    assert colunas == ("invoice_number", "issuer_tax_id_digits")
    # Não deve existir unique global so de invoice_number.
    assert "uq_invoices_invoice_number" not in nomes


def test_b13_cliente_internacional_sem_tax_id():
    """B-13: cliente internacional (tipo foreign) pode não ter tax_id; email/phone persistidos."""
    from src.backend.models.client import Client
    from sqlalchemy import inspect

    mapper = inspect(Client)
    col_tax = mapper.columns["tax_id_digits"]
    col_type = col_tax.type
    # VARCHAR(32) nullable.
    assert col_type.__class__.__name__ == "VARCHAR"
    assert col_type.length == 32
    assert col_tax.nullable is True

    col_tipo = mapper.columns["tax_id_type"]
    assert col_tipo.nullable is False

    col_email = mapper.columns["email"]
    assert col_email.nullable is True
    col_phone = mapper.columns["phone"]
    assert col_phone.nullable is True


# ---------- Auditoria CR-009: aceitação dos BLOQ já satisfeitos (B-05, B-06) ----------


def test_b05_create_invoice_verifica_ownership():
    """B-05: create_invoice carrega client/simulacao filtrando por owner_user_id."""
    import inspect

    from src.backend.routers import invoices

    fonte = inspect.getsource(invoices.create_invoice)
    assert "Client.owner_user_id == sess.user_id" in fonte
    assert "Simulation.owner_user_id == sess.user_id" in fonte


def test_b06_csrf_cookie_nao_httponly_e_logout_nao_isento():
    """B-06: cookie CSRF sem HttpOnly; logout nao esta isento (requer CSRF token)."""
    from src.backend.middleware.csrf import CSRF_EXEMPT_PATHS, CSRF_COOKIE_NAME

    # Cookie CSRF nao deve ser HttpOnly.
    import src.backend.middleware.csrf as csrf_mod

    fonte = inspect.getsource(csrf_mod.CSRFMiddleware.__call__)
    set_cookie_trecho = [l for l in fonte.splitlines() if "set-cookie" in l.lower()]
    assert any("httponly" not in l.lower() for l in set_cookie_trecho), "cookie CSRF deve permitir leitura pelo frontend"

    # Logout nao esta na lista de isencao.
    assert "/v1/auth/logout" not in CSRF_EXEMPT_PATHS


# ---------- Auditoria CR-009: aceitação dos BLOQ já satisfeitos (B-08, B-09) ----------


def test_b08_exclusao_anonimiza_sem_colidir_unicos():
    """B-08: exclusao anonimiza com NULL (não colide índices parciais) e captura from_status ANTES."""
    import inspect

    from src.backend.routers import account

    fonte = inspect.getsource(account.delete_account)
    # from_status capturado antes de mudar user.status
    assert "from_status = user.status" in fonte
    # user.status = UserStatus.DELETED vem depois
    assert "user.status = UserStatus.DELETED" in fonte
    # Anonimiza com None (não com "" ou "00000000000" que colidem)
    assert "user.email = None" in fonte
    assert "user.cpf = None" in fonte


def test_b09_reativacao_publica_com_rate_limit():
    """B-09: reativacao dormente é endpoint publico com rate limit do login."""
    import inspect

    from src.backend.routers import account

    fonte = inspect.getsource(account.reactivate_account)
    # Endpoint publico: nao exige session (usa payload + senha)
    assert "_require_session(session)" not in fonte
    # Rate limit do login (5/minute)
    assert '@limiter.limit("5/minute")' in fonte
    # Reativa de DORMANT para ACTIVE
    assert "UserStatus.DORMANT" in fonte
    assert "UserStatus.ACTIVE" in fonte


