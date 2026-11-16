"""Testes funcionais de simulação — CT-FUNC-001 / CT-FUNC-002.

Fluxo: usuário abre a tela de simulação, preenche o formulário por um regime,
submete e verifica o resultado renderizado pelo front (recálculo no back via /v1/simulate).

As asserções são estruturais (formato pt-BR) porque a cotação do back varia com o
provedor real; o valor exato é validado nos testes de contrato (tests/integration).
"""

from __future__ import annotations

import re

import pytest
from playwright.async_api import Page

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import actor_named
from tests.e2e_playwright.screenplay.tasks.fill_simulation_form import FillSimulationForm
from tests.e2e_playwright.screenplay.tasks.navigate_to import NavigateTo
from tests.e2e_playwright.screenplay.tasks.submit_simulation import SubmitSimulation
from tests.e2e_playwright.screenplay.questions.visible_text import VisibleText

SIMULATION_URL_PATH = "/"

MONEY_BR = re.compile(r"^R\$ \d{1,3}(\.\d{3})*,\d{2}$")

REGIMES = [
    ("hourly", "30", "160"),
    ("daily", "100", "5"),
    ("weekly", "250", "4"),
    ("monthly", "1000", "12"),
    ("fixed", "1000", None),
]


async def _simulate(
    page: Page, base_url: str, regime: str, amount: str, quantity: str | None
) -> str:
    """Executa uma simulação completa e devolve o texto do líquido (net_brl)."""
    actor = actor_named("usuario")
    actor.add_ability(BrowseTheWeb(page))
    await actor.perform(NavigateTo(base_url + SIMULATION_URL_PATH))
    await actor.perform(
        FillSimulationForm(
            currency="USD",
            regime=regime,
            amount=amount,
            quantity=quantity,
            spread_pct="2",
            iof_pct="0.38",
        )
    )
    await actor.perform(SubmitSimulation())
    return await actor.ask(VisibleText("#r-net-brl"))


@pytest.mark.functional
@pytest.mark.playwright
@pytest.mark.parametrize(
    ("regime", "amount", "quantity"),
    REGIMES,
    ids=[r[0] for r in REGIMES],
)
async def test_simulacao_por_regime_exibe_liquido_formatado(
    page: Page, base_url: str, regime: str, amount: str, quantity: str | None,
) -> None:
    """CT-FUNC-001: cada um dos 5 regimes exibe o líquido formatado em pt-BR."""
    net = await _simulate(page, base_url, regime, amount, quantity)
    assert MONEY_BR.match(net.strip()), f"{regime}: {net!r}"


@pytest.mark.functional
@pytest.mark.playwright
async def test_simulacao_usd_horario_exibe_resultado_detalhado(page: Page, base_url: str) -> None:
    """CT-FUNC-002: simulação USD hourly exibe bruto, spread, IOF, líquido e cotação."""
    actor = actor_named("usuario")
    actor.add_ability(BrowseTheWeb(page))
    await actor.perform(NavigateTo(base_url + SIMULATION_URL_PATH))
    await actor.perform(
        FillSimulationForm(currency="USD", regime="hourly", amount="30", quantity="160",
                           spread_pct="2", iof_pct="0.38")
    )
    await actor.perform(SubmitSimulation())

    assert (await actor.ask(VisibleText("#r-gross-foreign"))).strip().endswith("USD")
    assert MONEY_BR.match((await actor.ask(VisibleText("#r-gross-brl"))).strip())
    assert "R$" in (await actor.ask(VisibleText("#r-spread-brl")))
    assert "R$" in (await actor.ask(VisibleText("#r-iof-brl")))
    assert MONEY_BR.match((await actor.ask(VisibleText("#r-net-brl"))).strip())
    quote_rate = (await actor.ask(VisibleText("#r-quote-rate"))).strip()
    assert "BRL/USD" in quote_rate
    assert (await actor.ask(VisibleText("#r-source"))).strip().lower() in ("frankfurter", "ptax")
