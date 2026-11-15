"""Tarefa: submeter o formulário de simulação."""

from __future__ import annotations

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.tasks.base import Task


class SubmitSimulation(Task):
    """Submete o formulário de simulação e aguarda o resultado."""

    def perform_as(self, actor: Actor) -> None:
        """Clica em simular e aguarda o card de resultado aparecer.

        Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.
        """
        page = actor.ability(BrowseTheWeb).page
        page.click("#btn")
        page.wait_for_selector("#result.visible", state="visible", timeout=10000)
