import { createDatabase, createTables, getMysqlConfig, loadLocalEnv } from "./db-config.mjs";

try {
  await loadLocalEnv();
  const config = getMysqlConfig();
  await createDatabase(config);
  await createTables(config);
  console.log("Banco " + config.databaseName + " e tabelas configurados com sucesso.");
} catch (error) {
  console.error("Não foi possível configurar o banco de dados.");
  console.error(error instanceof Error ? error.message : error);
  process.exitCode = 1;
}
