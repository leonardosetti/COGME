---
id: docs-operacao-ciclo-codificacao-deploy
title: Runbook — Ciclo de Codificação e Deploy (Espec Aprovada → Stage → Aprovação de Merge)
type: procedimento
version: 1.1.0
status: ativo
owner: agent-devops
derived-from:
  - constitution.md (Art. 6.1 SDD; Art. 9.3 fluxo de mudança integrado; P-06 qualidade fechada; P-11 YAGNI; P-10 linguagem)
  - ADR-007 (redes de projeto PMBOK — dualidade CPM macro × Kanban micro)
  - ADR-011 (separação ortogonal L1/L2/L3; memória persistente)
  - docs/operacao/proc-runbook.md (deploy, rollback, stage, smoke tests)
  - docs/operacao/proc-cr-spec-approval-workflow.md (CR + Spec → produção)
  - docs/normas/NORMA-TEMPLATES-ARTEFATOS.md
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
  - procedimento
  - runbook
  - codificacao
  - deploy
  - stage
  - pipeline
  - pdca
  - pmbok
  - merge
hook: scripts/githooks/pre-push-ciclo-codificacao-deploy.sh
---

# Runbook — Ciclo de Codificação e Deploy (Espec Aprovada → Stage → Aprovação de Merge)

> **Finalidade**: definir o ciclo obrigatório de codificação e deploy do COGME: codifica-se **sobre specs aprovadas**, verifica e resolve dependências, calcula paralelismo com gate de redes de projeto (PMBOK), aplica ciclos PDCA contínuos antes de implementar, respeita YAGNI+KISS e padrões dev, testa localmente (unitário + integração ou mock/stub), faz deploy em stage com pipelines CI/CD all green, emite documentação (logs, relatórios de testes, implantação, deploy) e, após o gate de stage, **aguarda aprovação humana para merge**.
> **Público**: desenvolvedores, QA, DevOps, GP/CCB.
> **Hook local**: `scripts/githooks/pre-push-ciclo-codificacao-deploy.sh` (ativa em `.git/hooks/pre-push`).
> **Atualização**: a cada release, mudança de infra, ou incidente (lições aprendidas).

---

## 1. OBJETIVO E ESCOPO

Aplicar, em cada ciclo de trabalho, a sequência:

**Espec aprovada → dependências → paralelismo (PMBOK) → PDCA → testes locais → implementação → commit (docs + testes) → deploy stage → CI/CD all green → documentação → gate de stage → aprovação de merge.**

Não há código sem spec aprovada. Não há merge sem gate de stage aprovado humano (CCB/GP). Não há exceção sem Change Request (Constituição Art. 9).

---

## 2. PAPÉIS E RESPONSABILIDADES

| Papel | Responsabilidade no ciclo |
|---|---|
| Desenvolvedor | Lê spec, valida dependências, codifica (PDCA), testa localmente, commita docs + testes, abre PR |
| QA / agent-reviewer | Revisão contínua, valida testes unitários/integração, confirma coverage ≥ 80% |
| DevOps / agent-devops | Deploy em stage, verifica pipelines CI/CD, decide rollback vs correção de pipeline |
| GP / CCB | Aprova specs (ratificação), Gate 3 de stage, aprovação final de merge (ato exclusivamente humano — Constituição Art. 5.3) |

---

## 3. DEFINIÇÕES

