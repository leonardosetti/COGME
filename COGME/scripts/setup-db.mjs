import fs from "node:fs/promises";
import path from "node:path";
import mysql from "mysql2/promise";

async function loadLocalEnv() {
  const file = path.join(process.cwd(), ".env.local");
  try {
    const content = await fs.readFile(file, "utf8");
    for (const line of content.split(/\r?\n/)) {
      const match = line.match(/^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$/);
      if (!match || process.env[match[1]] !== undefined) continue;
      process.env[match[1]] = match[2].replace(/^['"]|['"]$/g, "");
    }
  } catch {
    // Variáveis de ambiente do sistema continuam sendo aceitas.
  }
}

await loadLocalEnv();

const host = process.env.MYSQL_HOST || "localhost";
const port = Number(process.env.MYSQL_PORT || 3306);
const user = process.env.MYSQL_USER || "root";
const password = process.env.MYSQL_PASSWORD;
const database = process.env.MYSQL_DATABASE || "cogme";

if (!password) throw new Error("Defina MYSQL_PASSWORD no .env.local antes de configurar o banco.");
if (!/^[A-Za-z0-9_$-]+$/.test(database)) throw new Error("MYSQL_DATABASE contém caracteres inválidos.");

const admin = await mysql.createConnection({ host, port, user, password });
await admin.query(
  "CREATE DATABASE IF NOT EXISTS " + database + " CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
);
await admin.end();

const connection = await mysql.createConnection({ host, port, user, password, database });
const schema = await fs.readFile(path.join(process.cwd(), "database", "schema.sql"), "utf8");
await connection.query(schema);
await connection.end();
console.log("Banco " + database + " e tabela simulations configurados com sucesso.");
