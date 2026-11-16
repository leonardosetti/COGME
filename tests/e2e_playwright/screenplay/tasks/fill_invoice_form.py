"""Tarefa: preencher o formulário de emissão de invoice (tela ``/invoice``)."""

from __future__ import annotations

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.tasks.base import Task


class FillInvoiceForm(Task):
    """Preenche simulação, partes e dados do documento da invoice."""

    def __init__(
        self,
        *,
        sim_currency: str = "USD",
        sim_regime: str = "hourly",
        sim_amount: str = "30",
        sim_quantity: str = "160",
        sim_spread_pct: str = "2",
        sim_iof_pct: str = "0.38",
        issuer_name: str = "Pessoa Fictícia da Silva",
        issuer_tax_id: str = "000.000.000-00",
        issuer_address: str = "Rua Exemplo, 123, Cidade Fictícia",
        client_name: str = "Example Fictional LLC",
        client_tax_id: str | None = None,
        client_address: str | None = None,
        invoice_number: str = "INV-E2E-0001",
        issue_date: str = "2026-01-15",
        description: str = "Serviços fictícios de desenvolvimento de software.",
    ) -> None:
        """Args:
            sim_*: Campos da simulação embarcada no formulário de invoice.
            issuer_*: Dados do emitente (nome obrigatório).
            client_*: Dados do cliente (nome obrigatório).
            invoice_number: Número da invoice.
            issue_date: Data de emissão (AAAA-MM-DD).
            description: Descrição do serviço.
        """
        self.sim_currency = sim_currency
        self.sim_regime = sim_regime
        self.sim_amount = sim_amount
        self.sim_quantity = sim_quantity
        self.sim_spread_pct = sim_spread_pct
        self.sim_iof_pct = sim_iof_pct
        self.issuer_name = issuer_name
        self.issuer_tax_id = issuer_tax_id
        self.issuer_address = issuer_address
        self.client_name = client_name
        self.client_tax_id = client_tax_id
        self.client_address = client_address
        self.invoice_number = invoice_number
        self.issue_date = issue_date
        self.description = description

    async def perform_as(self, actor: Actor) -> None:
        """Preenche todos os campos do formulário de invoice.

        Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.
        """
        page = actor.ability(BrowseTheWeb).page
        await page.select_option("#sim-currency", self.sim_currency)
        await page.select_option("#sim-regime", self.sim_regime)
        await page.fill("#sim-amount", self.sim_amount)
        await page.fill("#sim-quantity", self.sim_quantity)
        await page.fill("#sim-spread_pct", self.sim_spread_pct)
        await page.fill("#sim-iof_pct", self.sim_iof_pct)
        await page.fill("#issuer-name", self.issuer_name)
        if self.issuer_tax_id is not None:
            await page.fill("#issuer-tax_id", self.issuer_tax_id)
        if self.issuer_address is not None:
            await page.fill("#issuer-address", self.issuer_address)
        await page.fill("#client-name", self.client_name)
        if self.client_tax_id is not None:
            await page.fill("#client-tax_id", self.client_tax_id)
        if self.client_address is not None:
            await page.fill("#client-address", self.client_address)
        await page.fill("#invoice_number", self.invoice_number)
        await page.fill("#issue_date", self.issue_date)
        await page.fill("#description", self.description)
