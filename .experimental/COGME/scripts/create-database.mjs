import { createDatabase, getMysqlConfig, loadLocalEnv } from "./db-config.mjs";

try {
  await loadLocalEnv();
  const config = getMysqlConfig({ withDatabase: false });
  await createDatabase(config);
  console.log("Banco " + config.databaseName + " criado ou já existente.");
} catch (error) {
  console.error("Não foi possível criar o banco de dados.");
  console.error(error instanceof Error ? error.message : error);
  process.exitCode = 1;
}
