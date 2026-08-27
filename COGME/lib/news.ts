export type NewsSourceKey = "cnn" | "uol" | "g1" | "record";

export type NewsSource = {
  key: NewsSourceKey;
  name: string;
  shortName: string;
  url: string;
  host: string;
  accent: string;
};

export type CollectedArticle = {
  source: NewsSourceKey;
  title: string;
  description: string;
  url: string;
  imageUrl?: string;
  publishedAt?: string;
};

export type NewsCard = CollectedArticle & {
  sourceName: string;
  sourceUrl: string;
  summary: string;
  fetchedAt: string;
  aiGenerated: boolean;
};

export type NewsCache = {
  updatedAt: string | null;
  cards: NewsCard[];
};

export const NEWS_REFRESH_INTERVAL_MS = 4 * 60 * 60 * 1000;

export function isNewsCacheStale(cache: Pick<NewsCache, "updatedAt">, now = Date.now()) {
  if (!cache.updatedAt) return true;
  const updatedAt = Date.parse(cache.updatedAt);
  return Number.isNaN(updatedAt) || now - updatedAt >= NEWS_REFRESH_INTERVAL_MS;
}

export const newsSources: readonly NewsSource[] = [
  { key: "cnn", name: "CNN Brasil", shortName: "CNN", url: "https://www.cnnbrasil.com.br/economia/", host: "cnnbrasil.com.br", accent: "cnn" },
  { key: "uol", name: "UOL Economia", shortName: "UOL", url: "https://economia.uol.com.br/", host: "economia.uol.com.br", accent: "uol" },
  { key: "g1", name: "G1 Economia", shortName: "g1", url: "https://g1.globo.com/economia/", host: "g1.globo.com", accent: "g1" },
  { key: "record", name: "Record / R7 Economia", shortName: "R7", url: "https://noticias.r7.com/economia/", host: "noticias.r7.com", accent: "record" },
];

const economyKeywords = [
  "economia", "mercado", "dólar", "dolar", "euro", "juros", "inflação", "inflacao", "pib",
  "lucro", "empresa", "investimento", "bolsa", "petróleo", "petroleo", "imposto", "salário",
  "salario", "crédito", "credito", "taxa", "comércio", "comercio", "emprego", "banco",
  "energia", "agronegócio", "agronegocio", "varejo", "produção", "producao",
];

const entityMap: Record<string, string> = {
  "&amp;": "&", "&quot;": "\"", "&#39;": "'", "&apos;": "'", "&lt;": "<", "&gt;": ">",
  "&nbsp;": " ", "&ldquo;": "“", "&rdquo;": "”", "&ndash;": "–", "&mdash;": "—",
};

