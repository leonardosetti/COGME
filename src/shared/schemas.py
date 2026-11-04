"""HTTP contract of the COGME API, version ``/v1`` (single source of truth).

Decimal policy:
    * Money, rates and percentages are ``Decimal``; ``float`` is never stored.
    * Input accepts a JSON string or number. A number that already reached Python as
      ``float`` is rebuilt from its shortest ``repr``, never from its binary value. Every
      value this contract accepts has at most 12 significant digits, so the ``repr`` gives
      back exactly what the client wrote.
    * Output accepts no ``float`` at all and leaves as a plain JSON string, at a fixed scale
      and never in scientific notation.

Validation messages are in PT-BR and never echo the submitted value. All examples are
synthetic.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import UTC, date, datetime
from decimal import ROUND_HALF_EVEN, Context, Decimal
from enum import StrEnum
from typing import Annotated, Final, Literal, NoReturn

from pydantic import (
    AfterValidator,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    PlainSerializer,
    ValidationInfo,
    field_validator,
    model_validator,
)
from pydantic_core import PydanticCustomError

__all__ = [
    "NOTICE",
    "Currency",
    "ErrorBody",
    "ErrorDetail",
    "ErrorKey",
    "ErrorResponse",
    "HealthResponse",
    "InvoiceParty",
    "InvoiceRequest",
    "RateQuote",
    "RateSource",
    "Regime",
    "SimulationRequest",
    "SimulationResponse",
]

NOTICE: Final[str] = (
    "Simulação de caráter informativo; spread e IOF foram informados pelo usuário "
    "e não substituem a orientação de um profissional habilitado."
)

_MONEY_PLACES: Final[int] = 2
_PERCENT_PLACES: Final[int] = 4
_RATE_PLACES: Final[int] = 6

_MAX_AMOUNT: Final[Decimal] = Decimal("1000000000")
_MAX_QUANTITY: Final[Decimal] = Decimal("100000")
_MAX_PERCENT: Final[Decimal] = Decimal("100")
_MAX_RATE: Final[Decimal] = Decimal("1000")
# Output ceiling derived from the input limits: amount x quantity x rate < 10^17.
_MAX_OUTPUT: Final[Decimal] = Decimal("100000000000000000")
_ZERO: Final[Decimal] = Decimal("0")

# Bounds the parsing cost of a string; every valid value fits with room to spare.
_MAX_DECIMAL_TEXT_LENGTH: Final[int] = 64
# Decimal() alone would also take "1_000", non-ASCII digits, "NaN" and "Infinity".
_DECIMAL_TEXT: Final[re.Pattern[str]] = re.compile(
    r"-?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?",
)
# Explicit context: the outcome must not depend on the ambient decimal context.
_DECIMAL_CONTEXT: Final[Context] = Context(prec=64, rounding=ROUND_HALF_EVEN)


class Currency(StrEnum):
    """Foreign currencies the API quotes."""

    USD = "USD"
    EUR = "EUR"


class Regime(StrEnum):
    """Billing regimes of the simulated income."""

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    FIXED = "fixed"


class RateSource(StrEnum):
    """Public sources of the exchange rate."""

    FRANKFURTER = "frankfurter"
    PTAX = "ptax"


class ErrorKey(StrEnum):
    """Stable keys of the canonical error model."""

    VALIDATION_ERROR = "validation_error"
    NOT_FOUND = "not_found"
    RATES_UNAVAILABLE = "rates_unavailable"
    PDF_UNAVAILABLE = "pdf_unavailable"
    INTERNAL_ERROR = "internal_error"


def _raise_invalid_decimal() -> NoReturn:
    """Reject a value that is not a decimal number, without echoing it.

    Raises:
        PydanticCustomError: Always.
    """
    raise PydanticCustomError("decimal_invalid", "Informe um número decimal válido.")


def _parse_decimal(value: object) -> Decimal:
    """Build a finite ``Decimal`` without going through a binary value.

    Args:
        value: Raw value of the field.

    Returns:
        The exact decimal the input denotes.

    Raises:
        PydanticCustomError: If the value is not a finite decimal number.
    """
    # bool is a subclass of int, so this check must come first.
    if isinstance(value, bool):
        _raise_invalid_decimal()
    if isinstance(value, Decimal):
        parsed = value
    elif isinstance(value, int):
        parsed = Decimal(value)
    elif isinstance(value, float):
        parsed = Decimal(repr(value))
    elif (
        isinstance(value, str)
        and len(value) <= _MAX_DECIMAL_TEXT_LENGTH
        and _DECIMAL_TEXT.fullmatch(value)
    ):
        parsed = Decimal(value)
    else:
        _raise_invalid_decimal()
    if not parsed.is_finite():
        raise PydanticCustomError("decimal_not_finite", "NaN e infinito não são aceitos.")
    return parsed


def _parse_output_decimal(value: object) -> Decimal:
    """Build a ``Decimal`` for an output field, where ``float`` is a defect.

    Args:
        value: Raw value of the field.

    Returns:
        The exact decimal the input denotes.

    Raises:
        PydanticCustomError: If the value is a ``float`` or not a finite decimal.
    """
    if isinstance(value, float):
        _raise_invalid_decimal()
    return _parse_decimal(value)


def _significant_places(value: Decimal) -> int:
    """Count the decimal places of a finite value, ignoring trailing zeros.

    Reads the digit tuple because ``Decimal.normalize`` rounds to the context precision,
    which would hide excess places on long inputs.

    Args:
        value: A finite decimal.

    Returns:
        How many decimal places the value needs to be represented exactly.
    """
    if value.is_zero():
        return 0
    _, digits, exponent = value.as_tuple()
    if not isinstance(exponent, int):  # pragma: no cover - finite values have an int exponent
        _raise_invalid_decimal()
    text = "".join(map(str, digits))
    trailing_zeros = len(text) - len(text.rstrip("0"))
    return max(0, -(exponent + trailing_zeros))


def _round_money(value: Decimal) -> Decimal:
    """Round a value to the money scale with ``ROUND_HALF_EVEN``.

    Args:
        value: A finite decimal within the output bounds.

    Returns:
        The value with two decimal places.
    """
    step = Decimal(1).scaleb(-_MONEY_PLACES)
    return value.quantize(step, rounding=ROUND_HALF_EVEN, context=_DECIMAL_CONTEXT)


@dataclass(frozen=True)
class _DecimalRule:
    """Limits of a decimal field, which also bring the value to its canonical form.

    Attributes:
        places: Maximum decimal places, and the scale of the canonical form.
        minimum: Lower limit.
        maximum: Upper limit.
        exclusive_minimum: Whether the lower limit itself is rejected.
        exclusive_maximum: Whether the upper limit itself is rejected.
    """

    places: int
    minimum: Decimal
    maximum: Decimal
    exclusive_minimum: bool = False
    exclusive_maximum: bool = False

    def __call__(self, value: Decimal) -> Decimal:
        """Validate the value and bring it to a fixed scale.

        Limits run first: they bound the digit count of what reaches the quantization, so
        an input such as ``1E+999999999`` is refused at no cost.

        Args:
            value: A finite decimal.

        Returns:
            The same number at the scale of the rule, with no negative zero.

        Raises:
            PydanticCustomError: If a limit or the number of places is violated.
        """
        self._check_limits(value)
        if _significant_places(value) > self.places:
            raise PydanticCustomError(
                "decimal_max_places",
                "Use no máximo {places} casas decimais.",
                {"places": self.places},
            )
        step = Decimal(1).scaleb(-self.places)
        canonical = value.quantize(step, context=_DECIMAL_CONTEXT)
        return canonical.copy_abs() if canonical.is_zero() else canonical

    def _check_limits(self, value: Decimal) -> None:
        """Enforce both limits of the rule.

        Args:
            value: A finite decimal.

        Raises:
            PydanticCustomError: If the value falls outside the limits.
        """
        if self.exclusive_minimum and value <= self.minimum:
            raise PydanticCustomError(
                "decimal_too_low",
                "O valor deve ser maior que {limit}.",
                {"limit": format(self.minimum, "f")},
            )
        if value < self.minimum:
            raise PydanticCustomError(
                "decimal_too_low",
                "O valor deve ser maior ou igual a {limit}.",
                {"limit": format(self.minimum, "f")},
            )
        if self.exclusive_maximum and value >= self.maximum:
            raise PydanticCustomError(
                "decimal_too_high",
                "O valor deve ser menor que {limit}.",
                {"limit": format(self.maximum, "f")},
            )
        if value > self.maximum:
            raise PydanticCustomError(
                "decimal_too_high",
                "O valor deve ser menor ou igual a {limit}.",
                {"limit": format(self.maximum, "f")},
            )


def _format_decimal(value: Decimal) -> str:
    """Render a decimal as plain text, never in scientific notation.

    Args:
        value: A validated decimal.

    Returns:
        The fixed-point text of the value.
    """
    return format(value, "f")


_AS_PLAIN_TEXT: Final[PlainSerializer] = PlainSerializer(
    _format_decimal,
    return_type=str,
    when_used="json",
)

AmountInput = Annotated[
    Decimal,
    BeforeValidator(_parse_decimal),
    AfterValidator(
        _DecimalRule(
            places=_MONEY_PLACES,
            minimum=_ZERO,
            maximum=_MAX_AMOUNT,
            exclusive_minimum=True,
        ),
    ),
    _AS_PLAIN_TEXT,
]
QuantityInput = Annotated[
    Decimal,
    BeforeValidator(_parse_decimal),
    AfterValidator(
        _DecimalRule(
            places=_MONEY_PLACES,
            minimum=_ZERO,
            maximum=_MAX_QUANTITY,
            exclusive_minimum=True,
        ),
    ),
    _AS_PLAIN_TEXT,
]
PercentInput = Annotated[
    Decimal,
    BeforeValidator(_parse_decimal),
    AfterValidator(_DecimalRule(places=_PERCENT_PLACES, minimum=_ZERO, maximum=_MAX_PERCENT)),
    _AS_PLAIN_TEXT,
]
PercentOutput = Annotated[
    Decimal,
    BeforeValidator(_parse_output_decimal),
    AfterValidator(_DecimalRule(places=_PERCENT_PLACES, minimum=_ZERO, maximum=_MAX_PERCENT)),
    _AS_PLAIN_TEXT,
]
PositiveMoneyOutput = Annotated[
    Decimal,
    BeforeValidator(_parse_output_decimal),
    AfterValidator(
        _DecimalRule(
            places=_MONEY_PLACES,
            minimum=_ZERO,
            maximum=_MAX_OUTPUT,
            exclusive_minimum=True,
        ),
    ),
    _AS_PLAIN_TEXT,
]
MoneyOutput = Annotated[
    Decimal,
    BeforeValidator(_parse_output_decimal),
    AfterValidator(_DecimalRule(places=_MONEY_PLACES, minimum=_ZERO, maximum=_MAX_OUTPUT)),
    _AS_PLAIN_TEXT,
]
RateOutput = Annotated[
    Decimal,
    BeforeValidator(_parse_output_decimal),
    AfterValidator(
        _DecimalRule(
            places=_RATE_PLACES,
            minimum=_ZERO,
            maximum=_MAX_RATE,
            exclusive_minimum=True,
            exclusive_maximum=True,
        ),
    ),
    _AS_PLAIN_TEXT,
]
# Money rounding can lift it slightly above the quote, so the quote ceiling does not apply.
EffectiveRateOutput = Annotated[
    Decimal,
    BeforeValidator(_parse_output_decimal),
    AfterValidator(_DecimalRule(places=_RATE_PLACES, minimum=_ZERO, maximum=_MAX_OUTPUT)),
    _AS_PLAIN_TEXT,
]


def _as_utc(value: datetime) -> datetime:
    """Require a timezone-aware datetime and convert it to UTC.

    Args:
        value: Parsed datetime.

    Returns:
        The same instant in UTC.

    Raises:
        PydanticCustomError: If the datetime has no timezone.
    """
    if value.utcoffset() is None:
        raise PydanticCustomError("datetime_naive", "Informe a data e hora com fuso horário.")
    return value.astimezone(UTC)


def _require_notice(value: str) -> str:
    """Refuse any notice other than the constant one.

    Args:
        value: Candidate notice.

    Returns:
        The notice, unchanged.

    Raises:
        PydanticCustomError: If the notice differs from the constant.
    """
    if value != NOTICE:
        raise PydanticCustomError("notice_mismatch", "O aviso informativo não pode ser alterado.")
    return value


UtcDatetime = Annotated[datetime, AfterValidator(_as_utc)]
NoticeText = Annotated[str, AfterValidator(_require_notice)]


class _Schema(BaseModel):
    """Base of every schema: closed, immutable and free of input in error reprs."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        hide_input_in_errors=True,
        str_strip_whitespace=True,
    )


