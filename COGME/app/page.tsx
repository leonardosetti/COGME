import Link from "next/link";
import PublicHeader from "@/components/PublicHeader";

export default function Home() {
  return <main className="public-page">
    <PublicHeader active="home" />
    <section className="landing-hero">
      <div className="landing-copy">
        <div className="eyebrow">Conversão de ganhos em moeda estrangeira</div>
        <h1>Clareza para cada ganho internacional.</h1>
        <p>Transforme seus recebimentos em dólar ou euro em uma visão clara do valor que chega ao seu bolso.</p>
        <div className="landing-actions"><Link className="primary-button" href="/login">Começar agora →</Link><Link className="secondary-button" href="/sobre">Conheça o COGME</Link></div>
      </div>
      <div className="landing-preview" aria-label="Prévia do painel COGME">
        <div className="preview-top"><span className="preview-label">Visão financeira</span><span className="preview-status">● Atualizado</span></div>
        <small>Ganho líquido estimado</small>
        <strong>R$ 18.425,60</strong>
        <div className="preview-chart"><span /><span /><span /><span /><span /><span /><span /></div>
        <div className="preview-footer"><span>USD → BRL</span><b>+12,8%</b></div>
      </div>
    </section>
    <section className="landing-features">
      <div className="eyebrow">Por que usar o COGME</div>
      <h2>Decisões financeiras mais simples.</h2>
      <div className="feature-grid"><article className="surface-card feature-card"><span className="feature-icon">↗</span><h3>Simule em segundos</h3><p>Compare diferentes regimes de contratação e veja o impacto das taxas no resultado.</p></article><article className="surface-card feature-card"><span className="feature-icon">◎</span><h3>Cotações atualizadas</h3><p>Use cotações de referência para tomar decisões com mais segurança e transparência.</p></article><article className="surface-card feature-card"><span className="feature-icon">PDF</span><h3>Organize seus recebimentos</h3><p>Salve suas simulações e gere invoices para manter tudo pronto quando precisar.</p></article></div>
    </section>
    <section className="landing-cta"><div><div className="eyebrow">Comece hoje</div><h2>Seu ganho internacional, sob controle.</h2></div><Link className="primary-button" href="/login">Acessar plataforma →</Link></section>
    <footer className="public-footer"><span>© 2026 COGME</span><span>Conversão de ganhos em moeda estrangeira</span></footer>
  </main>;
}
