import Link from "next/link";
import PublicHeader from "@/components/PublicHeader";

export default function AboutPage() {
  return <main className="public-page">
    <PublicHeader active="about" />
    <section className="about-hero">
      <div><div className="eyebrow">Sobre o COGME</div><h1>Mais clareza para quem trabalha além das fronteiras.</h1><p>O COGME nasceu para simplificar a conversão e o planejamento de ganhos recebidos em moedas estrangeiras.</p></div>
      <div className="about-highlight"><strong>Transparência</strong><span>em cada etapa da sua conversão.</span></div>
    </section>
    <section className="about-grid"><article className="surface-card"><div className="eyebrow">Nosso propósito</div><h2>Informação para decidir melhor.</h2><p>Profissionais que atendem clientes internacionais precisam lidar com câmbio, taxas e diferentes formas de contratação. Reunimos essas informações em uma experiência direta, visual e fácil de entender.</p></article><article className="surface-card"><div className="eyebrow">Nossa visão</div><h2>Uma rotina financeira mais previsível.</h2><p>O COGME ajuda você a enxergar o valor bruto, os encargos simulados e o ganho líquido antes de tomar decisões sobre seus recebimentos.</p></article></section>
    <section className="about-values"><div className="eyebrow">O que guia o produto</div><div className="value-list"><div><strong>Clareza</strong><span>Dados organizados em uma linguagem simples.</span></div><div><strong>Autonomia</strong><span>Simulações para você explorar seus próprios cenários.</span></div><div><strong>Transparência</strong><span>Taxas e premissas visíveis no resultado.</span></div></div></section>
    <section className="landing-cta"><div><div className="eyebrow">Pronto para começar?</div><h2>Faça sua primeira simulação.</h2></div><Link className="primary-button" href="/login">Entrar no COGME →</Link></section>
    <footer className="public-footer"><span>© 2026 COGME</span><span>Conversão de ganhos em moeda estrangeira</span></footer>
  </main>;
}
