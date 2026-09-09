"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import type { SavedSimulation } from "@/lib/types";
import { regimeLabels } from "@/lib/simulation";

const money = new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" });
const date = new Intl.DateTimeFormat("pt-BR", { dateStyle: "medium", timeStyle: "short" });

export default function InvoicesPage() {
  const [items, setItems] = useState<SavedSimulation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    void loadItems();
  }, []);

  async function loadItems() {
    try {
      const response = await fetch("/api/simulations");
      if (!response.ok) throw new Error("Falha ao carregar");
      const data = (await response.json()) as { simulations?: SavedSimulation[] };
      setItems(data.simulations || []);
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }

  async function remove(id: string) {
    try {
      const response = await fetch("/api/simulations/" + encodeURIComponent(id), { method: "DELETE" });
      if (!response.ok) throw new Error("Falha ao excluir");
      setItems((current) => current.filter((item) => item.id !== id));
    } catch {
      setError(true);
    }
  }

  return <>
    <header className="page-header"><div><div className="eyebrow">Documentos financeiros</div><h1>Minhas invoices</h1><p>Exporte uma representação da simulação para impressão ou PDF.</p></div><Link className="primary-button" href="/simulacoes">＋ Nova simulação</Link></header>
    <div className="print-only"><h1>COGME — Invoice de simulação</h1><p>Documento gerado a partir de uma estimativa cambial. Não é documento fiscal.</p></div>
    {loading ? <div className="empty-state">Carregando suas simulações...</div> : error ? <div className="empty-state">Não foi possível consultar o banco de dados. Tente novamente.</div> : items.length === 0 ? <div className="empty-state">Você ainda não salvou nenhuma simulação.<br /><Link href="/simulacoes" style={{ color: "var(--teal-dark)", fontWeight: 700 }}>Criar primeira simulação →</Link></div> : <section className="invoice-list">{items.map((item) => <article className="surface-card invoice-item" key={item.id}><div><h3>{item.currency} · {regimeLabels[item.regime]}</h3><p>{date.format(new Date(item.createdAt))} · cotação {item.exchangeRate.toFixed(4)}</p><div className="invoice-actions no-print"><button onClick={() => window.print()}>Exportar PDF</button><button onClick={() => void remove(item.id)}>Excluir</button></div></div><div className="invoice-value"><small>Ganho líquido estimado</small><strong>{money.format(item.netBRL)}</strong><p>{money.format(item.grossBRL)} bruto · {money.format(item.feesBRL)} encargos</p></div></article>)}</section>}
  </>;
}
