"""Tarefa: navegar até uma URL."""

from __future__ import annotations

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.tasks.base import Task


class NavigateTo(Task):
    """Navega o navegador até a URL informada."""

    def __init__(self, url: str) -> None:
        """Args:
            url: URL de destino (ex.: ``http://localhost:8001/``).
        """
        self.url = url

    def perform_as(self, actor: Actor) -> None:
        """Leva o ator à URL, aguardando estabilização da rede.

        Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.
        """
        page = actor.ability(BrowseTheWeb).page
        page.goto(self.url, wait_until="networkidle")
