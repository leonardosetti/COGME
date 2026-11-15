"""Tarefa: preencher o formulário de simulação (tela ``/``)."""

from __future__ import annotations

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.tasks.base import Task


class FillSimulationForm(Task):
    """Preenche os campos do formulário de simulação de recebimento."""

    def __init__(
        self,
        *,
        currency: str = "USD",
        regime: str = "hourly",
        amount: str = "30",
        quantity: str | None = "160",
        spread_pct: str = "2",
        iof_pct: str = "0.38",
    ) -> None:
        """Args:
            currency: Moeda estrangeira (``USD``/``EUR``).
            regime: Regime de contratação (``hourly``/``daily``/``weekly``/``monthly``/``fixed``).
            amount: Valor por unidade.
            quantity: Quantidade de unidades (``None`` no regime ``fixed``).
            spread_pct: Spread em %.
            iof_pct: IOF em %.
        """
        self.currency = currency
        self.regime = regime
        self.amount = amount
        self.quantity = quantity
        self.spread_pct = spread_pct
        self.iof_pct = iof_pct

    def perform_as(self, actor: Actor) -> None:
        """Preenche o formulário e submete.

        Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.
        """
        page = actor.ability(BrowseTheWeb).page
        page.select_option("#currency", self.currency)
        page.select_option("#regime", self.regime)
        page.fill("#amount", self.amount)
        if self.quantity is not None:
            page.fill("#quantity", self.quantity)
        page.fill("#spread_pct", self.spread_pct)
        page.fill("#iof_pct", self.iof_pct)
