import NewsRefreshButton from "@/components/NewsRefreshButton";
import { newsSources, type NewsCache } from "@/lib/news";

function formatDate(value: string | null) {
  if (!value) return "Aguardando primeira atualização";
  return "Atualizado em " + new Intl.DateTimeFormat("pt-BR", { dateStyle: "short", timeStyle: "short" }).format(new Date(value));
}

export default function NewsSection({ news }: { news: NewsCache }) {
  const cardsBySource = new Map(news.cards.map((card) => [card.source, card]));
  return <section className="news-section">
    <div className="news-section-header"><div><div className="eyebrow">Radar econômico</div><h2>O que está movimentando a economia</h2><small>{formatDate(news.updatedAt)}</small></div><NewsRefreshButton /></div>
    <div className="news-grid">{newsSources.map((source) => {
      const card = cardsBySource.get(source.key);
      if (!card) return <article className={"news-card news-placeholder " + source.accent} key={source.key}><div className="news-card-media news-placeholder-media"><span>{source.shortName}</span></div><div className="news-card-body"><div className="news-source">{source.name}</div><h3>Notícia aguardando atualização</h3><p>O próximo job buscará o destaque econômico mais atual desta fonte.</p><a href={source.url} target="_blank" rel="noreferrer">Abrir fonte original ↗</a></div></article>;
      return <article className="news-card" key={source.key}>{card.imageUrl ? <img className="news-card-media" src={card.imageUrl} alt="" loading="lazy" referrerPolicy="no-referrer" /> : <div className={"news-card-media news-placeholder-media " + source.accent}><span>{source.shortName}</span></div>}<div className="news-card-body"><div className="news-meta"><span className="news-source">{source.name}</span>{card.aiGenerated && <span className="ai-badge">IA</span>}</div><h3>{card.title}</h3><p>{card.summary}</p><small>{card.publishedAt ? new Intl.DateTimeFormat("pt-BR", { dateStyle: "short", timeStyle: "short" }).format(new Date(card.publishedAt)) : "Data não informada"}</small><a href={card.url} target="_blank" rel="noreferrer">Ler na fonte original ↗</a></div></article>;
    })}</div>
    <p className="news-disclaimer">Os cards são informativos e direcionam para o conteúdo original de cada veículo. O COGME não reproduz as reportagens.</p>
  </section>;
}
