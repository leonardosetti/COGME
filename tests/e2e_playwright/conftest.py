"""Fixtures dos testes Playwright (Screenplay Pattern).

O alvo é o front publicado pelo docker compose (porta 8001 no host, serviço
``front`` mapeando 8000). Defina ``COGME_BASE_URL`` para apontar a outro stack
(ex.: ``http://localhost:8080`` via proxy). Todos os dados são sintéticos.
"""

from __future__ import annotations

import os
from typing import Final

import pytest
from playwright.async_api import async_playwright

from tests.e2e_playwright.screenplay.actor import Actor, stage

BASE_URL: Final[str] = os.environ.get("COGME_BASE_URL", "http://localhost:8001")


@pytest.fixture(scope="function")
async def browser():
    """Navegador Chromium lançado por teste (evita ScopeMismatch com pytest-asyncio)."""
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        yield browser
        await browser.close()


@pytest.fixture
async def page(browser):
    """Página nova por teste; fecha ao fim."""
    page = await browser.new_page()
    yield page
    await page.close()


@pytest.fixture
def base_url() -> str:
    """URL base do front sob teste."""
    return BASE_URL


@pytest.fixture
def actor(page) -> Actor:
    """Ator com a habilidade de navegar pela página informada."""
    from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb

    a = Actor("usuario")
    a.add_ability(BrowseTheWeb(page))
    stage.cast(a)
    return a
