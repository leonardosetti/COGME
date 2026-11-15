"""Pergunta: se um elemento está presente/visível."""

from __future__ import annotations

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.questions.base import Question


class ElementPresent(Question):
    """Responde se o elemento no locator está visível na página."""

    def __init__(self, locator: str) -> None:
        """Args:
            locator: Seletor CSS do elemento.
        """
        self.locator = locator

    def answered_by(self, actor: Actor) -> bool:
        """Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.

        Returns:
            Verdadeiro se o elemento estiver visível.
        """
        page = actor.ability(BrowseTheWeb).page
        return page.locator(self.locator).is_visible()
