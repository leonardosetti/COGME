"""Cálculo puro do recebimento em moeda estrangeira (spec backend-mvp-v1, §2; REQ-02, REQ-03).

Sem rede, relógio ou banco. Toda a aritmética roda em um contexto decimal próprio, com
``ROUND_HALF_EVEN``: o resultado não depende do contexto ambiente do processo. Alíquotas não
existem aqui; spread e IOF são sempre informados pelo usuário.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import (
    MAX_EMAX,
    MIN_EMIN,
    ROUND_HALF_EVEN,
    Context,
    Decimal,
    DivisionByZero,
    InvalidOperation,
    Overflow,
    localcontext,
)
from typing import Final

from src.shared.schemas import Regime

_MONEY_STEP: Final[Decimal] = Decimal("0.01")
_RATE_STEP: Final[Decimal] = Decimal("0.000001")
_HUNDRED: Final[Decimal] = Decimal("100")

# Com os limites do contrato, nenhum produto passa de 40 dígitos significativos. Com 64 dígitos
# a divisão também não sofre arredondamento duplo antes do q6. Todos os campos são explícitos
# porque Context() herda de DefaultContext o que for omitido.
_CONTEXT: Final[Context] = Context(
    prec=64,
    rounding=ROUND_HALF_EVEN,
    Emin=MIN_EMIN,
    Emax=MAX_EMAX,
    capitals=1,
    clamp=0,
    flags=[],
    traps=[InvalidOperation, DivisionByZero, Overflow],
)


def q2(value: Decimal) -> Decimal:
    """Arredonda para a escala de dinheiro: 2 casas com ``ROUND_HALF_EVEN``.

    Args:
        value: Valor finito.

    Returns:
        O valor com exatamente 2 casas decimais.

    Raises:
        decimal.InvalidOperation: Se o valor não couber na precisão do contexto.
    """
    return value.quantize(_MONEY_STEP, rounding=ROUND_HALF_EVEN, context=_CONTEXT)


def q6(value: Decimal) -> Decimal:
    """Arredonda para a escala de taxas: 6 casas com ``ROUND_HALF_EVEN``.

    Args:
        value: Valor finito.

    Returns:
        O valor com exatamente 6 casas decimais.

    Raises:
        decimal.InvalidOperation: Se o valor não couber na precisão do contexto.
    """
    return value.quantize(_RATE_STEP, rounding=ROUND_HALF_EVEN, context=_CONTEXT)


@dataclass(frozen=True, slots=True)
class Breakdown:
    """Detalhamento de uma simulação.

    Attributes:
        gross_foreign: Bruto na moeda estrangeira.
        gross_brl: Bruto convertido para BRL.
        spread_brl: Spread em BRL.
        iof_brl: IOF em BRL.
        net_brl: Líquido em BRL.
        effective_rate: BRL líquido por unidade estrangeira.
    """

    gross_foreign: Decimal
    gross_brl: Decimal
    spread_brl: Decimal
    iof_brl: Decimal
    net_brl: Decimal
    effective_rate: Decimal


def _gross(regime: Regime, amount: Decimal, quantity: Decimal | None) -> Decimal:
    """Calcula o bruto estrangeiro do regime, antes do arredondamento.

    Args:
        regime: Regime de cobrança.
        amount: Valor por unidade do regime.
        quantity: Quantidade de unidades; ignorada em ``fixed``.

    Returns:
        ``amount`` em ``fixed``; ``amount × quantity`` nos regimes por período.

    Raises:
        ValueError: Se o regime for por período e ``quantity`` for ``None``.
    """
    if regime == Regime.FIXED:
        return amount
    if quantity is None:
        raise ValueError("Regime por período exige quantidade.")
    return amount * quantity


def calculate(
    regime: Regime,
    amount: Decimal,
    quantity: Decimal | None,
    rate: Decimal,
    spread_pct: Decimal,
    iof_pct: Decimal,
) -> Breakdown:
    """Aplica as fórmulas da §2 da spec.

    A coerência entre ``regime`` e ``quantity`` é validada pelo schema; aqui ``fixed`` apenas
    ignora ``quantity``. O líquido sai por subtração, o que garante a identidade
    ``gross_brl − spread_brl − iof_brl == net_brl``.

    Args:
        regime: Regime de cobrança.
        amount: Valor por unidade do regime.
        quantity: Quantidade de unidades; ignorada em ``fixed``.
        rate: Cotação em BRL por 1 unidade estrangeira.
        spread_pct: Spread informado pelo usuário, em %.
        iof_pct: IOF informado pelo usuário, em %.

    Returns:
        O detalhamento, com 2 casas nos valores em moeda e 6 na taxa efetiva.

    Raises:
        ValueError: Se o regime for por período e ``quantity`` for ``None``.
        decimal.DivisionByZero: Se o bruto arredondar para zero com líquido positivo.
        decimal.InvalidOperation: Se o bruto e o líquido forem zero ou o valor exceder a
            precisão do contexto.

    Example:
        >>> result = calculate(
        ...     Regime.HOURLY, Decimal("30"), Decimal("160"),
        ...     Decimal("5.000000"), Decimal("2"), Decimal("0.38"),
        ... )
        >>> str(result.net_brl), str(result.effective_rate)
        ('23430.62', '4.881379')
    """
    with localcontext(_CONTEXT):
        gross_foreign = q2(_gross(regime, amount, quantity))
        gross_brl = q2(gross_foreign * rate)
        spread_brl = q2(gross_brl * spread_pct / _HUNDRED)
        iof_brl = q2((gross_brl - spread_brl) * iof_pct / _HUNDRED)
        net_brl = gross_brl - spread_brl - iof_brl
        effective_rate = q6(net_brl / gross_foreign)
    return Breakdown(
        gross_foreign=gross_foreign,
        gross_brl=gross_brl,
        spread_brl=spread_brl,
        iof_brl=iof_brl,
        net_brl=net_brl,
        effective_rate=effective_rate,
    )
