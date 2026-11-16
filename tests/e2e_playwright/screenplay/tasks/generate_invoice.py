"""Tarefa: gerar a invoice em PDF."""

from __future__ import annotations

from typing import Final

from tests.e2e_playwright.screenplay.abilities.browse_the_web import BrowseTheWeb
from tests.e2e_playwright.screenplay.actor import Actor
from tests.e2e_playwright.screenplay.tasks.base import Task

PDF_SIGNATURE: Final[bytes] = b"%PDF-"


class GenerateInvoice(Task):
    """Gera a invoice e captura o PDF baixado pelo navegador."""

    def __init__(self) -> None:
        self.pdf_bytes: bytes | None = None

    async def perform_as(self, actor: Actor) -> None:
        """Clica em gerar invoice e aguarda o download do PDF.

        Args:
            actor: Ator com a habilidade ``BrowseTheWeb``.

        Raises:
            AssertionError: Se nenhum PDF for baixado ou o conteúdo não for PDF.
        """
        page = actor.ability(BrowseTheWeb).page

        download_promise = page.wait_for_event("download", timeout=15000)
        await page.click("#btn")
        download = await download_promise

        path = await download.path()
        assert path is not None, "download do PDF não gerou caminho de arquivo"
        self.pdf_bytes = path.read_bytes()
        assert self.pdf_bytes.startswith(PDF_SIGNATURE), "baixado não é um PDF válido"
