#!/bin/bash
set -euo pipefail

# Restore de banco de dados — COGME
# Restaura um dump PostgreSQL criado por backup_pre_deploy.sh.

if [ $# -lt 1 ]; then
    echo "Uso: $0 <arquivo.dump>"
    echo "Exemplo: $0 /backups/cogme/cogme_pre_deploy_20261122_100000.dump"
    exit 1
fi

BACKUP_FILE="${1}"
POSTGRES_USER="${POSTGRES_USER:-cogme}"
POSTGRES_DB="${POSTGRES_DB:-cogme}"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "ERRO: Arquivo não encontrado: $BACKUP_FILE"
    exit 1
fi

echo "=== COGME Restore de Banco ==="
echo "Arquivo: $BACKUP_FILE"
echo ""

# 1. Parar aplicação (manter DB rodando)
echo -n "1. Parando aplicação (back, front, proxy)... "
docker compose stop back front proxy 2>/dev/null
echo "OK"

# 2. Drop + Recreate DB
echo -n "2. Recriando banco de dados... "
docker compose exec -T db psql -U "$POSTGRES_USER" -c "DROP DATABASE IF EXISTS \"$POSTGRES_DB\"; CREATE DATABASE \"$POSTGRES_DB\";" 2>/dev/null
echo "OK"

# 3. Restore
echo -n "3. Restaurando dump... "
docker compose exec -T db pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Fc < "$BACKUP_FILE" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "OK"
else
    echo "FALHA"
    exit 1
fi

# 4. Subir aplicação
echo -n "4. Subindo aplicação... "
docker compose up -d back front proxy 2>/dev/null
echo "OK"

# 5. Aguardar health checks
echo -n "5. Aguardando health checks... "
for i in $(seq 1 30); do
    STATUS=$(docker compose ps --filter "status=running" | grep -qE "back.*healthy" && echo "ok" || echo "pending")
    if [ "$STATUS" = "ok" ]; then
        echo "OK (back healthy)"
        break
    fi
    sleep 2
done

# 6. Smoke tests
echo -n "6. Executando smoke tests... "
if command -v ./scripts/smoke_tests.sh >/dev/null 2>&1; then
    ./scripts/smoke_tests.sh
else
    echo "AVISO (scripts/smoke_tests.sh não encontrado)"
fi

echo ""
echo "Restore concluído com sucesso de: $BACKUP_FILE"