class HealthResponse(_Schema):
    """Answer of ``GET /v1/health``."""

    model_config = ConfigDict(json_schema_extra={"examples": [{"status": "ok"}]})

    status: Literal["ok"] = Field(description="Estado da API.")


class RateQuote(_Schema):
    """Exchange rate in BRL for one unit of the foreign currency."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "currency": "USD",
                    "rate": "5.000000",
                    "source": "frankfurter",
                    "quoted_at": "2026-01-01T00:00:00Z",
                    "bulletin": None,
                    "stale": False,
                },
            ],
        },
    )

    currency: Currency = Field(description="Moeda estrangeira cotada.")
    rate: RateOutput = Field(description="BRL por 1 unidade estrangeira, com 6 casas.")
    source: RateSource = Field(description="Fonte pública da cotação.")
    quoted_at: UtcDatetime = Field(description="Instante da cotação, em UTC.")
    bulletin: str | None = Field(description="Boletim da PTAX; nulo nas demais fontes.")
    stale: bool = Field(description="Verdadeiro quando a cotação vem de cache vencido.")


class SimulationRequest(_Schema):
    """Input of ``POST /v1/simulate``.

    Field order matters: ``quantity`` is cross-checked against ``regime`` and ``amount``,
    which must be validated first.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "currency": "USD",
                    "regime": "hourly",
                    "amount": "30.00",
                    "quantity": "160",
                    "spread_pct": "2",
                    "iof_pct": "0.38",
                },
                {
                    "currency": "EUR",
                    "regime": "fixed",
                    "amount": "1000.00",
                    "spread_pct": "1.5",
                    "iof_pct": "0.38",
                },
            ],
        },
    )

    currency: Currency = Field(description="Moeda estrangeira do recebimento.")
    regime: Regime = Field(description="Regime de cobrança.")
    amount: AmountInput = Field(
        description="Valor por unidade do regime: maior que 0, até 1.000.000.000, 2 casas.",
        json_schema_extra={"exclusiveMinimum": 0, "maximum": 1000000000},
    )
    quantity: QuantityInput | None = Field(
        default=None,
        validate_default=True,
        description=(
            "Quantidade de unidades: maior que 0, até 100.000, 2 casas. "
            "Obrigatória nos regimes por período; proibida em fixed."
        ),
        json_schema_extra={"exclusiveMinimum": 0, "maximum": 100000},
    )
    spread_pct: PercentInput = Field(
        description="Spread informado pelo usuário, em %: de 0 a 100, 4 casas.",
        json_schema_extra={"minimum": 0, "maximum": 100},
    )
    iof_pct: PercentInput = Field(
        description="IOF informado pelo usuário, em %: de 0 a 100, 4 casas.",
        json_schema_extra={"minimum": 0, "maximum": 100},
    )

    @field_validator("quantity", mode="after")
    @classmethod
    def _check_quantity_for_regime(
        cls,
        quantity: Decimal | None,
        info: ValidationInfo,
    ) -> Decimal | None:
        """Cross ``regime`` and ``quantity`` so the error points at ``quantity``.

        Args:
            quantity: Validated quantity, if any.
            info: Holds the fields validated before this one.

        Returns:
            The quantity, unchanged.

        Raises:
            PydanticCustomError: If the regime forbids or requires a quantity, or if the
                gross value rounds to zero, which would leave no effective rate.
        """
        regime = info.data.get("regime")
        if regime is None:
            return quantity
        if regime is Regime.FIXED:
            if quantity is not None:
                raise PydanticCustomError(
                    "quantity_forbidden",
                    "A quantidade não é permitida no regime fixed.",
                )
            return None
        if quantity is None:
            raise PydanticCustomError(
                "quantity_required",
                "Informe a quantidade para este regime.",
            )
        amount = info.data.get("amount")
        if amount is not None and _round_money(amount * quantity).is_zero():
            raise PydanticCustomError(
                "gross_rounds_to_zero",
                "O valor bruto resultante deve ser de pelo menos 0.01.",
            )
        return quantity


