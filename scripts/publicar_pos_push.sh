#!/usr/bin/env bash
# publicar_pos_push.sh — Executa sanity de CI após push e publica README atualizado.
#
# Fluxo:
#   1. Rode por usuário/CI após `git push` de sucesso.
#   2. Executa scripts/ci_post_commit_check.py (sanity).
#   3. Se passar: reescreve README (limpa seção de falha), commit, push.
#   4. Se falhar: retry até 5 vezes (sanity -> commit -> push).
#   5. Se continuar falhando: anota falha no README (seção específica), commit, push, sai com 1.
#
# Stdlib + git. Não adiciona dependências.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PY="${PYTHON:-python3}"
MAX_RETRIES="${COGME_MAX_RETRIES:-5}"
REMOTE="${COGME_REMOTE:-origin}"
BRANCH="${COGME_BRANCH:-$(git branch --show-current)}"

GIT_AUTHOR_NAME="${GIT_AUTHOR_NAME:-COGME bot}"
GIT_AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:-bot@cogme.local}"

git_config_local() {
  git -c user.name="$GIT_AUTHOR_NAME" -c user.email="$GIT_AUTHOR_EMAIL" "$@"
}

commit_readme() {
  local msg="$1"
  git add README.md
  if git diff --cached --quiet; then
    echo "README sem alterações para commitar."
    return 0
  fi
  export COGME_README_REWRITING=1
  git_config_local commit -m "$msg" || true
  git push "$REMOTE" "$BRANCH" || true
}

registra_falha() {
  local motivo="$1"
  echo "Falha de pipeline persistente. Anotando no README."
  export COGME_README_REWRITING=1
  "$PY" scripts/atualizar_readme_governanca.py --falha-pipeline "$motivo"
  commit_readme "docs(readme): registra falha de pipeline após ${MAX_RETRIES} tentativas de sanity"
}

limpa_falha() {
  export COGME_README_REWRITING=1
  "$PY" scripts/atualizar_readme_governanca.py --limpar-falha-pipeline
  commit_readme "docs(readme): atualiza versão e governança pós-push"
}

echo "==> Sanity de CI (scripts/ci_post_commit_check.py)"
sucesso=0
for i in $(seq 1 "$MAX_RETRIES"); do
  if "$PY" scripts/ci_post_commit_check.py; then
    sucesso=1
    break
  fi
  echo "==> Tentativa $i/$MAX_RETRIES falhou. Novo retry em 2s..."
  sleep 2
done

if [ "$sucesso" -eq 1 ]; then
  limpa_falha
  echo "==> Publicado com sucesso."
  exit 0
fi

registra_falha "CI sanity falhou após ${MAX_RETRIES} tentativas. Última tentativa não passou."
echo "==> Falha persistente anotada no README. Publishe novamente após saneamento."
exit 1
