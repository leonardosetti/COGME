import mysql, { type Pool } from "mysql2/promise";

const globalForDatabase = globalThis as unknown as { cogmePool?: Pool };

function databasePool() {
  if (globalForDatabase.cogmePool) return globalForDatabase.cogmePool;

  const pool = mysql.createPool({
    host: process.env.MYSQL_HOST || "localhost",
    port: Number(process.env.MYSQL_PORT || 3306),
    user: process.env.MYSQL_USER || "root",
    password: process.env.MYSQL_PASSWORD,
    database: process.env.MYSQL_DATABASE || "cogme",
    waitForConnections: true,
    connectionLimit: Number(process.env.MYSQL_CONNECTION_LIMIT || 10),
    maxIdle: 10,
    idleTimeout: 60000,
    enableKeepAlive: true,
  });

  if (process.env.NODE_ENV !== "production") globalForDatabase.cogmePool = pool;
  return pool;
}

export const db = databasePool();
