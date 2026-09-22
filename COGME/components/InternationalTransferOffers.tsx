type TransferPlatform = {
  name: string;
  label: string;
  description: string;
  highlights: string[];
  href: string;
  sourceLabel: string;
  featured?: boolean;
};

const platforms: TransferPlatform[] = [
  {
    name: "Wise",
    label: "Destaque em transparência",
    description: "Conta internacional e transferências para contas bancárias em outros países.",
    highlights: ["Câmbio comercial", "Tarifa exibida antes do envio", "Pagamento por Pix ou transferência"],
    href: "https://wise.com/br/compare/",
    sourceLabel: "Comparar oferta na Wise",
    featured: true,
  },
  {
    name: "Remessa Online",
    label: "Para enviar ou receber",
    description: "Plataforma digital para remessas internacionais de pessoas físicas e empresas.",
    highlights: ["Envio e recebimento", "Custo varia por operação e volume", "Possíveis tarifas externas e impostos"],
    href: "https://www.remessaonline.com.br/",
    sourceLabel: "Consultar oferta na Remessa",
  },
  {
    name: "Revolut",
    label: "Conta global",
    description: "Conta com várias moedas e transferências internacionais pelo aplicativo.",
    highlights: ["Taxas mostradas no app", "Transferências para mais de 130 países", "Opções bancárias e entre contas"],
    href: "https://www.revolut.com/pt-BR/money-transfer/",
    sourceLabel: "Consultar oferta na Revolut",
  },
  {
    name: "Western Union",
    label: "Rede internacional",
    description: "Envio online, pelo aplicativo ou em agentes, com recebimento em conta ou local físico.",
    highlights: ["Envio para mais de 200 países e territórios", "Conta bancária ou retirada", "Câmbio e tarifas variam por rota"],
    href: "https://www.westernunion.com/br/pt/transferenciais-internacionais.html",
    sourceLabel: "Consultar oferta na Western Union",
  },
];

export default function InternationalTransferOffers() {
  return <section className="surface-card offers-card">
    <div className="offers-heading">
      <div>
        <div className="eyebrow">Onde transferir</div>
        <h2>Compare as melhores opções para sua remessa</h2>
        <p className="subtle">Confira as condições atuais de plataformas digitais e escolha a que entrega o melhor valor final para o seu destino.</p>
      </div>
      <span className="offers-live-badge">Ofertas no site oficial</span>
    </div>
    <div className="offers-grid">{platforms.map((platform) => <article className={"offer-card" + (platform.featured ? " featured" : "")} key={platform.name}>
      <div className="offer-card-top"><div className="offer-brand">{platform.name}</div><span>{platform.label}</span></div>
      <p>{platform.description}</p>
      <ul>{platform.highlights.map((highlight) => <li key={highlight}>{highlight}</li>)}</ul>
      <a className="offer-link" href={platform.href} target="_blank" rel="noreferrer">{platform.sourceLabel} ↗</a>
    </article>)}</div>
    <p className="offers-disclaimer">Não existe uma vencedora universal: compare o valor que o beneficiário recebe, o custo total, o prazo, o IOF e as regras da operação antes de confirmar. A COGME não intermedeia nem executa a transferência. <a href="https://www.bcb.gov.br/estabilidadefinanceira/instituicoescambio" target="_blank" rel="noreferrer">Consulte as instituições habilitadas no BCB ↗</a></p>
  </section>;
}