class SimulationResponse(_Schema):
    """Output of ``POST /v1/simulate``."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "currency": "USD",
                    "regime": "hourly",
                    "gross_foreign": "4800.00",
                    "gross_brl": "24000.00",
                    "spread_brl": "480.00",
                    "iof_brl": "89.38",
                    "net_brl": "23430.62",
                    "effective_rate": "4.881379",
                    "spread_pct": "2.0000",
                    "iof_pct": "0.3800",
                    "quote": {
                        "currency": "USD",
                        "rate": "5.000000",
                        "source": "frankfurter",
                        "quoted_at": "2026-01-01T00:00:00Z",
                        "bulletin": None,
                        "stale": False,
                    },
                    "notice": NOTICE,
                },
            ],
        },
    )

    currency: Currency = Field(description="Moeda estrangeira do recebimento.")
    regime: Regime = Field(description="Regime de cobrança.")
    gross_foreign: PositiveMoneyOutput = Field(description="Bruto na moeda estrangeira.")
    gross_brl: MoneyOutput = Field(description="Bruto convertido para BRL.")
    spread_brl: MoneyOutput = Field(description="Spread em BRL.")
    iof_brl: MoneyOutput = Field(description="IOF em BRL.")
    net_brl: MoneyOutput = Field(description="Líquido em BRL.")
    effective_rate: EffectiveRateOutput = Field(description="BRL líquido por unidade estrangeira.")
    spread_pct: PercentOutput = Field(description="Spread informado pelo usuário, em %.")
    iof_pct: PercentOutput = Field(description="IOF informado pelo usuário, em %.")
    quote: RateQuote = Field(description="Cotação usada no cálculo.")
    notice: NoticeText = Field(
        default=NOTICE,
        description="Aviso constante.",
        json_schema_extra={"const": NOTICE},
    )

    @model_validator(mode="after")
    def _check_net_invariant(self) -> SimulationResponse:
        """Refuse a breakdown that does not add up.

        Returns:
            The validated response.

        Raises:
            PydanticCustomError: If gross minus spread minus IOF differs from the net.
        """
        if self.gross_brl - self.spread_brl - self.iof_brl != self.net_brl:
            raise PydanticCustomError(
                "net_mismatch",
                "O valor líquido não confere com o bruto, o spread e o IOF.",
            )
        return self


class InvoiceParty(_Schema):
    """Issuer or client of an invoice. Personal data: never persisted or logged."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "name": "Pessoa Fictícia da Silva",
                    "tax_id": "000.000.000-00",
                    "address": "Rua Exemplo, 123, Cidade Fictícia",
                },
            ],
        },
    )

    name: str = Field(min_length=1, max_length=120, description="Nome da parte.")
    tax_id: str | None = Field(default=None, max_length=40, description="Documento fiscal.")
    address: str | None = Field(default=None, max_length=240, description="Endereço.")


