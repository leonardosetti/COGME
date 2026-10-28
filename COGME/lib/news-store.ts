import fs from "node:fs/promises";
import path from "node:path";
import { refreshNews, isNewsCacheStale, type NewsCache } from "@/lib/news";

function cacheFile() {
  return path.join(process.cwd(), "data", "news.json");
}

export async function readNewsCache(): Promise<NewsCache> {
  try {
    const content = await fs.readFile(cacheFile(), "utf8");
    const parsed = JSON.parse(content) as Partial<NewsCache>;
    return {
      updatedAt: typeof parsed.updatedAt === "string" ? parsed.updatedAt : null,
      cards: Array.isArray(parsed.cards) ? parsed.cards : [],
    };
  } catch {
    return { updatedAt: null, cards: [] };
  }
}

export async function writeNewsCache(cache: NewsCache) {
  const file = cacheFile();
  await fs.mkdir(path.dirname(file), { recursive: true });
  const temporaryFile = file + ".tmp";
  await fs.writeFile(temporaryFile, JSON.stringify(cache, null, 2), "utf8");
  await fs.rename(temporaryFile, file);
}

let refreshInFlight: Promise<NewsCache> | null = null;

export async function refreshNewsIfStale() {
  const existing = await readNewsCache();
  if (!isNewsCacheStale(existing)) return existing;

  if (!refreshInFlight) {
    refreshInFlight = refreshNews()
      .then(async (result) => {
        await writeNewsCache(result.cache);
        return result.cache;
      })
      .finally(() => {
        refreshInFlight = null;
      });
  }

  try {
    return await refreshInFlight;
  } catch {
    return existing;
  }
}
