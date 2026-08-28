import { createTables, getMysqlConfig, loadLocalEnv } from "./db-config.mjs";

try {
  await loadLocalEnv();
  const config = getMysqlConfig();
  await createTables(config);
  console.log("Tabelas do COGME criadas ou já existentes no banco " + config.databaseName + ".");
} catch (error) {
  console.error("Não foi possível criar as tabelas.");
  console.error(error instanceof Error ? error.message : error);
  console.error("Verifique se o banco existe e se as variáveis MYSQL_* estão configuradas.");
  process.exitCode = 1;
}
