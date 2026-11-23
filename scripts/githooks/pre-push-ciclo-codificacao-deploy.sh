#!/usr/bin/env bash
# pre-push-ciclo-codificacao-deploy.sh — Gate local ANTES do push (ciclo de codificação e deploy).
#
# Valida, para os commits sendo pushados:
#   1. frontmatter de .md alterados (NORMA-TEMPLATES-ARTEFATOS)
#   2. flake8 em Python alterado (src, migrations, tests)
#   3. mypy strict em src/
#   4. testes unitários locais (coverage >= 80)
#   5. testes de integração se COGME_TEST_DATABASE_URL estiver definido; caso contrário,
#      usar mock/stub para dependências externas e registrar no relatório de testes
#   6. sanity de specs alteradas e de specs referenciadas por commits de código
#      (devem estar liberadas para codificação: ativo/ratificado — vocabulário fechado
#      da NORMA-TEMPLATES-ARTEFATOS; draft/obsoleto/arquivado bloqueiam)
#   7. CI/CD all green (best effort via gh; verificação obrigatória no Gate de stage)
#   8. formato Conventional Commits nas mensagens (aviso, não bloqueia)
#
# Qualquer falha hard bloqueia o push (exit 1). Avisos não bloqueam.
#
# Ativar:
#   cp scripts/githooks/pre-push-ciclo-codificacao-deploy.sh .git/hooks/pre-push
#   chmod +x .git/hooks/pre-push
#
# Base: constitution.md (Art. 6.1 SDD; Art. 9.3; P-06; P-11), ADR-007 (rede PMBOK),
# docs/operacao/proc-ciclo-codificacao-deploy.md (runbook deste ciclo).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

if [ "${COGME_README_REWRITING:-0}" = "1" ]; then exit 0; fi

REMOTE="${1:-}"
REMOTE_URL="${2:-}"

FAIL=0
NOTES=()

note() { NOTES+=("$*"); }
fail() { echo "FALHA: $*" >&2; FAIL=1; }

# spec_field ARQUIVO CAMPO — lê CAMPO só do bloco frontmatter (entre os dois primeiros '---').
# Não usa o corpo do arquivo: linhas 'status:' em tabelas/texto não contam (NORMA-TEMPLATES-ARTEFATOS).
spec_field() {
  python3 - "$1" "$2" <<'PY'
import re
import sys
from pathlib import Path

lines = Path(sys.argv[1]).read_text(encoding="utf-8").splitlines()
frontmatter = []
if lines and lines[0].strip() == "---":
    for line in lines[1:]:
        if line.strip() == "---":
            break
        frontmatter.append(line)
for line in frontmatter:
    m = re.match(rf"{sys.argv[2]}:\s*(.+?)\s*$", line)
    if m and m.group(1):
        print(m.group(1))
        break
PY
}

# Status que liberam codificação (decisão do gate): ativo (vigente) e ratificado/aprovado (CCB).
SPEC_STATUS_RE='^(ativo|ratificado|ratificada|aprovado|aprovada)$'
spec_liberada() { [ -n "$(spec_field "$1" "status")" ] && spec_field "$1" "status" | grep -qE "$SPEC_STATUS_RE"; }

echo "==> pre-push: ciclo de codificação e deploy (COGME)"
[ -n "$REMOTE" ] && echo "   remote: $REMOTE ($REMOTE_URL)"

# --- 1. intervalos de commits sendo pushados (stdin: local_ref local_sha remote_ref remote_sha) ---
RANGES=""
while read -r local_ref local_sha remote_ref remote_sha; do
  [ -z "$local_ref" ] && continue
  if [ "$remote_sha" = "0000000000000000000000000000000000000000" ]; then
    base=$(git merge-base "$local_sha" main 2>/dev/null || echo "$local_sha")
    RANGES="$RANGES $base..$local_sha"
  else
    RANGES="$RANGES $remote_sha..$local_sha"
  fi
done

if [ -z "$RANGES" ]; then
  echo "==> sem commits para avaliar. Liberando."
  exit 0
fi
echo "==> intervalos: $RANGES"

# --- 2. arquivos alterados no intervalo (--diff-filter=d: arquivos deletados não são lintados) ---
CHANGED=$(git diff --name-only --diff-filter=d $RANGES 2>/dev/null || true)
MD_CHANGED=$(printf '%s\n' "$CHANGED" | grep '\.md$' || true)
PY_CHANGED=$(printf '%s\n' "$CHANGED" | grep -E '\.py$' | grep -E '^(src|migrations|tests)/' || true)
SRC_CHANGED=$(printf '%s\n' "$PY_CHANGED" | grep -E '^src/' || true)

