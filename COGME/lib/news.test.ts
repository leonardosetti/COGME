import { describe, expect, it } from "vitest";
import { isNewsCacheStale, NEWS_REFRESH_INTERVAL_MS, newsSources, parseSourceHtml } from "@/lib/news";

describe("parseSourceHtml", () => {
  it("extrai manchete, data e imagem de metadados HTML", () => {
    const source = newsSources[0];
    const html = '<html><head><meta property="og:image" content="/img/cnn.jpg"></head><body><a href="/economia/noticia-destaque">Mercado recebe novos dados de inflação nesta manhã</a><time datetime="2026-08-26T12:00:00Z"></time></body></html>';
    const [article] = parseSourceHtml(html, source);
    expect(article.title).toBe("Mercado recebe novos dados de inflação nesta manhã");
    expect(article.url).toContain("cnnbrasil.com.br/economia/noticia-destaque");
    expect(article.imageUrl).toContain("cnnbrasil.com.br/img/cnn.jpg");
  });

  it("ignora links de outros domínios", () => {
    const source = newsSources[1];
    const html = '<a href="https://example.com/noticia">Uma notícia econômica suficientemente longa para o teste</a>';
    expect(parseSourceHtml(html, source)).toHaveLength(0);
  });

  it("descarta datas futuras ou impossíveis", () => {
    const source = newsSources[0];
    const html = '<a href="/economia/noticia-futura">Mercado recebe novos dados de inflacao nesta manha</a><time datetime="2316-06-26T00:00:00Z"></time>';
    const [article] = parseSourceHtml(html, source);
    expect(article.publishedAt).toBeUndefined();
  });
});

describe("validade do cache de notícias", () => {
  const now = Date.parse("2026-08-27T12:00:00.000Z");

  it("considera vencido o cache sem data ou com 4 horas ou mais", () => {
    expect(isNewsCacheStale({ updatedAt: null }, now)).toBe(true);
    expect(isNewsCacheStale({ updatedAt: new Date(now - NEWS_REFRESH_INTERVAL_MS).toISOString() }, now)).toBe(true);
  });

  it("mantém válido o cache com menos de 4 horas", () => {
    expect(isNewsCacheStale({ updatedAt: new Date(now - NEWS_REFRESH_INTERVAL_MS + 1).toISOString() }, now)).toBe(false);
  });
});
