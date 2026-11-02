"""Testes unitários de services/calculator.py (spec backend-mvp-v1, §2; REQ-02, REQ-03).

Função pura: sem rede, sem relógio e sem banco. Os valores esperados saem das
fórmulas da §2 e foram conferidos à mão; nenhum foi copiado da saída do código.
"""

from __future__ import annotations

import dataclasses
import itertools
from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from src.backend.services.calculator import Breakdown, calculate
from src.shared.schemas import Regime

MONEY_FIELDS = ("gross_foreign", "gross_brl", "spread_brl", "iof_brl", "net_brl")


def _run(
    regime: Regime = Regime.HOURLY,
    amount: str = "30",
    quantity: str | None = "160",
    rate: str = "5.000000",
    spread_pct: str = "2",
    iof_pct: str = "0.38",
) -> Breakdown:
    """Chama ``calculate`` com entradas em texto, como chegam do contrato.

    Args:
        regime: Regime de cobrança.
        amount: Valor por unidade, em texto decimal.
        quantity: Quantidade, ou ``None`` no regime fixed.
        rate: Cotação em BRL por unidade, em texto decimal.
        spread_pct: Spread em %, em texto decimal.
        iof_pct: IOF em %, em texto decimal.

    Returns:
        O detalhamento calculado.
    """
    return calculate(
        regime=regime,
        amount=Decimal(amount),
        quantity=None if quantity is None else Decimal(quantity),
        rate=Decimal(rate),
        spread_pct=Decimal(spread_pct),
        iof_pct=Decimal(iof_pct),
    )


def test_spec_section2_example_gives_exact_values() -> None:
    """Exemplo da §2: USD, hourly, 30 × 160, cotação 5, spread 2, IOF 0,38."""
    result = _run()
    assert str(result.gross_foreign) == "4800.00"
    assert str(result.gross_brl) == "24000.00"
    assert str(result.spread_brl) == "480.00"
    assert str(result.iof_brl) == "89.38"
    assert str(result.net_brl) == "23430.62"
    assert str(result.effective_rate) == "4.881379"


def test_money_fields_keep_two_places_and_rate_keeps_six() -> None:
    """Escala canônica: 2 casas nos valores em moeda e 6 na taxa efetiva (§2)."""
    result = _run()
    for name in MONEY_FIELDS:
        assert getattr(result, name).as_tuple().exponent == -2, name
    assert result.effective_rate.as_tuple().exponent == -6


@pytest.mark.parametrize(
    ("regime", "amount", "quantity", "gross_foreign", "gross_brl"),
    [
        (Regime.HOURLY, "30", "160", "4800.00", "24000.00"),
        (Regime.DAILY, "100", "5", "500.00", "2500.00"),
        (Regime.WEEKLY, "250", "4", "1000.00", "5000.00"),
        (Regime.MONTHLY, "1000", "12", "12000.00", "60000.00"),
        (Regime.FIXED, "1000", None, "1000.00", "5000.00"),
    ],
)
def test_each_of_the_five_regimes_section2(
    regime: Regime,
    amount: str,
    quantity: str | None,
    gross_foreign: str,
    gross_brl: str,
) -> None:
    """Bruto por regime: amount × quantity nos períodos; amount puro no fixed (§2)."""
    result = _run(
        regime=regime,
        amount=amount,
        quantity=quantity,
        rate="5",
        spread_pct="0",
        iof_pct="0",
    )
    assert str(result.gross_foreign) == gross_foreign
    assert str(result.gross_brl) == gross_brl
    assert result.net_brl == result.gross_brl
    assert str(result.effective_rate) == "5.000000"


