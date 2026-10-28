import { NextResponse } from "next/server";

const fallbackRates = { USD: 5.42, EUR: 6.08 } as const;
const supportedCurrencies = ["USD", "EUR"] as const;
type SupportedCurrency = (typeof supportedCurrencies)[number];

type BcbQuote = {
  cotacaoCompra?: number;
  cotacaoVenda?: number;
  dataHoraCotacao?: string;
  tipoBoletim?: string;
};

function isSupportedCurrency(value: string | null): value is SupportedCurrency {
  return supportedCurrencies.includes(value as SupportedCurrency);
}

function bcbDate(value: Date) {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Sao_Paulo",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(value);
  const values = Object.fromEntries(parts.map((part) => [part.type, part.value]));
  return values.month + "-" + values.day + "-" + values.year;
}

function quoteTimestamp(quote: BcbQuote) {
  return quote.dataHoraCotacao ? Date.parse(quote.dataHoraCotacao) || 0 : 0;
}

async function fetchBcbQuote(currency: SupportedCurrency) {
  const end = new Date();
  const start = new Date(end.getTime() - 7 * 24 * 60 * 60 * 1000);
  const endpoint = new URL(
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)",
  );
  endpoint.searchParams.set("@moeda", "'" + currency + "'");
  endpoint.searchParams.set("@dataInicial", "'" + bcbDate(start) + "'");
  endpoint.searchParams.set("@dataFinalCotacao", "'" + bcbDate(end) + "'");
  endpoint.searchParams.set("$format", "json");
  endpoint.searchParams.set("$top", "100");

  const response = await fetch(endpoint, {
    headers: { Accept: "application/json" },
    next: { revalidate: 300 },
    signal: AbortSignal.timeout(12000),
  });
  if (!response.ok) throw new Error("Banco Central respondeu HTTP " + response.status);

  const data = (await response.json()) as { value?: BcbQuote[] };
  const quotes = (data.value || []).filter((quote) =>
    Number.isFinite(quote.cotacaoVenda) || Number.isFinite(quote.cotacaoCompra),
  );
  const closingQuotes = quotes.filter((quote) => quote.tipoBoletim?.toLowerCase() === "fechamento");
  const candidates = closingQuotes.length ? closingQuotes : quotes;
  const quote = [...candidates].sort((first, second) => quoteTimestamp(second) - quoteTimestamp(first))[0];
  const rate = quote?.cotacaoVenda ?? quote?.cotacaoCompra;
  if (!quote || typeof rate !== "number" || !Number.isFinite(rate) || rate <= 0) throw new Error("Banco Central nao retornou uma cotacao valida.");

  return {
    rate,
    date: quote.dataHoraCotacao?.slice(0, 10),
    source: "Banco Central do Brasil (PTAX)",
  };
}

export async function GET(request: Request) {
  const currency = new URL(request.url).searchParams.get("currency");
  if (!isSupportedCurrency(currency)) return NextResponse.json({ error: "Moeda nao suportada." }, { status: 400 });
  try {
    const quote = await fetchBcbQuote(currency);
    return NextResponse.json({ currency, ...quote });
  } catch {
    return NextResponse.json({ currency, rate: fallbackRates[currency], source: "estimativa de contingência", fallback: true });
  }
}
