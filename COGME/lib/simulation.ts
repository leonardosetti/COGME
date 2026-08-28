export type Regime = "hour" | "day" | "week" | "month" | "fixed";

export type SimulationInput = {
  currency: "USD" | "EUR";
  regime: Regime;
  unitRate: number;
  exchangeRate: number;
  spread: number;
  iof: number;
  otherFees: number;
};

export type SimulationResult = SimulationInput & {
  quantity: number;
  foreignAmount: number;
  grossBRL: number;
  feesBRL: number;
  netBRL: number;
  effectiveRate: number;
};

export const regimeQuantities: Record<Regime, number> = { hour: 176, day: 22, week: 4.33, month: 1, fixed: 1 };

export const regimeLabels: Record<Regime, string> = {
  hour: "Por hora",
  day: "Por dia",
  week: "Por semana",
  month: "Por mês",
  fixed: "Valor fixo",
};

export function calculateSimulation(input: SimulationInput): SimulationResult {
  const quantity = regimeQuantities[input.regime];
  const foreignAmount = input.unitRate * quantity;
  const grossBRL = foreignAmount * input.exchangeRate;
  const feeRate = (input.spread + input.iof + input.otherFees) / 100;
  const feesBRL = grossBRL * feeRate;
  const netBRL = grossBRL - feesBRL;
  return { ...input, quantity, foreignAmount, grossBRL, feesBRL, netBRL, effectiveRate: netBRL / foreignAmount };
}

/**
 * Compares regimes using the same total foreign-currency amount as the
 * selected regime instead of reusing a value with a different unit.
 */
export function calculateEquivalentRegime(input: SimulationInput, comparisonRegime: Regime): SimulationResult {
  const sourceQuantity = regimeQuantities[input.regime];
  const comparisonQuantity = regimeQuantities[comparisonRegime];
  const equivalentUnitRate = (input.unitRate * sourceQuantity) / comparisonQuantity;
  return calculateSimulation({ ...input, regime: comparisonRegime, unitRate: equivalentUnitRate });
}