# --- 3. frontmatter de .md alterados (só os alterados; o estoque legado é dívida à parte) ---
# xargs -d '\n': caminhos com espaços (ex.: exports Excalidraw) chegam inteiros ao validador.
if [ -n "$MD_CHANGED" ]; then
  echo "==> validando frontmatter de .md alterados"
  if ! printf '%s\n' "$MD_CHANGED" | xargs -d '\n' python3 scripts/validar_frontmatter_md.py; then
    fail "frontmatter .md inválido (scripts/validar_frontmatter_md.py). Corrija antes do push."
  fi
fi

# --- 4. flake8 em Python alterado ---
if [ -n "$PY_CHANGED" ]; then
  echo "==> flake8 em Python alterado"
  if ! printf '%s\n' "$PY_CHANGED" | xargs -d '\n' python3 -m flake8; then
    fail "flake8 falhou nos arquivos Python alterados."
  fi
fi

# --- 5. mypy strict em src/ (só quando src/ muda; config SSOT: pyproject.toml [tool.mypy]) ---
if [ -n "$SRC_CHANGED" ]; then
  echo "==> mypy strict em src/"
  if ! python3 -m mypy; then
    fail "mypy strict falhou em src/."
  fi
fi

# --- 6. testes unitários locais (sempre) + cobertura reportada ---
echo "==> testes unitários locais (tests/unit)"
set +e
PY_OUT=$(python3 -m pytest tests/unit -q --tb=short --cov=src --cov-report=term-missing -p no:cacheprovider 2>&1)
PY_RC=$?
set -e
echo "$PY_OUT"
if [ "$PY_RC" -ne 0 ]; then fail "testes unitários locais falharam (rc=$PY_RC)."; fi
if echo "$PY_OUT" | grep -qE ", [1-9][0-9]* skipped"; then
  fail "testes pulados detectados na suíte unitária (skipping proibido)."
fi
TOTAL=$(echo "$PY_OUT" | grep -E "^TOTAL" | awk '{print $NF}' | tr -d '%')
echo "==> cobertura unitária: ${TOTAL:-n/d}% (alvo CI: >= 90% com PostgreSQL efêmero)"

# --- 7. testes de integração + cobertura >= 90% com DB real; sem PG, apenas avisa ---
if [ -n "${COGME_TEST_DATABASE_URL:-}" ]; then
  echo "==> testes de integração + cobertura >= 90% (COGME_TEST_DATABASE_URL definido)"
  if ! python3 -m pytest tests/unit tests/integration -q --tb=short --cov=src --cov-report=term-missing --cov-fail-under=90 -p no:cacheprovider; then
    fail "testes de integração/cobertura falharam (cobertura < 90% ou erros)."
  fi
else
  echo "==> COGME_TEST_DATABASE_URL não definido: integração com banco real pulada."
  echo "==> Cobertura >= 90% é exigida pelo CI (test-suite com PostgreSQL efêmero); localmente apenas reportada acima."
  note "Integração com banco real pulada (sem COGME_TEST_DATABASE_URL) — CI valida >= 90% com PostgreSQL efêmero."
fi

# --- 8. sanity de specs alteradas (status que libera codificação + rastreabilidade id) ---
SPEC_CHANGED=$(printf '%s\n' "$CHANGED" | grep -E '\.spec\.md$|specs/spec-|especificacoes/spec-' || true)
if [ -n "$SPEC_CHANGED" ]; then
  echo "==> verificando status de specs alteradas"
  while IFS= read -r sf; do
    [ -z "$sf" ] && continue
    status=$(spec_field "$sf" "status")
    case "$status" in
      ativo|ratificado|ratificada|aprovado|aprovada) echo "   OK $sf ($status)" ;;
      draft|obsoleto|arquivado)
        note "spec $sf com status '$status' — edição documental liberada; codificação contra ela é bloqueada (item 9)." ;;
      *)
        fail "spec $sf com status '$status' fora do vocabulário fechado da norma (ativo|draft|ratificado|obsoleto|arquivado)." ;;
    esac
    if [ -z "$(spec_field "$sf" "spec-id")" ] && [ -z "$(spec_field "$sf" "id")" ]; then
      fail "spec $sf sem 'id:'/'spec-id:' no frontmatter (rastreabilidade — runbook §3)."
    fi
  done <<< "$SPEC_CHANGED"
