import { NextResponse } from "next/server";
import { isNewsCacheStale, refreshNews } from "@/lib/news";
import { readNewsCache, writeNewsCache } from "@/lib/news-store";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST() {
  try {
    const existing = await readNewsCache();
    if (!isNewsCacheStale(existing)) {
      return NextResponse.json({ ok: true, skipped: true, reason: "Atualização recente já disponível.", updatedAt: existing.updatedAt, cards: existing.cards.length });
    }
    const result = await refreshNews();
    await writeNewsCache(result.cache);
    return NextResponse.json({
      ok: true,
      updatedAt: result.cache.updatedAt,
      cards: result.cache.cards.length,
      aiGenerated: result.aiGenerated,
      sources: result.statuses,
    });
  } catch (error) {
    return NextResponse.json({ error: error instanceof Error ? error.message : "Falha ao atualizar notícias." }, { status: 500 });
  }
}
