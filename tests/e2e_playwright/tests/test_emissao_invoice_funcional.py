"""Testes funcionais de emissão de invoice — CT-FUNC-003.

Fluxo: usuário abre a tela de emissão de invoice, preenche simulação + partes +
documento, gera o PDF e verifica o download (assinatura %PDF-).

Todos os dados são sintéticos (P-04, constitution.md:90).
"""

from __future__ import annotations

import pytest
from playwright.async_api import Page

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import actor_named
from tests.e2e_playwright.screenplay.tasks.fill_invoice_form import FillInvoiceForm
from tests.e2e_playwright.screenplay.tasks.generate_invoice import GenerateInvoice
from tests.e2e_playwright.screenplay.tasks.navigate_to import NavigateTo

INVOICE_URL_PATH = "/invoice"


@pytest.mark.functional
@pytest.mark.playwright
async def test_emissao_invoice_gera_pdf_para_download(page: Page, base_url: str) -> None:
    """CT-FUNC-003: emissão de invoice produz download de PDF válido (%PDF-).

    A validação da assinatura %PDF- ocorre dentro de ``GenerateInvoice``; este
    teste apenas executa o fluxo completo e confirma que não há exceção.
    """
    actor = actor_named("usuario")
    actor.add_ability(BrowseTheWeb(page))
    await actor.perform(NavigateTo(base_url + INVOICE_URL_PATH))
    await actor.perform(
        FillInvoiceForm(
            sim_currency="USD",
            sim_regime="hourly",
            sim_amount="30",
            sim_quantity="160",
            sim_spread_pct="2",
            sim_iof_pct="0.38",
            issuer_name="Pessoa Fictícia da Silva",
            issuer_tax_id="000.000.000-00",
            issuer_address="Rua Exemplo, 123, Cidade Fictícia",
            client_name="Example Fictional LLC",
            invoice_number="INV-E2E-0001",
            issue_date="2026-01-15",
            description="Serviços fictícios de desenvolvimento de software.",
        )
    )
    await actor.perform(GenerateInvoice())
