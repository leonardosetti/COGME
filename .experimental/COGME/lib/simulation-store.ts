import type { ResultSetHeader, RowDataPacket } from "mysql2";
import { db } from "@/lib/db";
import type { SavedSimulation } from "@/lib/types";

type SimulationRow = RowDataPacket & {
  id: string;
  currency: "USD" | "EUR";
  regime: SavedSimulation["regime"];
  unit_rate: number;
  exchange_rate: number;
  spread: number;
  iof: number;
  other_fees: number;
  quantity: number;
  foreign_amount: number;
  gross_brl: number;
  fees_brl: number;
  net_brl: number;
  effective_rate: number;
  created_at: Date | string;
};

function toSavedSimulation(row: SimulationRow): SavedSimulation {
  return {
    id: row.id,
    currency: row.currency,
    regime: row.regime,
    unitRate: Number(row.unit_rate),
    exchangeRate: Number(row.exchange_rate),
    spread: Number(row.spread),
    iof: Number(row.iof),
    otherFees: Number(row.other_fees),
    quantity: Number(row.quantity),
    foreignAmount: Number(row.foreign_amount),
    grossBRL: Number(row.gross_brl),
    feesBRL: Number(row.fees_brl),
    netBRL: Number(row.net_brl),
    effectiveRate: Number(row.effective_rate),
    createdAt: new Date(row.created_at).toISOString(),
  };
}

export async function listSimulations(userEmail: string) {
  const [rows] = await db.execute<SimulationRow[]>(
    "SELECT id, currency, regime, unit_rate, exchange_rate, spread, iof, other_fees, quantity, foreign_amount, gross_brl, fees_brl, net_brl, effective_rate, created_at FROM simulations WHERE user_email = ? ORDER BY created_at DESC LIMIT 50",
    [userEmail],
  );
  return rows.map(toSavedSimulation);
}

export async function saveSimulation(userEmail: string, simulation: SavedSimulation) {
  await db.execute(
    "INSERT INTO simulations (id, user_email, currency, regime, unit_rate, exchange_rate, spread, iof, other_fees, quantity, foreign_amount, gross_brl, fees_brl, net_brl, effective_rate, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    [
      simulation.id,
      userEmail,
      simulation.currency,
      simulation.regime,
      simulation.unitRate,
      simulation.exchangeRate,
      simulation.spread,
      simulation.iof,
      simulation.otherFees,
      simulation.quantity,
      simulation.foreignAmount,
      simulation.grossBRL,
      simulation.feesBRL,
      simulation.netBRL,
      simulation.effectiveRate,
      new Date(simulation.createdAt),
    ],
  );
  return simulation;
}

export async function deleteSimulation(userEmail: string, id: string) {
  const [result] = await db.execute<ResultSetHeader>(
    "DELETE FROM simulations WHERE id = ? AND user_email = ?",
    [id, userEmail],
  );
  return result.affectedRows > 0;
}
