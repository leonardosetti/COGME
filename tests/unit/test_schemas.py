"""Contrato HTTP de src/shared/schemas.py (spec backend-mvp-v1, §2, §3 e §8.1).

Dados sintéticos; só o schema, sem serviços nem rede. A §3 não tem IDs REQ próprios.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta
from decimal import Decimal
from typing import Any

import pytest
from pydantic import ValidationError

from src.backend.errors import PdfUnavailableError, RatesUnavailableError
from src.shared.schemas import (
    NOTICE,
    ErrorKey,
    RateQuote,
    SimulationRequest,
    SimulationResponse,
)

BASE: dict[str, Any] = {
    "currency": "USD",
    "regime": "hourly",
    "amount": "30.00",
    "quantity": "160",
    "spread_pct": "2",
    "iof_pct": "0.38",
}
QUOTE: dict[str, Any] = {
    "currency": "USD",
    "rate": "5.000000",
    "source": "frankfurter",
    "quoted_at": "2026-10-30T00:00:00Z",
    "bulletin": None,
    "stale": False,
}
RESPONSE: dict[str, Any] = {
    "currency": "USD",
    "regime": "hourly",
    "gross_foreign": "4800.00",
    "gross_brl": "24000.00",
    "spread_brl": "480.00",
    "iof_brl": "89.38",
    "net_brl": "23430.62",
    "effective_rate": "4.881379",
    "spread_pct": "2",
    "iof_pct": "0.38",
    "quote": QUOTE,
    "notice": NOTICE,
}


def _request(**changes: Any) -> dict[str, Any]:
    """Monta uma requisição válida; valor ``None`` remove a chave."""
    data = {**BASE, **changes}
    return {key: value for key, value in data.items() if value is not None}


def _rejects(model: type, data: dict[str, Any], loc: tuple[Any, ...], error_type: str) -> None:
    """Garante que o schema recusa o corpo com o erro esperado (sem ler a entrada)."""
    with pytest.raises(ValidationError) as info:
        model.model_validate(data)
    found = {(tuple(e["loc"]), e["type"]) for e in info.value.errors(include_input=False)}
    assert (loc, error_type) in found, f"esperado {error_type} em {loc}"


@pytest.mark.parametrize(
    ("regime", "quantity"),
    [("hourly", "160"), ("daily", "8"), ("weekly", "5"), ("monthly", "1"), ("fixed", None)],
)
def test_valid_request_for_each_regime(regime: str, quantity: str | None) -> None:
    """Valores válidos em todos os regimes; quantity só é exigida nos períodos (§2)."""
    parsed = SimulationRequest.model_validate(_request(regime=regime, quantity=quantity))
    assert parsed.regime == regime
    assert (parsed.quantity is None) == (quantity is None)


def test_valid_response_matches_spec_example_and_dumps_strings() -> None:
    """Resposta da §2 é aceita; decimais saem como texto no JSON (§3)."""
    parsed = SimulationResponse.model_validate(RESPONSE)
    assert parsed.notice == NOTICE
    dumped = parsed.model_dump(mode="json")
    for key in ("gross_foreign", "gross_brl", "spread_brl", "iof_brl", "net_brl"):
        assert isinstance(dumped[key], str), key
    assert dumped["effective_rate"] == "4.881379"
    assert dumped["spread_pct"] == "2.0000"
    assert isinstance(dumped["quote"]["rate"], str)


def test_decimal_text_from_json_numbers_floats_and_canonical_scale() -> None:
    """Número JSON chega com parse_float=Decimal (§8.1); float vira repr; escala canônica."""
    body = (
        '{"currency":"USD","regime":"hourly","amount":30.10,'
        '"quantity":160,"spread_pct":0.1,"iof_pct":"0.38"}'
    )
    parsed = SimulationRequest.model_validate(json.loads(body, parse_float=Decimal))
    assert parsed.amount == Decimal("30.10")
    assert parsed.spread_pct == Decimal("0.1000")
    assert str(SimulationRequest.model_validate(_request(amount="30.000")).amount) == "30.00"
    spread = SimulationRequest.model_validate(_request(spread_pct=0.1)).spread_pct
    assert spread == Decimal("0.1000")


def test_negative_zero_becomes_plain_zero() -> None:
    """``-0`` vira zero sem sinal, para não haver zero negativo na resposta."""
    parsed = SimulationRequest.model_validate(_request(spread_pct="-0"))
    assert parsed.spread_pct == Decimal("0.0000")
    assert not parsed.spread_pct.is_signed()


@pytest.mark.parametrize(
    ("amount", "error_type"),
    [
        ("0.01", None), ("1000000000", None), ("1000000000.00", None),
        ("0", "decimal_too_low"), ("0.00", "decimal_too_low"), ("-1", "decimal_too_low"),
        ("1000000000.01", "decimal_too_high"), ("10.001", "decimal_max_places"),
    ],
)
def test_amount_exact_limits(amount: str, error_type: str | None) -> None:
    """amount: maior que 0, até 1.000.000.000, no máximo 2 casas (§3)."""
    if error_type is None:
        SimulationRequest.model_validate(_request(amount=amount))
    else:
        _rejects(SimulationRequest, _request(amount=amount), ("amount",), error_type)


@pytest.mark.parametrize(
    ("quantity", "error_type"),
    [
        ("0.01", None), ("100000", None), ("100000.00", None),
        ("0", "decimal_too_low"), ("100000.01", "decimal_too_high"),
        ("1.001", "decimal_max_places"),
    ],
)
def test_quantity_exact_limits(quantity: str, error_type: str | None) -> None:
    """quantity: maior que 0, até 100.000, no máximo 2 casas (§3)."""
    if error_type is None:
        SimulationRequest.model_validate(_request(quantity=quantity))
    else:
        _rejects(SimulationRequest, _request(quantity=quantity), ("quantity",), error_type)


@pytest.mark.parametrize("field", ["spread_pct", "iof_pct"])
@pytest.mark.parametrize(
    ("value", "error_type"),
    [
        ("0", None), ("100", None), ("99.9999", None),
        ("100.0001", "decimal_too_high"), ("-0.0001", "decimal_too_low"),
        ("0.00001", "decimal_max_places"),
    ],
)
def test_percent_exact_limits(field: str, value: str, error_type: str | None) -> None:
    """Percentuais: de 0 a 100 com no máximo 4 casas (§3)."""
    if error_type is None:
        SimulationRequest.model_validate(_request(**{field: value}))
    else:
        _rejects(SimulationRequest, _request(**{field: value}), (field,), error_type)


def test_fixed_with_quantity_is_refused() -> None:
    """Regime fixed proíbe quantity (§2)."""
    _rejects(SimulationRequest, _request(regime="fixed"), ("quantity",), "quantity_forbidden")


def test_fixed_without_quantity_is_accepted() -> None:
    """Regime fixed sem quantity é válido (§2)."""
    parsed = SimulationRequest.model_validate(_request(regime="fixed", quantity=None))
    assert parsed.quantity is None


@pytest.mark.parametrize("regime", ["hourly", "daily", "weekly", "monthly"])
def test_period_regimes_require_quantity(regime: str) -> None:
    """Regimes por período exigem quantity (§2)."""
    data = _request(regime=regime, quantity=None)
    _rejects(SimulationRequest, data, ("quantity",), "quantity_required")


@pytest.mark.parametrize(
    ("quantity", "accepted"),
    [("1.5", True), ("0.5", False)],  # 0.01 × 1.5 = 0.015 → 0.02; 0.01 × 0.5 = 0.005 → 0.00
)
def test_gross_that_rounds_to_zero_is_refused(quantity: str, accepted: bool) -> None:
    """Bruto que arredonda para 0.00 é erro, o que evita divisão por zero (§8.1)."""
    data = _request(amount="0.01", quantity=quantity)
    if accepted:
        SimulationRequest.model_validate(data)
    else:
        _rejects(SimulationRequest, data, ("quantity",), "gross_rounds_to_zero")


@pytest.mark.parametrize(
    ("field", "value"), [("currency", "GBP"), ("currency", "usd"), ("regime", "yearly")]
)
def test_enums_reject_unknown_values(field: str, value: str) -> None:
    """Currency e Regime aceitam só os valores da §3."""
    _rejects(SimulationRequest, _request(**{field: value}), (field,), "enum")


@pytest.mark.parametrize("literal", ["NaN", "Infinity", "-Infinity"])
def test_non_finite_json_literals_are_refused(literal: str) -> None:
    """NaN e Infinity em JSON, lidos com parse_float=Decimal, não viram valor (§8.1)."""
    body = (
        '{"currency":"USD","regime":"hourly","amount":%s,'
        '"quantity":"160","spread_pct":"2","iof_pct":"0.38"}'
    ) % literal
    data = json.loads(body, parse_float=Decimal)
    _rejects(SimulationRequest, data, ("amount",), "decimal_not_finite")


@pytest.mark.parametrize(
    "value", ["NaN", "Infinity", "-Infinity", "inf", "1_000", "١٠", "abc", True]
)
def test_non_decimal_text_is_refused(value: Any) -> None:
    """Texto que não é decimal finito é recusado pela regex da §8.1."""
    _rejects(SimulationRequest, _request(amount=value), ("amount",), "decimal_invalid")


def test_extra_field_is_refused() -> None:
    """Campo extra é recusado (extra='forbid')."""
    _rejects(SimulationRequest, _request(surprise="x"), ("surprise",), "extra_forbidden")


@pytest.mark.parametrize(
    "changes",
    [
        {"amount": "1000000001.37"},
        {"amount": "SENTINELA-99"},
        {"spread_pct": "101.7531"},
        {"surprise": "SENTINELA-99"},
    ],
)
def test_error_text_never_echoes_submitted_value(changes: dict[str, Any]) -> None:
    """Nenhuma mensagem de erro ecoa o valor enviado (§3 e §8.1)."""
    with pytest.raises(ValidationError) as info:
        SimulationRequest.model_validate(_request(**changes))
    text = str(info.value) + json.dumps(info.value.errors(include_input=False), default=str)
    for value in changes.values():
        assert str(value) not in text


@pytest.mark.parametrize(
    ("rate", "error_type"),
    [
        ("0.000001", None), ("999.999999", None), ("0", "decimal_too_low"),
        ("1000", "decimal_too_high"), ("5.1234567", "decimal_max_places"), (5.0, "decimal_invalid"),
    ],
)
def test_rate_quote_bounds_and_no_float(rate: Any, error_type: str | None) -> None:
    """Taxa: 0 < rate < 1000 com 6 casas; saída não aceita float (§4, §8.1)."""
    if error_type is None:
        RateQuote.model_validate({**QUOTE, "rate": rate})
    else:
        _rejects(RateQuote, {**QUOTE, "rate": rate}, ("rate",), error_type)


def test_rate_quote_converts_offset_to_utc() -> None:
    """quoted_at com offset sai em UTC (§3)."""
    parsed = RateQuote.model_validate({**QUOTE, "quoted_at": "2026-10-30T10:00:00-03:00"})
    assert parsed.quoted_at == datetime(2026, 10, 30, 13, 0, tzinfo=UTC)
    assert parsed.quoted_at.utcoffset() == timedelta(0)


@pytest.mark.parametrize("net", ["23430.63", "23430.61", "0.00"])
def test_response_refuses_breakdown_that_does_not_add_up(net: str) -> None:
    """gross − spread − iof deve ser igual ao net (§2, propriedade obrigatória)."""
    with pytest.raises(ValidationError) as info:
        SimulationResponse.model_validate({**RESPONSE, "net_brl": net})
    assert "net_mismatch" in {error["type"] for error in info.value.errors()}


def test_response_refuses_altered_notice() -> None:
    """O aviso é constante; qualquer outro texto é recusado (§3)."""
    with pytest.raises(ValidationError) as info:
        SimulationResponse.model_validate({**RESPONSE, "notice": "Aviso alterado."})
    assert "notice_mismatch" in {error["type"] for error in info.value.errors()}


def test_error_keys_raised_by_errors_module_exist_in_error_key() -> None:
    """Toda chave de errors.py existe em ErrorKey (§3)."""
    raised = {RatesUnavailableError().key, PdfUnavailableError().key}
    assert raised <= {member.value for member in ErrorKey}


def test_error_key_set_matches_spec_table() -> None:
    """ErrorKey tem exatamente as cinco chaves da tabela de erros da §3."""
    assert {member.value for member in ErrorKey} == {
        "validation_error",
        "not_found",
        "rates_unavailable",
        "pdf_unavailable",
        "internal_error",
    }
