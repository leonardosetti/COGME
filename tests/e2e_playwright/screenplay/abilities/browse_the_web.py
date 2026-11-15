"""Habilidade ``BrowseTheWeb``: o ator navega por uma página Playwright."""

from __future__ import annotations

from playwright.async_api import Page


class BrowseTheWeb:
    """Habilidade que expõe a ``Page`` do Playwright ao ator.

    Attributes:
        page: Página do navegador sob controle do ator.
    """

    def __init__(self, page: Page) -> None:
        """Associa a habilidade a uma página do navegador.

        Args:
            page: Instância de ``Page`` do Playwright.
        """
        self.page = page