- **Spec liberada para codificação**: arquivo `.ai/specs/spec-*.spec.md` ou `docs/especificacoes/spec-*.md` com frontmatter `status` no vocabulário fechado da NORMA-TEMPLATES-ARTEFATOS liberando codificação — `ativo` (vigente) ou `ratificado`/`ratificada`/`aprovado(a)` (aprovado pelo CCB) — e rastreabilidade `id:` (ou `spec-id:`) preenchida. Specs `draft`, `obsoleto` ou `arquivado` não liberam codificação.
- **DoR (Definition of Ready)**: spec liberada para codificação (§3) + dependências resolvidas + gate de rede de projeto liberado + WIP ≤ 3 (constituição 6.2).
- **DoD (Definition of Done)**: código implementado conforme spec + testes unitários locais verdes + integração ou mock/stub + lint/type verdes + cobertura ≥ 80% + documentação (log + relatório de teste + implantação + deploy) + stage verde + gate de stage aprovado.
- **Gate de rede de projeto (PMBOK)**: dependência entre specs tratada como rede de atividades (CPM macro — ADR-007). Spec dependente só inicia após a spec predecessora estar `ratificada` e implementada/mergeada. Redes valida o marco; o Kanban executa a tarefa — nunca usar datas CPM para bloquear card diário.
- **Paralelismo**: specs independentes (sem aresta de dependência e sem dono/recurso compartilhado) podem ser codificadas em paralelo. Specs em cadeia (A → B) são sequenciais.
- **PDCA (antes de implementar)**: Plan → Do → Check → Act, aplicado em ciclos curtos sobre cada unidade de código.
- **YAGNI+KISS**: nada além do exigido pela spec do ciclo atual; solução mais simples que funcione; sem abstração "para depois".
- **Anti-loop de revisão**: no máximo 3 ciclos PDCA por item; sem convergência, escalar para reviewer/gatekeeper e abrir issue. Não revisar indefinidamente.

---

## 4. FASE 0 — VALIDAÇÃO DE ENTRADA (ANTES DE CODIFICAR)

### 4.1 Confirma spec liberada
```
grep -RnE "^status: (ativo|ratificado)" .ai/specs/spec-XXX.spec.md docs/especificacoes/spec-XXX.md
```
Sem `status: ativo` ou `status: ratificado` no frontmatter, **não iniciar codificação**. Propostas (`draft`, `spec-prop-*`) exigem CR (Change Request) e ratificação do CCB.

### 4.2 Verificar e resolver dependências
1. Mapear `trace:` / `derived-from` / `blocks:` da spec.
2. Para cada dependência, confirmar que a spec predecessora está liberada para codificação (§3) e seu código está em `main`.
3. Dependência não resolvida → aguardar ou abrir CR para desbloquear. Não codificar sobre dependência aberta.

### 4.3 Gate de rede de projeto (PMBOK) e paralelismo
1. Construir grafo de dependências das specs do ciclo (nó = spec, aresta = depende-de).
2. Especs sem predecessores pendentes = **Ready** (podem iniciar).
3. Especs independentes entre si = **paralelizáveis** (alocar desenvolvedores distintos, WIP ≤ 3 por pessoa).
4. Especs em cadeia = sequenciais; a sucessora inicia após a predecessora entregar.
5. Registrar decisão de paralelismo no handoff/ledger (`.ai/agents/ledger.yaml`) — SSOT, sem duplicação (constituição 6.7).

**Saída da Fase 0**: lista de specs liberadas, quais codificar em paralelo, quais aguardam gate, e branch(es) de criação.

---

## 5. FASE 1 — CICLO DE CODIFICAÇÃO PDCA CONTÍNUO (ANTES DE IMPLEMENTAR)

Aplicar PDCA em cada unidade antes de gravar código definitivo:

| Ciclo | Ação |
|---|---|
| **Plan** | Ler spec; listar tarefas mínimas; definir testes a passar; separar o que é YAGNI (fora de escopo) |
| **Do** | Implementar o menor trecho que satisfaça a spec (KISS); padrões dev do projeto (FastAPI, Pydantic v2, SQLAlchemy async, Decimal para dinheiro, contrato de erro padronizado, owner_user_id em todo recurso — P-14) |
| **Check** | Revisão contínua: flake8 + mypy strict sobre o trecho; testes unitários locais; comparar contra critérios de aceite da spec |
| **Act** | Se passou: consolidar e avançar. Se falhou: corrigir e repetir PDCA. Máximo 3 ciclos por item; sem convergência, escalar ao reviewer/gatekeeper e abrir issue |

Regras:
- Implementar **apenas** o que a spec exige (YAGNI). Exclusões de fronteira vão ao backlog Kanban, não ao código.
- Manter contexto de código não degradado: não refatorar além do necessário para a spec; não introduzir abstrações genéricas.
- Logs e artefatos técnicos **sem PII** (constituição P-04, P-15).

