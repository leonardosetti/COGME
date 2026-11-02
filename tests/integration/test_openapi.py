"""Documentação OpenAPI da API (spec backend-mvp-v1, §3; REQ-14).

O 422 do FastAPI não existe no contrato: a validação responde 400 ``validation_error``. A
documentação precisa refletir isso, com as quatro rotas e o modelo ``ErrorResponse``.
"""

from __future__ import annotations

from typing import Any

import pytest
from fastapi.testclient import TestClient

from src.backend.main import app

EXPECTED_PATHS = {"/v1/health", "/v1/rates/{currency}", "/v1/simulate", "/v1/invoice"}
ERROR_REF_SUFFIX = "/ErrorResponse"


@pytest.fixture
def schema() -> dict[str, Any]:
    """Documento OpenAPI gerado pela própria aplicação, sem subir o lifespan."""
    response = TestClient(app).get("/openapi.json")
    assert response.status_code == 200
    document: dict[str, Any] = response.json()
    return document


def _operations(schema: dict[str, Any]) -> list[tuple[str, str, dict[str, Any]]]:
    """Lista cada operação como (caminho, método, definição).

    Args:
        schema: Documento OpenAPI.

    Returns:
        Uma tupla por operação.
    """
    found: list[tuple[str, str, dict[str, Any]]] = []
    for path, item in schema["paths"].items():
        for method, operation in item.items():
            found.append((path, method, operation))
    return found


def test_openapi_document_is_served_req14(schema: dict[str, Any]) -> None:
    """REQ-14: /openapi.json responde com o título e a versão do contrato (§3)."""
    assert schema["info"]["title"] == "COGME API"
    assert schema["info"]["version"] == "1.0.0"


def test_exactly_the_four_v1_routes_are_documented_req14(schema: dict[str, Any]) -> None:
    """REQ-14: as quatro rotas de /v1 estão documentadas, nem uma a mais (§3)."""
    assert set(schema["paths"]) == EXPECTED_PATHS


def test_no_operation_declares_422_req14(schema: dict[str, Any]) -> None:
    """REQ-14: nenhuma operação documenta 422; a validação é 400 (§3)."""
    for path, method, operation in _operations(schema):
        assert "422" not in operation.get("responses", {}), f"{method} {path} ainda tem 422"


def test_fastapi_validation_schemas_are_removed_req14(schema: dict[str, Any]) -> None:
    """REQ-14: os schemas HTTPValidationError e ValidationError do FastAPI não aparecem."""
    components = schema["components"]["schemas"]
    assert "HTTPValidationError" not in components
    assert "ValidationError" not in components


def test_error_response_is_documented_and_shared_req14(schema: dict[str, Any]) -> None:
    """REQ-14: ErrorResponse existe em components e é a resposta de 400 e 503 de simulação."""
    components = schema["components"]["schemas"]
    assert "ErrorResponse" in components
    simulate = schema["paths"]["/v1/simulate"]["post"]["responses"]
    for status in ("400", "500", "503"):
        content = simulate[status]["content"]["application/json"]["schema"]
        assert content["$ref"].endswith(ERROR_REF_SUFFIX), status


def test_error_responses_declare_their_keys_req14(schema: dict[str, Any]) -> None:
    """REQ-14: 400, 500 e 503 têm descrição com a chave canônica de cada erro (§3)."""
    rates = schema["paths"]["/v1/rates/{currency}"]["get"]["responses"]
    assert "validation_error" in rates["400"]["description"]
    assert "internal_error" in rates["500"]["description"]
    assert "rates_unavailable" in rates["503"]["description"]


def test_invoice_declares_pdf_success_and_pdf_unavailable_req14(
    schema: dict[str, Any],
) -> None:
    """REQ-14: a invoice documenta o PDF como resposta de sucesso e pdf_unavailable como 503."""
    invoice = schema["paths"]["/v1/invoice"]["post"]["responses"]
    assert "application/pdf" in invoice["200"]["content"]
    assert "pdf_unavailable" in invoice["503"]["description"]


def test_health_documents_no_error_responses_req14(schema: dict[str, Any]) -> None:
    """REQ-14: /v1/health não tem erros de domínio; só o 200 é documentado."""
    health = schema["paths"]["/v1/health"]["get"]["responses"]
    assert set(health) == {"200"}


def test_docs_page_is_served_req14() -> None:
    """REQ-14: /docs responde 200 com a página Swagger UI."""
    response = TestClient(app).get("/docs")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "swagger" in response.text.lower()