@pytest.mark.parametrize(
    ("rate", "spread_pct", "iof_pct", "spread_brl", "iof_brl", "net_brl"),
    [
        # 12.50 × 1 % = 0.125: HALF_EVEN vai ao 0.12 par; HALF_UP daria 0.13.
        ("1.250000", "1", "0", "0.12", "0.00", "12.38"),
        # 14.50 × 1 % = 0.145: HALF_EVEN vai ao 0.14 par; HALF_UP daria 0.15.
        ("1.450000", "1", "0", "0.14", "0.00", "14.36"),
        # Mesmo empate no IOF: (12.50 − 0) × 1 % = 0.125 → 0.12.
        ("1.250000", "0", "1", "0.00", "0.12", "12.38"),
    ],
)
def test_round_half_even_differs_from_half_up(
    rate: str,
    spread_pct: str,
    iof_pct: str,
    spread_brl: str,
    iof_brl: str,
    net_brl: str,
) -> None:
    """ROUND_HALF_EVEN em empates de terceira casa com dígito anterior par (§2)."""
    result = _run(amount="10", quantity="1", rate=rate, spread_pct=spread_pct, iof_pct=iof_pct)
    assert str(result.spread_brl) == spread_brl
    assert str(result.iof_brl) == iof_brl
    assert str(result.net_brl) == net_brl


def test_zero_spread_and_iof_leave_net_equal_to_gross() -> None:
    """Spread 0 e IOF 0: nenhum desconto, líquido igual ao bruto (§2)."""
    result = _run(amount="10", quantity="1", rate="5", spread_pct="0", iof_pct="0")
    assert str(result.spread_brl) == "0.00"
    assert str(result.iof_brl) == "0.00"
    assert str(result.net_brl) == "50.00"
    assert str(result.effective_rate) == "5.000000"


def test_spread_of_one_hundred_percent_zeroes_net() -> None:
    """Spread de 100 %: o spread consome todo o bruto (§2, limite superior)."""
    result = _run(spread_pct="100", iof_pct="0")
    assert str(result.spread_brl) == "24000.00"
    assert str(result.net_brl) == "0.00"
    assert str(result.effective_rate) == "0.000000"


def test_iof_of_one_hundred_percent_zeroes_net() -> None:
    """IOF de 100 % sobre o que sobra do spread consome todo o líquido (§2)."""
    result = _run(spread_pct="0", iof_pct="100")
    assert str(result.iof_brl) == "24000.00"
    assert str(result.net_brl) == "0.00"


# Tabela ampla: cada combinação precisa cumprir a identidade da §2.
# O bruto nunca arredonda para zero aqui (valor mínimo 0,01 × 1), o que evita divisão por zero.
_AMOUNTS = ["0.01", "1", "30", "999.99", "1000000000"]
_QUANTITIES = ["1", "160", "100000"]
_RATES = ["0.000001", "0.5", "5.432501", "999.999999"]
_SPREADS = ["0", "0.0001", "2", "100"]
_IOFS = ["0", "0.38", "7.5", "99.9999"]


@pytest.mark.parametrize(
    ("amount", "quantity", "rate", "spread_pct", "iof_pct"),
    list(itertools.product(_AMOUNTS, _QUANTITIES, _RATES, _SPREADS, _IOFS)),
)
def test_identity_gross_minus_spread_minus_iof_equals_net(
    amount: str,
    quantity: str,
    rate: str,
    spread_pct: str,
    iof_pct: str,
) -> None:
    """Propriedade da §2 em toda combinação: bruto − spread − IOF == líquido."""
    result = _run(
        amount=amount,
        quantity=quantity,
        rate=rate,
        spread_pct=spread_pct,
        iof_pct=iof_pct,
    )
    assert result.gross_brl - result.spread_brl - result.iof_brl == result.net_brl, (
        "a identidade bruto − spread − IOF == líquido falhou"
    )
    for name in MONEY_FIELDS:
        assert getattr(result, name).as_tuple().exponent == -2, name


def test_every_result_field_is_decimal_never_float() -> None:
    """Todas as saídas são Decimal; float é proibido no cálculo (§2)."""
    result = _run()
    for field in dataclasses.fields(Breakdown):
        value = getattr(result, field.name)
        assert type(value) is Decimal, f"{field.name} deveria ser Decimal"


def test_breakdown_is_frozen() -> None:
    """Breakdown é imutável (dataclass frozen, §8.1)."""
    result = _run()
    with pytest.raises(FrozenInstanceError):
        result.net_brl = Decimal("1")  # type: ignore[misc]
