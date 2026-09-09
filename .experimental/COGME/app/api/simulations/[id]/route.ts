import { NextResponse } from "next/server";
import { getRequestSession } from "@/lib/request-session";
import { deleteSimulation } from "@/lib/simulation-store";

export const runtime = "nodejs";

export async function DELETE(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const session = await getRequestSession();
  if (!session) return NextResponse.json({ error: "Não autenticado." }, { status: 401 });

  const { id } = await params;
  if (!id || id.length > 36) return NextResponse.json({ error: "Identificador inválido." }, { status: 400 });

  try {
    const removed = await deleteSimulation(session.email, id);
    return removed
      ? NextResponse.json({ ok: true })
      : NextResponse.json({ error: "Simulação não encontrada." }, { status: 404 });
  } catch {
    return NextResponse.json({ error: "Não foi possível excluir a simulação." }, { status: 503 });
  }
}