class InvoiceRequest(_Schema):
    """Input of ``POST /v1/invoice``. The server recalculates the simulation."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "simulation": {
                        "currency": "USD",
                        "regime": "hourly",
                        "amount": "30.00",
                        "quantity": "160",
                        "spread_pct": "2",
                        "iof_pct": "0.38",
                    },
                    "issuer": {
                        "name": "Pessoa Fictícia da Silva",
                        "tax_id": "000.000.000-00",
                        "address": "Rua Exemplo, 123, Cidade Fictícia",
                    },
                    "client": {
                        "name": "Example Fictional LLC",
                        "tax_id": None,
                        "address": "1 Sample Street, Nowhere",
                    },
                    "invoice_number": "INV-0001",
                    "issue_date": "2026-01-15",
                    "description": "Serviços fictícios de desenvolvimento de software.",
                },
            ],
        },
    )

    simulation: SimulationRequest = Field(description="Dados recalculados pelo servidor.")
    issuer: InvoiceParty = Field(description="Quem emite a invoice.")
    client: InvoiceParty = Field(description="Quem recebe a invoice.")
    invoice_number: str = Field(min_length=1, max_length=40, description="Número da invoice.")
    issue_date: date = Field(description="Data de emissão.")
    description: str = Field(min_length=1, max_length=500, description="Descrição do serviço.")


class ErrorDetail(_Schema):
    """One invalid field. Never carries the submitted value."""

    field: str = Field(description="Nome do campo inválido.")
    message: str = Field(description="Explicação em PT-BR, sem ecoar o valor enviado.")


class ErrorBody(_Schema):
    """Content of the canonical error model."""

    key: ErrorKey = Field(description="Chave estável do erro.")
    message: str = Field(description="Mensagem em PT-BR.")
    details: list[ErrorDetail] = Field(
        default_factory=list,
        description="Campos inválidos; vazio fora de erros de validação.",
    )


class ErrorResponse(_Schema):
    """Canonical error envelope of every failure, validation included."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "error": {
                        "key": "validation_error",
                        "message": "Dados inválidos.",
                        "details": [
                            {"field": "amount", "message": "O valor deve ser maior que 0."},
                        ],
                    },
                },
                {
                    "error": {
                        "key": "rates_unavailable",
                        "message": "Cotação indisponível no momento. Tente novamente mais tarde.",
                        "details": [],
                    },
                },
            ],
        },
    )

    error: ErrorBody = Field(description="Dados do erro.")