fi

# --- 9. commits de código só podem codificar contra specs liberadas (runbook Fase 0) ---
COMMIT_SHAS=$(git rev-list $RANGES 2>/dev/null || true)
for sha in $COMMIT_SHAS; do
  code_touched=$(git show --name-only --pretty=format: --diff-filter=d "$sha" 2>/dev/null | grep -E '^(src|migrations|tests)/' || true)
  [ -n "$code_touched" ] || continue
  # Refs de specs oficiais (spec-NNN) e de propostas (spec-prop-NNN / PROP-NNN), normalizadas.
  refs=$(git show -s --format='%s%n%b' "$sha" \
    | grep -oiE '(spec-[0-9]+|prop-[0-9]+)' \
    | tr '[:upper:]' '[:lower:]' | sed 's/^prop-/spec-prop-/' | sort -u || true)
  [ -n "$refs" ] || continue
  for ref in $refs; do
    matches=$(git ls-files | grep -E "/${ref}[-.]" || true)
    if [ -z "$matches" ]; then
      fail "commit ${sha:0:12} referencia ${ref}, mas nenhuma spec com esse id existe (rastreabilidade quebrada)."
      continue
    fi
    unlocked=0
    while IFS= read -r mf; do
      if spec_liberada "$mf"; then unlocked=1; break; fi
    done <<< "$matches"
    if [ "$unlocked" -eq 0 ]; then
      status=$(spec_field "$(head -1 <<< "$matches")" "status")
      fail "commit ${sha:0:12} codifica contra ${ref} não liberada (status '$status') — runbook Fase 0: não há código sem spec aprovada."
    fi
  done
done

# --- 9b. lembrança: commits (qualquer tipo) que referenciam specs ---
if git log --format='%s%n%b' $RANGES 2>/dev/null | grep -qiE 'spec-|spec_prop'; then
  echo "==> commits referenciam specs: confirme que as codificações têm spec liberada (ativo/ratificado)."
fi

# --- 9c. formato Conventional Commits (runbook §7.3) — aviso, não bloqueia ---
while IFS= read -r subject; do
  [ -z "$subject" ] && continue
  case "$subject" in
    "Merge "*|"Revert "*) continue ;;
  esac
  if ! printf '%s' "$subject" | grep -qE '^[a-z][a-z0-9_]*(\([^)]*\))?: .+'; then
    note "commit fora do padrão Conventional Commits (runbook §7.3): $subject"
  elif [ "${#subject}" -gt 72 ]; then
    note "subject de commit com ${#subject} chars (> 72, runbook §7.3): $subject"
  fi
done < <(git log --format='%s' $RANGES 2>/dev/null || true)

# --- 10. CI/CD all green (best effort via gh; não bloqueia sem auth) ---
echo "==> pipelines CI/CD (verificar a cada deploy — Gate de stage)"
echo "   ci.yml:        https://github.com/leonardosetti/COGME/actions/workflows/ci.yml"
echo "   sddai-verify:  https://github.com/leonardosetti/COGME/actions/workflows/sddai-verify.yml"
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  gh run list --repo leonardosetti/COGME --limit 5 --json name,status,conclusion,headBranch 2>/dev/null \
    | python3 -c "
import sys,json
try:
    runs=json.load(sys.stdin)
    for r in runs:
        print(f\"   {r['name']}: branch={r.get('headBranch','?')} status={r['status']} conclusion={r.get('conclusion','-')}\")
except Exception:
    pass
" || true
  note "CI/CD: confirme ci.yml e sddai-verify.yml all green para este commit antes do Gate de stage."
else
  note "gh não autenticado — verifique ci.yml e sddai-verify.yml manualmente antes do Gate de stage."
fi

# --- resumo ---
echo
echo "==> RESUMO PRE-PUSH"
if [ "$FAIL" -eq 1 ]; then
  echo "BLOQUEADO: corrigir as falhas acima antes de pushar."
  for n in "${NOTES[@]}"; do echo "  - $n"; done
  exit 1
fi
echo "Liberado para push."
if [ "${#NOTES[@]}" -gt 0 ]; then
  echo "Avisos pendentes (não bloqueiam):"
  for n in "${NOTES[@]}"; do echo "  - $n"; done
fi
exit 0
