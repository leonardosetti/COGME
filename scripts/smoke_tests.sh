#!/bin/bash
set -euo pipefail

# Smoke tests pós-deploy — COGME
# Retorna exit code 0 se todos passam, não-zero se algum falha.

BASE_URL="${BASE_URL:-http://localhost:8080}"
FAILURES=0

echo "=== COGME Smoke Tests ==="
echo "Base URL: $BASE_URL"
echo ""

# 1. Health Check API
echo -n "1. Health Check API... "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$BASE_URL/health" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "PASS (HTTP 200)"
else
    echo "FAIL (HTTP $HTTP_CODE)"
    FAILURES=$((FAILURES + 1))
fi

# 2. Health Check DB
echo -n "2. Health Check DB... "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$BASE_URL/health/db" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "PASS (HTTP 200)"
else
    echo "FAIL (HTTP $HTTP_CODE)"
    FAILURES=$((FAILURES + 1))
fi

# 3. Rate API (USD)
echo -n "3. Rate API (USD)... "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "$BASE_URL/v1/rates/USD" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "PASS (HTTP 200)"
else
    echo "FAIL (HTTP $HTTP_CODE)"
    FAILURES=$((FAILURES + 1))
fi

# 4. Simulate Endpoint
echo -n "4. Simulate Endpoint... "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 -X POST -d '{"amount":1000,"currency":"USD"}' "$BASE_URL/v1/simulate" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "PASS (HTTP 200)"
else
    echo "FAIL (HTTP $HTTP_CODE)"
    FAILURES=$((FAILURES + 1))
fi

# 5. Frontend Carrega
echo -n "5. Frontend Carrega... "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$BASE_URL/" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "PASS (HTTP 200)"
else
    echo "FAIL (HTTP $HTTP_CODE)"
    FAILURES=$((FAILURES + 1))
fi

# 6. Invoice PDF
echo -n "6. Invoice PDF... "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 30 -X POST "$BASE_URL/v1/invoice" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "PASS (HTTP 200)"
else
    echo "FAIL (HTTP $HTTP_CODE)"
    FAILURES=$((FAILURES + 1))
fi

echo ""
echo "=== Resultado: $FAILURES falha(s) ==="

if [ "$FAILURES" -eq 0 ]; then
    echo "Todos os smoke tests passaram."
    exit 0
else
    echo "Alguns smoke tests falharam."
    exit 1
fi
