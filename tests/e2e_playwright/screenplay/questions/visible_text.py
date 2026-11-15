"""Pergunta: texto visível de um elemento."""

from __future__ import annotations

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.questions.base import Question


class VisibleText(Question):
    """Devolve o texto visível do elemento no locator informado."""

    def __init__(self, locator: str) -> None:
        """Args:
            locator: Seletor CSS do elemento.
        """
        self.locator = locator

    def answered_by(self, actor: Actor) -> str:
        """Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.

        Returns:
            Texto visível do elemento.
        """
        page = actor.ability(BrowseTheWeb).page
        return page.locator(self.locator).text_content() or ""
