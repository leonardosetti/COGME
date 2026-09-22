import Link from "next/link";
import NewsSection from "@/components/NewsSection";
import { refreshNewsIfStale } from "@/lib/news-store";

export default async function DashboardPage() {
  const news = await refreshNewsIfStale();
  return <>
    <header className="page-header"><div><div className="eyebrow">Visão geral</div><h1>Bom te ver por aqui.</h1><p>Acompanhe suas conversões e mantenha seus ganhos sob controle.</p></div><div className="user-chip"><span className="avatar">A</span> Conta demonstrativa</div></header>
    <section className="stats-grid"><div className="stat-card"><small>Simulações realizadas</small><strong>12</strong><span>+ 3 nesta semana</span></div><div className="stat-card"><small>Última cotação usada</small><strong>R$ 5,42</strong><span>USD → BRL · há 8 min</span></div><div className="stat-card"><small>Invoices geradas</small><strong>04</strong><span>Prontas para exportar</span></div></section>
    <section className="dashboard-grid"><div className="surface-card"><h2>Progresso do seu planejamento</h2><p className="subtle">Você já configurou as principais informações para simular seus ganhos.</p><div className="metric-line"><span>Perfil de simulação</span><strong>42%</strong></div><div className="progress"><span /></div><div className="activity"><div className="activity-item"><div className="activity-icon">✓</div><div><strong>Conta criada</strong><small>Informações básicas configuradas</small></div></div><div className="activity-item"><div className="activity-icon">↗</div><div><strong>Primeira simulação disponível</strong><small>Compare regimes de contratação</small></div></div><div className="activity-item"><div className="activity-icon">PDF</div><div><strong>Invoice pronta para emissão</strong><small>Gere um documento a partir do resultado</small></div></div></div></div><div className="surface-card cta-card"><div className="eyebrow" style={{ color: "#d6fff8" }}>Próximo passo</div><h2>Descubra seu ganho líquido.</h2><p className="subtle">Configure sua moeda, regime e encargos. O cálculo leva poucos segundos.</p><Link className="primary-button" href="/simulacoes">Começar simulação →</Link></div></section>
    <NewsSection news={news} />
  </>;
}