---

## 6. FASE 2 — TESTES LOCAIS

### 6.1 Rodada de testes unitários (local)
```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/unit -q --cov=src --cov-report=term-missing
```
Critério: cobertura ≥ 80% (constituição P-06). Falha → não avançar.

### 6.2 Testes de integração (quando houver)
```bash
# Requer COGME_TEST_DATABASE_URL apontando para banco descartável (nunca dados reais)
python -m pytest tests/integration -q --cov=src --cov-report=term-missing
```

### 6.3 Se não houver integração disponível → mock/stub
- Substituir dependência externa (banco, API de cotação, SMTP) por mock/stub determinístico.
- Testar contra o mock e registrar qual dependência foi substituída e por quê no relatório de testes.
- Mocks não substituem integração permanente: criar issue para complementar com integração real quando disponível.

---

## 7. FASE 3 — IMPLEMENTAÇÃO LOCAL E COMMIT

1. Implementar localmente conforme spec (Fase 1).
2. Commit contendo **código + testes + documentação** (não commitar código sozinho).
3. Mensagem no formato Conventional Commits do projeto:
   ```
   feat(simulacao): implementar endpoint X conforme spec-004
   ```
   Tipos válidos: `feat`, `fix`, `docs`, `test`, `refactor`, `build`, `ci`, `chore` e, para artefatos de especificação e de UAT, `spec` e `uat` (tipos em uso no histórico ratificado do projeto). Subject ≤ 72 chars, imperativo, sem ponto final.
4. Frontmatter de `.md` alterados conforme NORMA-TEMPLATES-ARTEFATOS (valida com `scripts/validar_frontmatter_md.py`).
5. Nunca versionar credenciais reais, PII ou segredos (constituição P-03, P-07). Apenas chaves dummy (`sk-local-dummy-key`).

---

## 8. FASE 4 — DEPLOY EM STAGE E CI/CD ALL GREEN

### 8.1 Commit + push de docs e testes
Enviar para o remote a branch com código, testes e documentação. O hook `pre-push` valida localmente antes de permitir o push.

### 8.2 Verificar pipelines CI/CD (workflows) a cada deploy
Após push, verificar no GitHub Actions (repositório `leonardosetti/COGME`):
- `ci.yml` — COGME CI/CD Pipeline
- `sddai-verify.yml` — SDDAI Verify Pipeline

Critério de sucesso: **todos os jobs `success`** para o commit/tag implantado. Verificar **a cada deploy**, não apenas uma vez.

```bash
# Exemplo (exige gh autenticado)
gh run list --repo leonardosetti/COGME --branch <branch> --limit 5
gh run view <run-id> --repo leonardosetti/COGME
```

### 8.3 Decisão ante falha de pipeline
Se qualquer pipeline falhar:
1. Classificar a falha:
   - **Falha de código** (teste, lint, type, security) → **reversão de código** (reverter o commit/ branch) ou correção do código e novo push.
   - **Falha de pipeline/workflow** (infra do CI, fluxo quebrado, falso positivo de health check/credencial — cf. auditorias AUD-2610-08/09/11) → **corrigir o issue do pipeline/workflow**, não o código da aplicação.
2. Não fazer deploy para stage com pipeline vermelho.
3. Documentar a decisão no relatório de deploy e, se incidente P0/P1, abrir post-mortem (template `docs/conhecimento/templates/kb-template-post-mortem.md`).

### 8.4 Smoke tests em stage
Executar `scripts/smoke_tests.sh` (ou equivalente) contra o stage:
- `/health`, `/health/db`, `/v1/rates/USD`, `/v1/simulate`, front-end, invoice PDF.

---

## 9. FASE 5 — DOCUMENTAÇÃO DO PROCESSO

Emitir e arquivar, por ciclo:

