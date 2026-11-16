"""Testes de unidade para rotas de invoice draft/PUT/download (SPEC-020, SPEC-021)."""

from __future__ import annotations

from datetime import date, datetime, UTC
from decimal import Decimal

import pytest
from fastapi import HTTPException

from src.backend.models.invoice_repository import StoredInvoice
from src.backend.routers.invoices import (
    create_invoice,
    download_invoice_pdf,
    update_invoice,
)
from src.backend.middleware.session import SessionData


def _make_stored_invoice(**overrides) -> StoredInvoice:
    base = dict(
        id=1,
        owner_user_id=1,
        client_id=None,
        simulation_id=None,
        invoice_number="INV-202601-0001",
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


class _FakeRepo:
    """Repositório falso com suporte a save/get_by_number/get_next_number."""

    def __init__(self, invoices: list | None = None) -> None:
        self.invoices = list(invoices or [])
        self.deleted: list[tuple[int, int]] = []
        self.saved: list[StoredInvoice] = []
        self.next_number = "INV-202601-0002"

    def _find(self, invoice_id: int, owner_user_id: int):
        for invoice in self.invoices:
            if invoice.id == invoice_id and invoice.owner_user_id == owner_user_id:
                return invoice
        return None

    async def get_by_id(self, invoice_id: int, owner_user_id: int):
        return self._find(invoice_id, owner_user_id)

    async def get_by_number(self, invoice_number: str, owner_user_id: int):
        for invoice in self.invoices:
            if invoice.invoice_number == invoice_number and invoice.owner_user_id == owner_user_id:
                return invoice
        return None

    async def get_next_number(self, issuer_tax_id_digits: str) -> str:
        return self.next_number

    async def save(self, invoice: StoredInvoice) -> None:
        self.saved.append(invoice)
        self.invoices.append(invoice)

    async def update_status(self, invoice_id, owner_user_id, status, when=None):
        inv = self._find(invoice_id, owner_user_id)
        if inv is None:
            return None
        from dataclasses import replace

        atualizada = replace(inv, status=status, updated_at=when)
        self.invoices[self.invoices.index(inv)] = atualizada
        return atualizada

    async def delete(self, invoice_id: int, owner_user_id: int) -> bool:
        inv = self._find(invoice_id, owner_user_id)
        if inv is None:
            return False
        self.invoices.remove(inv)
        self.deleted.append((invoice_id, owner_user_id))
        return True

    async def list_by_owner(self, owner_user_id, *, status=None, client_id=None, page=1, page_size=20):
        rows = [inv for inv in self.invoices if inv.owner_user_id == owner_user_id]
        if status is not None:
            rows = [inv for inv in rows if inv.status == status]
        return rows, len(rows)

    async def clone(self, invoice_id: int, owner_user_id: int):
        original = self._find(invoice_id, owner_user_id)
        if original is None:
            raise ValueError("not found")
        return original


def _payload(**overrides) -> dict:
    base = dict(
        client_id=None,
        client_fictitious={
            "name": "Cliente Fictício",
            "tax_id": "00000000000001",
            "address": "Rua X, 1",
            "country_code": "BR",
        },
        simulation_id=None,
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
    )
    base.update(overrides)
    return base


class _FakeRateService:
    async def get_quote(self, currency):
        class Q:
            rate = Decimal("5.12")
            source = "frankfurter"
            quoted_at = datetime(2026, 1, 31, 12, 0, 0, tzinfo=UTC)
            bulletin = None
            stale = False

        return Q()


def _run(coro):
    import asyncio

    return asyncio.run(coro)
    from src.backend.schemas.invoice import InvoiceCreateDraft

    repo = _FakeRepo()
    payload = InvoiceCreateDraft(**_payload())
    resposta = _run(create_invoice(payload, SessionData(1, 1), repo))
    assert resposta.status == "draft"
    assert resposta.invoice_number == "INV-202601-0002"
    assert len(repo.saved) == 1


def test_create_invoice_sem_cliente_falha():
    from src.backend.schemas.invoice import InvoiceCreateDraft

    repo = _FakeRepo()
    payload = InvoiceCreateDraft(**_payload(client_id=None, client_fictitious=None))
    with pytest.raises(HTTPException) as erro:
        _run(create_invoice(payload, SessionData(1, 1), repo))
    assert erro.value.status_code == 400


def test_update_invoice_draft_sucesso():
    from src.backend.schemas.invoice import InvoiceUpdate

    rascunho = _make_stored_invoice(id=1, status="draft")
    repo = _FakeRepo([rascunho])
    payload = InvoiceUpdate(description="Desc atualizada")
    resposta = _run(update_invoice(1, payload, SessionData(1, 1), repo))
    assert resposta.description == "Desc atualizada"


def test_update_invoice_finalized_nao_permitido():
    from src.backend.schemas.invoice import InvoiceUpdate

    finalizada = _make_stored_invoice(id=1, status="finalized")
    repo = _FakeRepo([finalizada])
    payload = InvoiceUpdate(description="X")
    with pytest.raises(HTTPException) as erro:
        _run(update_invoice(1, payload, SessionData(1, 1), repo))
    assert erro.value.status_code == 409


def test_update_invoice_nao_encontrado():
    from src.backend.schemas.invoice import InvoiceUpdate

    repo = _FakeRepo()
    payload = InvoiceUpdate(description="X")
    with pytest.raises(HTTPException) as erro:
        _run(update_invoice(99, payload, SessionData(1, 1), repo))
    assert erro.value.status_code == 404


def test_download_invoice_pdf_sucesso(monkeypatch):
    from src.backend.routers import invoices

    finalizada = _make_stored_invoice(id=7, status="finalized")
    repo = _FakeRepo([finalizada])

    async def _pdf_falso(stored, rate_service):
        return b"%PDF-1.4 falso"

    monkeypatch.setattr(invoices, "render_pdf_from_stored", _pdf_falso)
    resposta = _run(download_invoice_pdf(7, SessionData(1, 1), _FakeRateService(), repo))
    assert resposta.status_code == 200
    assert resposta.body == b"%PDF-1.4 falso"


def test_download_invoice_pdf_nao_encontrado():
    repo = _FakeRepo()
    with pytest.raises(HTTPException) as erro:
        _run(download_invoice_pdf(99, SessionData(1, 1), _FakeRateService(), repo))
    assert erro.value.status_code == 404
