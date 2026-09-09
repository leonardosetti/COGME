import fs from "node:fs/promises";
import path from "node:path";
import mysql from "mysql2/promise";

const DATABASE_NAME_PATTERN = /^[A-Za-z0-9_$-]+$/;

export async function loadLocalEnv() {
  // .env.local tem precedência sobre .env, e variáveis do sistema têm
  // precedência sobre os dois arquivos.
  for (const filename of [".env", ".env.local"]) {
    const file = path.join(process.cwd(), filename);

    try {
      const content = await fs.readFile(file, "utf8");
      for (const line of content.split(/\r?\n/)) {
        const match = line.match(/^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$/);
        if (!match || process.env[match[1]] !== undefined) continue;

        let value = match[2].trim();
        if ((value.startsWith("\"") && value.endsWith("\"")) || (value.startsWith("'") && value.endsWith("'"))) {
          value = value.slice(1, -1);
        }
        process.env[match[1]] = value;
      }
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
    }
  }
}

export function getMysqlConfig({ withDatabase = true } = {}) {
  const port = Number(process.env.MYSQL_PORT || 3306);
  if (!Number.isInteger(port) || port < 1 || port > 65535) {
    throw new Error("MYSQL_PORT precisa ser um número entre 1 e 65535.");
  }

  const database = process.env.MYSQL_DATABASE || "cogme";
  if (!DATABASE_NAME_PATTERN.test(database)) {
    throw new Error("MYSQL_DATABASE contém caracteres inválidos.");
  }

  return {
    host: process.env.MYSQL_HOST || "localhost",
    port,
    user: process.env.MYSQL_USER || "root",
    password: process.env.MYSQL_PASSWORD ?? "",
    ...(withDatabase ? { database } : {}),
    databaseName: database,
  };
}

function connectionOptions(config, withDatabase = true) {
  const { databaseName: _databaseName, ...options } = config;
  if (!withDatabase) delete options.database;
  return options;
}

export async function createDatabase(config) {
  const admin = await mysql.createConnection(connectionOptions(config, false));
  try {
    await admin.query(
      "CREATE DATABASE IF NOT EXISTS " +
        quoteIdentifier(config.databaseName) +
        " CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
    );
  } finally {
    await admin.end();
  }
}

export async function createTables(config) {
  const schemaPath = path.join(process.cwd(), "database", "schema.sql");
  const schema = await fs.readFile(schemaPath, "utf8");
  const connection = await mysql.createConnection({
    ...connectionOptions(config),
    // O schema pode conter mais de uma instrução; o arquivo é local e versionado.
    multipleStatements: true,
  });

  try {
    await connection.query(schema);
  } finally {
    await connection.end();
  }
}

export function quoteIdentifier(identifier) {
  return "`" + identifier.replace(/`/g, "``") + "`";
}