function decodeEntities(value: string) {
  return value
    .replace(/&(amp|quot|#39|apos|lt|gt|nbsp|ldquo|rdquo|ndash|mdash);/gi, (entity) => entityMap[entity.toLowerCase()] || entity)
    .replace(/&#(\d+);/g, (_, code: string) => String.fromCodePoint(Number(code)));
}

function cleanText(value: string) {
  return decodeEntities(value.replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim());
}

function normalizeUrl(value: string, baseUrl: string) {
  try {
    const url = new URL(decodeEntities(value), baseUrl);
    if (url.protocol !== "http:" && url.protocol !== "https:") return null;
    return url.toString();
  } catch {
    return null;
  }
}

function hostMatches(url: string, source: NewsSource) {
  try {
    const host = new URL(url).hostname.replace(/^www\./, "");
    return host === source.host || host.endsWith("." + source.host);
  } catch {
    return false;
  }
}

function imageValue(value: unknown): string | undefined {
  if (typeof value === "string") return value;
  if (Array.isArray(value)) return imageValue(value[0]);
  if (value && typeof value === "object") {
    const record = value as Record<string, unknown>;
    return imageValue(record.url || record.contentUrl);
  }
  return undefined;
}

function parseDate(value: string | undefined) {
  if (!value) return undefined;
  const timestamp = Date.parse(value);
  if (!Number.isNaN(timestamp)) return new Date(timestamp).toISOString();
  const match = value.match(/(\d{2})[/-](\d{2})[/-](\d{4})(?:[^\d]+(\d{1,2}):(\d{2}))?/);
  if (!match) return undefined;
  const date = new Date(Date.UTC(Number(match[3]), Number(match[2]) - 1, Number(match[1]), Number(match[4] || 0), Number(match[5] || 0)));
  return date.toISOString();
}

function nearbyDate(context: string) {
  const datetime = context.match(/datetime\s*=\s*["']([^"']+)["']/i)?.[1];
  return parseDate(datetime || context);
}

function nearbyImage(context: string, baseUrl: string) {
  const image = context.match(/(?:src|data-src|data-lazy-src|data-original)\s*=\s*["']([^"']+)["']/i)?.[1] ||
    context.match(/srcset\s*=\s*["']([^"']+)["']/i)?.[1]?.split(",")[0]?.trim().split(" ")[0];
  return image ? normalizeUrl(image, baseUrl) || undefined : undefined;
}

function isUsableTitle(title: string) {
  return title.length >= 24 && title.length <= 220 &&
    !/^(leia mais|veja mais|menu|economia|últimas notícias|ultimas noticias)$/i.test(title);
}

export function parseSourceHtml(html: string, source: NewsSource): CollectedArticle[] {
  const candidates: CollectedArticle[] = [];
  const seen = new Set<string>();
  const add = (candidate: CollectedArticle) => {
    const key = candidate.url || candidate.title.toLowerCase();
    if (!isUsableTitle(candidate.title) || seen.has(key) || !hostMatches(candidate.url, source)) return;
    seen.add(key);
    candidates.push(candidate);
  };

  const jsonLdPattern = /<script[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;
  let jsonLdMatch: RegExpExecArray | null;
  while ((jsonLdMatch = jsonLdPattern.exec(html))) {
    try {
      const walk = (value: unknown) => {
        if (Array.isArray(value)) { value.forEach(walk); return; }
        if (!value || typeof value !== "object") return;
        const record = value as Record<string, unknown>;
        const title = typeof record.headline === "string" ? cleanText(record.headline) : "";
        const url = typeof record.url === "string" ? normalizeUrl(record.url, source.url) : null;
        if (title && url) add({
          source: source.key,
          title,
          description: typeof record.description === "string" ? cleanText(record.description).slice(0, 420) : "",
          url,
          imageUrl: imageValue(record.image) ? normalizeUrl(imageValue(record.image) as string, source.url) || undefined : undefined,
          publishedAt: parseDate(typeof record.datePublished === "string" ? record.datePublished : typeof record.dateModified === "string" ? record.dateModified : undefined),
        });
        Object.values(record).forEach(walk);
      };
      walk(JSON.parse(jsonLdMatch[1]));
    } catch {
      // Alguns portais incluem JSON-LD inválido; os links HTML continuam sendo processados.
    }
  }

  const anchorPattern = /<a\b([^>]*\bhref\s*=\s*["']([^"']+)["'][^>]*)>([\s\S]*?)<\/a>/gi;
  let anchorMatch: RegExpExecArray | null;
  while ((anchorMatch = anchorPattern.exec(html))) {
    const url = normalizeUrl(anchorMatch[2], source.url);
    const title = cleanText(anchorMatch[3]);
    if (!url || !isUsableTitle(title) || !hostMatches(url, source)) continue;
    const context = html.slice(Math.max(0, anchorMatch.index - 800), Math.min(html.length, anchorMatch.index + anchorMatch[0].length + 800));
    add({ source: source.key, title, description: "", url, imageUrl: nearbyImage(context, source.url), publishedAt: nearbyDate(context) });
  }

  const fallbackImage = html.match(/<meta[^>]+property=[\"']og:image[\"'][^>]+content=[\"']([^\"']+)[\"']/i)?.[1];
  const validFallbackImage = fallbackImage ? normalizeUrl(fallbackImage, source.url) || undefined : undefined;
  return candidates
    .map((article) => ({ ...article, imageUrl: article.imageUrl || validFallbackImage }))
    .filter((article) => !article.publishedAt || Date.now() - Date.parse(article.publishedAt) < 1000 * 60 * 60 * 24 * 10)
    .sort((first, second) => (Date.parse(second.publishedAt || "") || 0) - (Date.parse(first.publishedAt || "") || 0) || Number(economyKeywords.some((word) => second.title.toLowerCase().includes(word))) - Number(economyKeywords.some((word) => first.title.toLowerCase().includes(word))))
    .slice(0, 8);
}

async function collectSource(source: NewsSource) {
  const response = await fetch(source.url, {
    headers: { "User-Agent": "COGME-NewsBot/1.0 (+https://cogme.local)", Accept: "text/html,application/xhtml+xml" },
    signal: AbortSignal.timeout(12000),
  });
  if (!response.ok) throw new Error(source.name + " respondeu HTTP " + response.status);
  return parseSourceHtml((await response.text()).slice(0, 3_000_000), source);
}

type SourceStatus = { source: NewsSourceKey; name: string; count: number; error?: string };

async function collectAll() {
  const results = await Promise.all(newsSources.map(async (source): Promise<{ source: NewsSource; articles: CollectedArticle[]; status: SourceStatus }> => {
    try {
      const articles = await collectSource(source);
      return { source, articles, status: { source: source.key, name: source.name, count: articles.length } };
    } catch (error) {
      return {
        source,
        articles: [],
        status: { source: source.key, name: source.name, count: 0, error: error instanceof Error ? error.message : "falha desconhecida" },
      };
    }
  }));
  return results;
}

function fallbackSummary(article: CollectedArticle) {
  return article.description || "Confira os principais detalhes e os impactos econômicos diretamente na reportagem original.";
}

type OpenRouterResponse = {
  choices?: Array<{ message?: { content?: string | Array<{ type?: string; text?: string }> } }>;
};

type OpenRouterModelConfig = {
  model: string;
  apiKey: string;
};

function responseText(content: string | Array<{ type?: string; text?: string }> | undefined) {
  if (typeof content === "string") return content;
  return content?.map((part) => part.text || "").join("") || "";
}

function configuredModels(): OpenRouterModelConfig[] {
  const candidates = [
    {
      model: process.env.OPENROUTER_MODEL || "nvidia/nemotron-3.5-lightning:free",
      apiKey: process.env.OPENROUTER_API_KEY,
    },
    {
      model: process.env.OPENROUTER_FALLBACK_MODEL || "dots-studio/dots-3-note-preview:free",
      apiKey: process.env.OPENROUTER_FALLBACK_API_KEY,
    },
    {
      model: process.env.OPENROUTER_RESERVE_MODEL || "poolside/laguna-s-2.1:free",
      apiKey: process.env.OPENROUTER_RESERVE_API_KEY,
    },
  ];

  return candidates.filter((candidate): candidate is OpenRouterModelConfig => Boolean(candidate.apiKey));
}

async function summarizeWithModel(articles: CollectedArticle[], config: OpenRouterModelConfig) {
  const input = articles.map((article) => ({
    source: article.source,
    title: article.title,
    url: article.url,
    publishedAt: article.publishedAt || null,
    description: article.description,
  }));
  const prompt = [
    "Você é editor de economia do COGME.",
    "Escolha no máximo uma notícia mais relevante e atual de cada fonte. Resuma cada escolhida em português brasileiro, em 1 ou 2 frases, sem opinião, sem inventar dados e sem repetir o título.",
    "Use exclusivamente os itens recebidos. Não altere URLs. Retorne somente JSON válido no formato {\"cards\":[{\"source\":\"cnn|uol|g1|record\",\"articleUrl\":\"URL_EXATA_RECEBIDA\",\"summary\":\"resumo\"}]} .",
    JSON.stringify(input),
  ].join("\n");
  const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      Authorization: "Bearer " + config.apiKey,
      "Content-Type": "application/json",
      "HTTP-Referer": process.env.PUBLIC_SITE_URL || "http://localhost:3000",
      "X-OpenRouter-Title": "COGME Notícias Econômicas",
    },
    body: JSON.stringify({
      model: config.model,
      messages: [
        { role: "system", content: "Você produz resumos factuais curtos e sempre obedece ao JSON solicitado." },
        { role: "user", content: prompt },
      ],
      temperature: 0.2,
      max_tokens: 1800,
    }),
    signal: AbortSignal.timeout(45000),
  });
  if (!response.ok) throw new Error("OpenRouter respondeu HTTP " + response.status);
  const payload = (await response.json()) as OpenRouterResponse;
  const text = responseText(payload.choices?.[0]?.message?.content)
    .replace(/^\x60{3}(?:json)?\s*/i, "")
    .replace(/\s*\x60{3}$/i, "");
  const start = text.indexOf("{");
  const end = text.lastIndexOf("}");
  if (start < 0 || end <= start) throw new Error("A LLM não retornou JSON.");
  const parsed = JSON.parse(text.slice(start, end + 1)) as {
    cards?: Array<{ source?: string; articleUrl?: string; url?: string; summary?: string }>;
  };
  const byUrl = new Map(articles.map((article) => [article.url, article]));
  const summaries = new Map<string, string>();
  for (const card of parsed.cards || []) {
    const article = card.articleUrl ? byUrl.get(card.articleUrl) : card.url ? byUrl.get(card.url) : undefined;
    if (!article || article.source !== card.source || typeof card.summary !== "string") continue;
    const summary = cleanText(card.summary).slice(0, 420);
    if (summary.length >= 40) summaries.set(article.url, summary);
  }
  return summaries;
}

async function summarizeWithFallbacks(articles: CollectedArticle[]) {
  let lastError: unknown;
  for (const config of configuredModels()) {
    try {
      return await summarizeWithModel(articles, config);
    } catch (error) {
      lastError = error;
    }
  }
  if (lastError) throw lastError;
  return new Map<string, string>();
}

export async function refreshNews() {
  const results = await collectAll();
  const articles = results.flatMap((result) => result.articles);
  let summaries = new Map<string, string>();
  let aiGenerated = false;
  if (articles.length && configuredModels().length) {
    try {
      summaries = await summarizeWithFallbacks(articles);
      aiGenerated = summaries.size > 0;
    } catch {
      // Uma falha da LLM não apaga as manchetes coletadas; o fallback mantém o job útil.
    }
  }
  const fetchedAt = new Date().toISOString();
  const cards = newsSources.flatMap((source) => {
    const article = results.find((result) => result.source.key === source.key)?.articles[0];
    if (!article) return [];
    return [{
      ...article,
      sourceName: source.name,
      sourceUrl: source.url,
      summary: summaries.get(article.url) || fallbackSummary(article),
      fetchedAt,
      aiGenerated: summaries.has(article.url),
    }];
  });
  return { cache: { updatedAt: fetchedAt, cards }, statuses: results.map((result) => result.status), aiGenerated };
}