| Artefato | Conteúdo | Onde |
|---|---|---|
| Log de execução | Saída dos comandos do ciclo (testes, lint, build, deploy) | `docs/relatorios/` ou evidências do UAT |
| Relatório de testes | Unitários, integração/mock, cobertura, falhas | `docs/qualidade/` + `docs/uat/<rodada>/evidencias/` |
| Relatório de implantação | Versão, commit, branch, data, ambiente stage, smoke tests | `docs/operacao/` |
| Relatório de deploy | Imagem/tag, health checks, decisão rollback ou pipeline, Gate 3 | `docs/relatorios/rel-release-notes-vX.Y.Z.md` |

Todos os artefatos `.md` com frontmatter completo (NORMA-TEMPLATES-ARTEFATOS). Nunca PII em logs (constituição P-04/P-15).

---

## 10. GATE DE IMPLANTAÇÃO EM STAGE → AGUARDAR APROVAÇÃO PARA MERGE

Após deploy em stage verde e documentação completa:

1. **Gate de implantação em stage revisado** (smoke tests OK, CI/CD all green, rollback validado).
2. **Aguardar aprovação humana para merge** (GP/CCB — ato exclusivamente humano, Constituição Art. 5.3; parecer do gatekeeper).
3. Só após a aprovação: merge em `main`, tag `vX.Y.Z`, deploy produção (conforme `docs/operacao/proc-runbook.md` §2) e atualização do Kanban (cards → Done).

Nenhum merge ocorre antes desta aprovação.

---

## 11. ROLLBACK E FALHAS DE PIPELINE

- Smoke tests falham pós-deploy stage → rollback rápido (tag anterior estável) em < 5 min (runbook operacional §3.2).
- Migração problemática → rollback + restore de backup (runbook operacional §3.3, §6).
- Pipeline verde local, vermelho remoto → corrigir workflow/pipeline; não confundir com falha de código.
- Toda decisão de rollback/correção registrada no relatório de deploy e no CCB Log.

---

## 12. CHECKLISTS

### Checklist de entrada (Fase 0)
- [ ] Spec com `status` liberador (`ativo` ou `ratificado`)
- [ ] Dependências todas resolvidas (specs predecessoras em `main`)
- [ ] Gate de rede de projeto liberado (não bloqueado por spec em cadeia)
- [ ] Paralelismo definido (quais specs rodam em paralelo, quais em sequência)
- [ ] WIP ≤ 3 por pessoa

### Checklist de saída / DoD (Fases 1–5)
- [ ] Código implementado conforme spec (YAGNI+KISS, padrões dev)
- [ ] PDCA aplicado, ≤ 3 ciclos por item
- [ ] Testes unitários locais verdes, cobertura ≥ 80%
- [ ] Integração executada ou mock/stub justificado
- [ ] flake8 + mypy strict verdes
- [ ] Commit com código + testes + documentação
- [ ] Push permitido pelo hook `pre-push`
- [ ] Deploy em stage realizado
- [ ] Pipelines CI/CD (ci.yml, sddai-verify.yml) all green
- [ ] Smoke tests stage OK
- [ ] Logs, relatório de testes, implantação e deploy arquivados
- [ ] Gate de stage revisado
- [ ] **Aprovação humana para merge (aguardando — não prosseguir sem ela)**

---

## 13. CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-15 | agent-devops | Criação inicial: ciclo de codificação e deploy com PDCA, gate PMBOK, stage, CI/CD all green, aprovação de merge | GP (CCB) |
| 1.1.0 | 2026-11-15 | agent-devops | Adequação à norma de dados (NORMA-TEMPLATES-ARTEFATOS §57): `ativo`/`ratificado` liberam codificação, `draft`/`obsoleto`/`arquivado` bloqueiam; rastreabilidade `id`/`spec-id`; tipos de commit `spec`/`uat`; reflete gate `pre-push` refinado (INC-009/015/016) | Pendente (GP/CCB) |

---

> Integração: este runbook é referenciado por `docs/operacao/proc-runbook.md` e por `docs/operacao/proc-cr-spec-approval-workflow.md`. O hook associado é `scripts/githooks/pre-push-ciclo-codificacao-deploy.sh`.
