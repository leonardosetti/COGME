"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { NEWS_REFRESH_INTERVAL_MS } from "@/lib/news";

export default function NewsRefreshButton() {
  const router = useRouter();
  const [status, setStatus] = useState<"idle" | "loading" | "done" | "error">("idle");

  useEffect(() => {
    const timer = window.setInterval(() => void refresh(), NEWS_REFRESH_INTERVAL_MS);
    return () => window.clearInterval(timer);
  }, []);

  async function refresh() {
    setStatus("loading");
    try {
      const response = await fetch("/api/news/update", { method: "POST" });
      if (!response.ok) throw new Error("Falha no job");
      setStatus("done");
      router.refresh();
      window.setTimeout(() => setStatus("idle"), 2500);
    } catch {
      setStatus("error");
      window.setTimeout(() => setStatus("idle"), 3500);
    }
  }

  return <button className="secondary-button news-refresh-button no-print" type="button" onClick={() => void refresh()} disabled={status === "loading"}>
    {status === "loading" ? "Atualizando..." : status === "done" ? "✓ Atualizado" : status === "error" ? "Tentar novamente" : "↻ Atualizar notícias"}
  </button>;
}
