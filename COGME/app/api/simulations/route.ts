import { NextResponse } from "next/server";
import { calculateSimulation, type Regime } from "@/lib/simulation";
import { getRequestSession } from "@/lib/request-session";
import { listSimulations, saveSimulation } from "@/lib/simulation-store";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const currencies = ["USD", "EUR"] as const;
const regimes = ["hour", "day", "week", "month", "fixed"] as const;

function isCurrency(value: unknown): value is (typeof currencies)[number] {
  return typeof value === "string" && currencies.includes(value as (typeof currencies)[number]);
}

function isRegime(value: unknown): value is Regime {
  return typeof value === "string" && regimes.includes(value as Regime);
}

function validNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value) && value >= 0;
}

export async function GET() {
  const session = await getRequestSession();
  if (!session) return NextResponse.json({ error: "Não autenticado." }, { status: 401 });

  try {
    return NextResponse.json({ simulations: await listSimulations(session.email) });
  } catch {
    return NextResponse.json({ error: "Não foi possível consultar o banco de dados." }, { status: 503 });
  }
}

export async function POST(request: Request) {
  const session = await getRequestSession();
  if (!session) return NextResponse.json({ error: "Não autenticado." }, { status: 401 });

  try {
    const body = (await request.json()) as Record<string, unknown>;
    if (
      !isCurrency(body.currency) ||
      !isRegime(body.regime) ||
      !validNumber(body.unitRate) ||
      !validNumber(body.exchangeRate) ||
      !validNumber(body.spread) ||
      !validNumber(body.iof) ||
      !validNumber(body.otherFees)
    ) {
      return NextResponse.json({ error: "Dados da simulação inválidos." }, { status: 400 });
    }

    const result = calculateSimulation({
      currency: body.currency,
      regime: body.regime,
      unitRate: body.unitRate,
      exchangeRate: body.exchangeRate,
      spread: body.spread,
      iof: body.iof,
      otherFees: body.otherFees,
    });
    const simulation = { ...result, id: crypto.randomUUID(), createdAt: new Date().toISOString() };
    await saveSimulation(session.email, simulation);
    return NextResponse.json({ simulation }, { status: 201 });
  } catch {
    return NextResponse.json({ error: "Não foi possível salvar a simulação no banco de dados." }, { status: 503 });
  }
}
