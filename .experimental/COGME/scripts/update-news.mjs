const baseUrl = process.env.NEWS_JOB_URL || "http://localhost:3000";
const secret = process.env.NEWS_JOB_SECRET;

if (!secret) {
  throw new Error("Defina NEWS_JOB_SECRET antes de executar o job.");
}

const response = await fetch(new URL("/api/news/update", baseUrl), {
  method: "POST",
  headers: { Authorization: "Bearer " + secret },
});
const body = await response.json();
if (!response.ok) throw new Error(body.error || "O job de notícias falhou.");
console.log(JSON.stringify(body, null, 2));
