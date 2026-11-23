#!/bin/bash
set -euo pipefail

# Backup pré-deploy — COGME
# Cria dump do PostgreSQL e backup de volumes Docker antes de um deploy.

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="${BACKUP_DIR:-/backups/cogme}"
mkdir -p "$BACKUP_DIR"

echo "=== COGME Backup Pré-Deploy ==="
echo "Timestamp: $TIMESTAMP"
echo "Diretório: $BACKUP_DIR"
echo ""

# 1. Dump PostgreSQL (custom format, compressed)
echo -n "1. Dump PostgreSQL... "
docker compose exec -T db pg_dump -U "${POSTGRES_USER:-cogme}" -d "${POSTGRES_DB:-cogme}" -Fc -Z9 > "$BACKUP_DIR/cogme_pre_deploy_${TIMESTAMP}.dump" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "OK ($BACKUP_DIR/cogme_pre_deploy_${TIMESTAMP}.dump)"
else
    echo "FALHA"
    exit 1
fi

# 2. Backup volumes Docker (opcional)
echo -n "2. Backup volume pgdata... "
docker run --rm -v cogme_pgdata:/data -v "$BACKUP_DIR":/backup alpine tar czf /backup/pgdata_${TIMESTAMP}.tar.gz -C /data . 2>/dev/null
if [ $? -eq 0 ]; then
    echo "OK ($BACKUP_DIR/pgdata_${TIMESTAMP}.tar.gz)"
else
    echo "AVISO (volume backup opcional falhou)"
fi

# 3. Retenção: manter últimos 30 backups
echo -n "3. Retenção (últimos 30 backups)... "
find "$BACKUP_DIR" -name "cogme_pre_deploy_*.dump" -mtime +30 -delete 2>/dev/null
find "$BACKUP_DIR" -name "pgdata_*.tar.gz" -mtime +30 -delete 2>/dev/null
echo "OK"

echo ""
echo "Backup concluído com sucesso."
echo "  Dump:  $BACKUP_DIR/cogme_pre_deploy_${TIMESTAMP}.dump"
echo "  Volume: $BACKUP_DIR/pgdata_${TIMESTAMP}.tar.gz"
