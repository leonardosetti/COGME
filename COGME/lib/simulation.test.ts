import { describe, expect, it } from "vitest";
import { calculateSimulation } from "@/lib/simulation";

describe("calculateSimulation", () => {
  it("calcula um contrato mensal com encargos", () => {
    const result = calculateSimulation({ currency: "USD", regime: "month", unitRate: 1000, exchangeRate: 5, spread: 1, iof: 0.38, otherFees: 0 });
    expect(result.foreignAmount).toBe(1000);
    expect(result.grossBRL).toBe(5000);
    expect(result.feesBRL).toBeCloseTo(69);
    expect(result.netBRL).toBeCloseTo(4931);
  });

  it("aplica a quantidade padrão do regime por hora", () => {
    const result = calculateSimulation({ currency: "EUR", regime: "hour", unitRate: 10, exchangeRate: 6, spread: 0, iof: 0, otherFees: 0 });
    expect(result.quantity).toBe(176);
    expect(result.netBRL).toBe(10560);
  });
});
