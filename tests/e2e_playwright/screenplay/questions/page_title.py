"""Pergunta: título da página."""

from __future__ import annotations

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.questions.base import Question


class PageTitle(Question):
    """Devolve o título da página atual."""

    def answered_by(self, actor: Actor) -> str:
        """Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.

        Returns:
            Título da página.
        """
        page = actor.ability(BrowseTheWeb).page
        return page.title()
