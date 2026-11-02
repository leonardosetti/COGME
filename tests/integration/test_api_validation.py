"""Erros de validação e de corpo em /v1 (spec backend-mvp-v1, §3 e §8.1; REQ-02, REQ-03).

Toda falha de entrada sai como 400 ``validation_error`` no modelo canônico. ``details`` traz o
campo e uma mensagem PT-BR, e nunca ecoa o valor enviado nem o nome de chave extra. Corpos são
enviados como bytes crus quando o literal importa: ``json=`` passaria por ``float``.
"""

from __future__ import annotations

from typing import Any

import pytest
from fastapi.testclient import TestClient

from .fakes import SIMULATE, SPEC_EXAMPLE_BODY, error_of

JSON_HEADERS = {"content-type": "application/json"}
LONG_LITERAL = "30.1000000000000000000001"
EXTRA_KEY = "chave_extra_sintetica"
BAD_ENUM_VALUE = "XYZ"
BODY_TOO_LARGE_MESSAGE = "O corpo da requisição excede o limite de 64 KiB."
VALIDATION_MESSAGE = "Dados inválidos."


def _without(body: dict[str, Any], *keys: str) -> dict[str, Any]:
    """Devolve uma cópia do corpo sem as chaves informadas.

    Args:
        body: Corpo de referência.
        *keys: Chaves a retirar.

    Returns:
        O corpo reduzido.
    """
    return {key: value for key, value in body.items() if key not in keys}


@pytest.mark.parametrize(
    ("body", "details"),
    [
        (
            _without(SPEC_EXAMPLE_BODY, "amount"),
            [{"field": "amount", "message": "Campo obrigatório."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "amount": "0"},
            [{"field": "amount", "message": "O valor deve ser maior que 0."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "amount": "1000000001"},
            [{"field": "amount", "message": "O valor deve ser menor ou igual a 1000000000."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "amount": "10.001"},
            [{"field": "amount", "message": "Número de casas decimais acima do permitido."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "spread_pct": "101"},
            [{"field": "spread_pct", "message": "O valor deve ser menor ou igual a 100."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "spread_pct": "1.00001"},
            [{"field": "spread_pct", "message": "Número de casas decimais acima do permitido."}],
        ),
        (
            _without(SPEC_EXAMPLE_BODY, "quantity"),
            [{"field": "quantity", "message": "Informe a quantidade para este regime."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "regime": "fixed"},
            [{"field": "quantity", "message": "A quantidade não é permitida no regime fixed."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "amount": "0.01", "quantity": "0.01"},
            [{
                "field": "quantity",
                "message": "O valor bruto resultante deve ser de pelo menos 0.01.",
            }],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "currency": BAD_ENUM_VALUE},
            [{"field": "currency", "message": "Valor não permitido para este campo."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, "regime": "yearly"},
            [{"field": "regime", "message": "Valor não permitido para este campo."}],
        ),
        (
            {**SPEC_EXAMPLE_BODY, EXTRA_KEY: "qualquer"},
            [{"field": "body", "message": "Campo não permitido."}],
        ),
    ],
    ids=[
        "falta_amount", "amount_zero", "amount_acima_do_teto", "amount_casas_demais",
        "spread_acima_de_100", "spread_5_casas", "quantity_faltando", "quantity_em_fixed",
        "bruto_arredonda_para_zero", "moeda_fora_do_enum", "regime_fora_do_enum",
        "campo_extra",
    ],
)
def test_invalid_simulation_body_is_400_validation_error_req02(
    client: TestClient, body: dict[str, Any], details: list[dict[str, str]],
) -> None:
    """REQ-02/REQ-03: entrada inválida responde 400 com detalhe por campo, sem eco do valor."""
    response = client.post(SIMULATE, json=body)
    error = error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert error["details"] == details
    # Nenhum valor enviado (texto ruim ou nome de chave extra) pode voltar na resposta.
    assert BAD_ENUM_VALUE not in response.text
    assert EXTRA_KEY not in response.text


def test_extra_key_name_is_never_echoed_req02(client: TestClient) -> None:
    """Campo extra: o nome da chave enviada não aparece na resposta (§8.1)."""
    body = {**SPEC_EXAMPLE_BODY, EXTRA_KEY: "valor"}
    response = client.post(SIMULATE, json=body)
    error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert EXTRA_KEY not in response.text


def test_invalid_path_enum_is_400_req01(client: TestClient) -> None:
    """REQ-01: moeda inválida no caminho responde 400, não 422 do FastAPI (§3)."""
    response = client.get("/v1/rates/BRL")
    error = error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert error["details"] == [
        {"field": "path.currency", "message": "Valor não permitido para este campo."},
    ]


def test_malformed_json_is_400_json_invalid(client: TestClient) -> None:
    """JSON malformado responde 400 e não repete o texto do corpo (§8.1)."""
    raw = b'{"currency": "USD", "regime": "hourly",'
    response = client.post(SIMULATE, content=raw, headers=JSON_HEADERS)
    error = error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert error["details"] == [{"field": "body", "message": "JSON inválido."}]
    assert "hourly" not in response.text


@pytest.mark.parametrize("constant", ["NaN", "Infinity", "-Infinity"])
def test_nan_and_infinity_literals_are_rejected_req02(client: TestClient, constant: str) -> None:
    """NaN e Infinity no JSON viram JSON inválido; o contrato nunca aceita não finitos (§8.1)."""
    raw = (
        '{"currency":"USD","regime":"fixed","amount":%s,"spread_pct":"2","iof_pct":"0.38"}'
        % constant
    ).encode()
    response = client.post(SIMULATE, content=raw, headers=JSON_HEADERS)
    error = error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert error["details"] == [{"field": "body", "message": "JSON inválido."}]


def test_long_decimal_literal_is_refused_not_rounded_req02(client: TestClient) -> None:
    """Literal de 22 casas: 400 por excesso de casas, sem arredondar para float (§8.1).

    O corpo vai como bytes crus. Com ``json=`` o literal viraria ``float`` antes do envio.
    """
    raw = (
        '{"currency":"USD","regime":"hourly","amount":%s,"quantity":"160",'
        '"spread_pct":"2","iof_pct":"0.38"}' % LONG_LITERAL
    ).encode()
    response = client.post(SIMULATE, content=raw, headers=JSON_HEADERS)
    error = error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert error["details"] == [
        {"field": "amount", "message": "Número de casas decimais acima do permitido."},
    ]
    assert LONG_LITERAL not in response.text


def test_body_over_64_kib_with_content_length_is_400_req02(client: TestClient) -> None:
    """Corpo acima de 64 KiB, com Content-Length, responde 400 antes de ser lido (§8.1)."""
    oversized = b'{"currency":"USD","padding":"' + b"a" * 70_000 + b'"}'
    response = client.post(SIMULATE, content=oversized, headers=JSON_HEADERS)
    error = error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert error["details"] == [{"field": "body", "message": BODY_TOO_LARGE_MESSAGE}]


def test_body_over_64_kib_without_content_length_is_400_req02(client: TestClient) -> None:
    """Corpo em pedaços, sem Content-Length, que passa de 64 KiB é cortado durante a leitura."""
    chunks = [b'{"currency":"USD","padding":"' + b"a" * 40_000, b"a" * 40_000 + b'"}']
    response = client.post(SIMULATE, content=iter(chunks), headers=JSON_HEADERS)
    error = error_of(response, 400, "validation_error", VALIDATION_MESSAGE)
    assert error["details"] == [{"field": "body", "message": BODY_TOO_LARGE_MESSAGE}]
