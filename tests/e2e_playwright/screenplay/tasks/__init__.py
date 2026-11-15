"""Tarefas dos atores (Screenplay Pattern)."""

from tests.e2e_playwright.screenplay.tasks.fill_invoice_form import FillInvoiceForm
from tests.e2e_playwright.screenplay.tasks.fill_simulation_form import FillSimulationForm
from tests.e2e_playwright.screenplay.tasks.generate_invoice import GenerateInvoice
from tests.e2e_playwright.screenplay.tasks.navigate_to import NavigateTo
from tests.e2e_playwright.screenplay.tasks.submit_simulation import SubmitSimulation

__all__ = [
    "FillInvoiceForm",
    "FillSimulationForm",
    "GenerateInvoice",
    "NavigateTo",
    "SubmitSimulation",
]
