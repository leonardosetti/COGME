---
id: docs-qualidade-08-relatorio-incidente-de-teste
title: Relatório de Incidente de Teste — ISTQB CTFL (Test Incident Report)
type: relatorio
version: 1.1.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/11-board-resultados-qualidade.md (RCA e incidentes)
- docs/auditorias/aud-2610-09-auditoria-extraordinaria-falso-positivo-cicd.md
- docs/auditorias/aud-2610-10-auditoria-extraordinaria-falso-positivo-health-check.md
- docs/auditorias/aud-2610-11-auditoria-extraordinaria-falso-positivo-credenciais.md
- docs/uat/rodada-001/relatorio-analitico.md (§4)
- .ai/specs/spec-010-qualidade-pdca-ishikawa-v1.spec.md (Ishikawa 6M)
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
- istqb
- incidente-de-teste
- test-incident-report
- rca
- defeito
---

# Relatório de Incidente de Teste — COGME (ISTQB CTFL Test Incident Report)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME |
| Artefato | Test Incident Report |
| Versão | 1.0.0 |
| Base | Board de Análise de Resultados de Qualidade (docs/qualidade/11-board-resultados-qualidade.md) |
| Rastreabilidade | RTM em docs/qualidade/10-rtm-qualidade.md |

## 2. Escala de prioridade, impacto e severidade

Usada para todos os incidentes deste relatório e do board de resultados.

| Nível | Prioridade (P) | Impacto (I) | Severidade (S) |
|---|---|---|---|
| P1 / Crítico | Correção imediato; bloqueia merge/UAT | Bloqueia fluxo crítico ou CI | Bloqueante: impossibilita entrega ou validação |
| P2 / Alto | Correção nesta iteração | Afeta funcionalidade importante sem bloqueio total | Maior: degrada função, workaround disponível |
| P3 / Médio | Correção no próximo ciclo | Afeta funcionalidade secundária | Menor: incômodo, sem perda de função |
| P4 / Baixo | Correção por oportunidade | Cosmético/documentação | Trivial: sem efeito sobre função |

## 3. Incidentes encontrados, resolvidos e pendentes

### INC-001 — Falso positivo CI/CD: segurança (CUDA/cloud)

| Campo | Valor |
|---|---|
| ID | INC-001 |
| Título | Alerta "Non-FOSS or cloud-bound reference detected!" no pipeline CI/CD |
| Data de abertura | 31/10/2026 |
| Status | Resolvido |
| Prioridade | P2 (Alto) |
| Impacto | Alto — pipeline `foss-compliance` ficava vermelho, bloqueando merge |
| Severidade | Média — não havia violação real de segurança |
| Detetado em | Auditoria extraordinária AUD-2610-09 |
| RCA | Dois fatores: (1) `grep -r` do `ci.yml` varria `.venv/` (pacotes terceiros com referências CUDA/AWS/GCP/Azure, não código COGME); (2) regex ingênua de `security_scan.py` marcava declarações de conformidade ("No cloud, no CUDA. Ever.") como falha. Causa-raiz: detecção sem análise de contexto e escopo de varredura muito amplo (Ishikawa-1: Método/Máquina). |
| Ação corretiva | `security_scan.py` passou a distinguir uso real vs. declaração de conformidade; aceitar agentes legacy-forge (Art. 4.8); não exigir Kill Switch/Bypass de agentes fora da topologia; resumo `[SECURITY] OK` movido para stderr. `ci.yml` passou a usar `security_scan.py --strict` em vez de `grep -r` ingênuo. |
| Evidência | docs/auditorias/aud-2610-09-...md; 181 testes passam, Security Scan 46/0 falhas |
| Rastreabilidade (RTM) | REQ-11 (CI/CD), FOSS P-01/P-02; nenhuma violação real |

### INC-002 — Falso positivo CI/CD: health check de agentes

| Campo | Valor |
|---|---|
| ID | INC-002 |
| Título | Health check marca `agent-factory-architect` e `-ultimate` como falha por ausência de frontmatter YAML |
| Data de abertura | 31/10/2026 |
| Status | Resolvido |
| Prioridade | P2 (Alto) |
| Impacto | Alto — job `agent-health` vermelho, bloqueando merge |
| Severidade | Baixa — agentes legacy-forge por decisão constitucional (Art. 4.8), intencionalmente sem frontmatter |
| Detetado em | Auditoria extraordinária AUD-2610-10 |
| RCA | Gate de validação não exibia categoria FORGE-LEGACY do registro; marcar como falha um artefato legacy por decisão constitucional é falso positivo. Causa-raiz: validação sem conhecimento da topologia/categoria do agente (Ishikawa-2: Método). |
| Ação corretiva | `agent_health_check.py` não gera erro nem aviso para legacy-forge sem frontmatter (conformidade Art. 4.8). |
| Evidência | docs/auditorias/aud-2610-10-...md; Agent Health Check 45/45 saudáveis |

### INC-003 — Falso positivo CI/CD: credenciais versionadas

| Campo | Valor |
|---|---|
| ID | INC-003 |
| Título | Alerta "Real credential detected in repository!" no job `foss-compliance` |
| Data de abertura | 31/10/2026 |
| Status | Resolvido |
| Prioridade | P2 (Alto) |
| Impacto | Alto — pipeline CI vermelho, bloqueando merge |
| Severidade | Baixa — não há credencial real versionada |
| Detetado em | Auditoria extraordinária AUD-2610-11 |
| RCA | Dois fatores: (1) string `AKIA[0-9A-Z]{16}` é o padrão regex de detecção dentro de `scripts/security_scan.py`, não uma credencial real; (2) `grep -r` varria `.venv/` (bibliotecas terceiras com variáveis `password` legítimas). Causa-raiz: varredura de diretórios não-projeto e auto-detecção de padrões de segurança (Ishikawa-1: Máquina/Método). |
| Ação corretiva | `ci.yml` passou a buscar credenciais apenas em diretórios do projeto (`.ai`, `.opencode`, `docs`, `scripts`, `src`, `test`, `tests`, `.github`), excluindo `.venv/`, `scripts/security_scan.py` e o próprio `ci.yml`. |
| Evidência | docs/auditorias/aud-2610-11-...md; Security Scan 46/0 falhas |

### INC-004 — Testes pulados violam regra zero-skipping do CI

| Campo | Valor |
|---|---|
| ID | INC-004 |
| Título | 13 testes pulados (skip) na suíte pytest (PDF real sem WeasyPrint nativo localmente) |
| Data de abertura | 14/11/2026 |
| Status | Pendente (aberto) |
| Prioridade | P3 (Médio) |
| Impacto | Médio — gate CI `test-suite` bloqueia se houver qualquer skip; em ambientes sem Pango a suíte não passa localmente |
| Severidade | Média — não é defeito de produto, é defeito de processo de execução |
| Detetado em | Instituição da disciplina de qualidade (docs/qualidade/05-casos-de-teste.md, §5) |
| RCA | Os testes de PDF real dependem de `import weasyprint` que levanta `OSError` apenas quando faltam bibliotecas nativas (Pango). No CI com Pango executam; localmente pulam. A regra "zero skipping" do CI não contempla skip condicional por ausência de biblioteca nativa. Causa-raiz: expectativa de execução invariante entre ambientes (Ishikawa-1: Máquina/Meio Ambiente). |
| Ação corretiva (proposta) | (a) Marcar os testes de PDF real com marcador `weasyprint` e rodá-los separadamente no CI (com Pango) e localmente (opcional); (b) ou instalar Pango nas imagens de build locais. Pendente de decisão do GP/CCB. |
| Rastreabilidade (RTM) | REQ-04 (invoice PDF), REQ-08 (coverage gate) |

### INC-005 — Drift de cobertura: plano 80% vs CI 95%

| Campo | Valor |
|---|---|
| ID | INC-005 |
| Título | `plano-qualidade.md` declara cobertura ≥ 80%; o CI `test-suite` exige `--cov-fail-under=95` |
| Data de abertura | 14/11/2026 |
| Status | Pendente (aberto) |
| Prioridade | P3 (Médio) |
| Impacto | Médio — divergência entre documento canônico de qualidade e gate real do CI gera confusão de critério de aceitação |
| Severidade | Baixa — não afeta produto; afeta clareza do critério de aceitação |
| Detetado em | Confronto `docs/planos/plano-granular/plano-qualidade.md` §5.4.2 (80%) vs `.github/workflows/ci.yml:213` (95%) |
| RCA | O plano de qualidade não foi atualizado após o aperfeiçoamento do gate de cobertura no CI (mudança de 80% para 95% não propagada ao documento). Causa-raiz: falta de sincronização documento↔CI em mudança de critério (Ishikawa-1: Método/Medida). |
| Ação corretiva (proposta) | Alinhar `plano-qualidade.md` §5.3/§5.4.2 para 95% (ou documentar o delta intencional por marco). Pendente. |
| Rastreabilidade (RTM) | REQ-08 (coverage ≥ 80% no termo autorizativo), REQ-11 (CI) |

### INC-006 — Ausência de evidências de execução dos PDCAs MF2/MF3

| Campo | Valor |
|---|---|
| ID | INC-006 |
| Título | `MF2-licoes.md` e `MF3-licoes.md` vazios (0 B); nenhuma lição por-PDCA registrada para N5-N12 |
| Data de abertura | 14/11/2026 |
| Status | Pendente (aberto) |
| Prioridade | P3 (Médio) |
| Impacto | Médio — não há evidência de execução/verificação dos ciclos PDCA da REQ-10 (fase N6.3) |
| Severidade | Baixa — não afeta produto; afeta conformidade da entrega de qualidade REQ-10 |
| Detetado em | spec-010 (§3.1, :130-137) e plano-qualidade §5.6 |
| RCA | Lições aprendidas não consolidadas após M1/M2; apenas LA-001 registrada (MF1). Causa-raiz: retrospectivas não geraram artefatos por-PDCA (Ishikawa-3: Método/Mão de Obra). |
| Ação corretiva (proposta) | Registrar lições por PDCA em `docs/conhecimento/licoes-aprendidas/MF2-licoes.md` e `MF3-licoes.md` na próxima retrospectiva (ondas MF2/MF3). Pendente. |
| Rastreabilidade (RTM) | REQ-10 (12 PDCAs + Ishikawa), fase N6.3 |

### INC-007 — Drift gráfico: FIG-5 aponta mesmo PNG de FIG-3; diretório diagrams/ inexistente

| Campo | Valor |
|---|---|
| ID | INC-007 |
| Título | FIG-5 reutiliza PNG de FIG-3 (`fig-05-ishikawa-coverage.png`) e `diagrams/` não existe |
| Data de abertura | 14/11/2026 |
| Status | Resolvido (forma de entrega alterada) |
| Prioridade | P4 (Baixo) |
| Impacto | Baixo — diagramas Ishikawa não renderizados no plano de qualidade |
| Severidade | Baixa — documentação, sem efeito sobre produto |
| Detetado em | spec-010 §2 (drift gráfico) |
| RCA | Os PNGs dos Ishikawa nunca foram gerados; o diretório `diagrams/` inexistente e FIG-5 aponta o mesmo arquivo de FIG-3. Causa-raiz: entrega em formato PNG não produzida (Ishikawa-1: Máquina). |
| Ação corretiva | Substituir forma de entrega dos Ishikawa por mermaid inline (spec-010 §3.2); drift registrado sem editar `plano-qualidade.md` (sem custódia de terceiro). |
| Evidência | spec-010 §3.2, AC-07 |

### INC-008 — Gate `pre-push` inexistente na prática (não instalado; artefatos untracked)

| Campo | Valor |
|---|---|
| ID | INC-008 |
| Título | O gate local `pre-push-ciclo-codificacao-deploy.sh` e seu runbook nunca foram commitados nem instalados em `.git/hooks/` |
| Data de abertura | 15/11/2026 |
| Status | EM VERIFICAÇÃO — gate instalado e artefatos commitados (cf063b6, 6e2049e); aguarda auditor |
| Prioridade | P2 (Alto) |
| Impacto | Alto — o DoD "Push permitido pelo hook `pre-push`" não era verificável; nenhum push era avaliado |
| Severidade | Média — defeito de processo (gate morto), não de produto |
| Detetado em | Rodada de refinamento do gate (15/11/2026): `.git/hooks/` sem `pre-push`; `git status` marca hook e runbook como untracked |
| RCA | O runbook (v1.0.0) e o hook foram criados no mesmo dia sem registro no fluxo de commit (código + testes + docs). Causa-raiz: artefato de processo emitido fora do ciclo de codificação que ele próprio normatiza (Ishikawa-3: Método/Mão de Obra). |
| Ação corretiva | Instalação local executada (`cp` para `.git/hooks/pre-push` + chmod +x) e gate refinado (INC-009/010/011). Pendente: commitar `scripts/githooks/pre-push-ciclo-codificacao-deploy.sh` e `docs/operacao/proc-ciclo-codificacao-deploy.md` (não commitado para não misturar com WIP de `src/` em andamento). |
| Rastreabilidade (RTM) | REQ-11 (CI/CD), P-06 (qualidade fechada) |

### INC-009 — Gate de specs inpassável (vocabulário `ratificada|aprovado` inexistente no acervo)

| Campo | Valor |
|---|---|
| ID | INC-009 |
| Título | Hook exigia `status: ratificada|aprovado`, vocabulário que não existe em nenhum arquivo do repositório |
| Data de abertura | 15/11/2026 |
| Status | Resolvido |
| Prioridade | P2 (Alto) |
| Impacto | Alto — qualquer push que tocasse um `.spec.md` seria bloqueado; gate letra-morta ou incentivo a bypass |
| Severidade | Média — gate normativo inoperável |
| Detetado em | Varredura do acervo: 100% das specs implementadas (spec-001..023) usam `status: ativo`; propostas usam `draft`; nenhum arquivo usa `ratificada`/`aprovado` |
| RCA | O runbook §3 v1.0.0 inventou vocabulário fora do conjunto fechado da NORMA-TEMPLATES-ARTEFATOS (`ativo|draft|ratificado|obsoleto|arquivado`), e o hook copiou o runbook. Ratificações reais do CCB ficaram registradas em CRs/commits, sem propagar ao frontmatter. Causa-raiz: falta de sincronização norma↔runbook↔acervo (Ishikawa-1: Método). |
| Ação corretiva | Hook refinado com decisão de gate ratificada pelo GP: `ativo` (vigente) e `ratificado/ratificada/aprovado(a)` liberam; `draft`/`obsoleto`/`arquivado`/ausente bloqueiam. Runbook emendado para v1.1.0 alinhado à norma. |
| Evidência | Teste em worktree: commit de código contra `spec-prop-017` (draft) bloqueado; contra `spec-004` (ativo) liberado |
| Rastreabilidade (RTM) | REQ-11, P-06; constituição Art. 5.3 (aprovação humana CCB preservada) |

### INC-010 — Falsos bloqueios do gate `pre-push` (deletados, coverage de integração, mypy)

| Campo | Valor |
|---|---|
| ID | INC-010 |
| Título | Três cenários legítimos de push eram bloqueados indevidamente pelo hook |
| Data de abertura | 15/11/2026 |
| Status | Resolvido |
| Prioridade | P2 (Alto) |
| Impacto | Alto — push de deleção de `.py` travava no flake8 de arquivo inexistente; integração com DB exigia cobertura ≥ 80% da suíte de integração sozinha (critério que o runbook §6.2 não estabelece); mypy rodava com flags duplicadas (fora do SSOT `pyproject.toml`) mesmo sem `src/` alterado |
| Severidade | Média — gate falhava fechado sobre cenários válidos |
| Detetado em | Auditoria linha a linha do hook contra o runbook (15/11/2026) |
| RCA | (1) `git diff --name-only` sem filtro de estado inclui arquivos deletados; (2) critério de cobertura da suíte unitária (§6.1) replicado na integração (§6.2); (3) flags `--strict src/` duplicando `[tool.mypy]` e escopo maior que a mudança. Causa-raiz: gate escrito sem derivar critérios das seções do runbook (Ishikawa-1: Método). |
| Ação corretiva | `--diff-filter=d` no diff; `--cov-fail-under=80` removido da integração (mantido relatório); mypy condicionado a `src/` alterado e invocado sem flags (config única no `pyproject.toml`). |
| Evidência | Commit histórico de deleção/rename de `.py` passa sem flake8 fantasma; `mypy` verde no working tree |
| Rastreabilidade (RTM) | REQ-08, REQ-11 |

### INC-011 — Status de spec lido fora do frontmatter (falsa passagem)

| Campo | Valor |
|---|---|
| ID | INC-011 |
| Título | Regex `\nstatus:` casava a primeira ocorrência em qualquer ponto do arquivo, não só no frontmatter |
| Data de abertura | 15/11/2026 |
| Status | Resolvido |
| Prioridade | P3 (Médio) |
| Impacto | Médio — linha `status:` em tabela ou corpo do documento poderia liberar (ou bloquear) a spec errada |
| Severidade | Baixa — gate de especificação com leitura imprecisa |
| Detetado em | Auditoria do hook (15/11/2026) |
| RCA | Validação por regex de texto integral em vez de parse do bloco YAML entre os dois primeiros `---`. Causa-raiz: parser implícito sem delimitação de frontmatter (Ishikawa-1: Método). |
| Ação corretiva | Função `spec_field` lê apenas o bloco frontmatter; exige também `id:`/`spec-id:` (rastreabilidade, runbook §3). |
| Evidência | Teste de unidade do helper: arquivo com `status: draft` no frontmatter e `status: ratificado` no corpo retorna `draft` |
| Rastreabilidade (RTM) | REQ-11 |

### INC-012 — Validador de frontmatter escaneia acervo integral no gate; 30 problemas legados; CI lint vermelho

| Campo | Valor |
|---|---|
| ID | INC-012 |
| Título | `validar_frontmatter_md.py` sem escopo por arquivo; acervo com 30 não conformidades em 427 `.md`; runs do `ci.yml` em FAIL |
| Data de abertura | 15/11/2026 |
| Status | EM VERIFICAÇÃO — acervo 427/427 `.md` com frontmatter válido (2626e5d); aguarda CI remoto |
| Prioridade | P2 (Alto) |
| Impacto | Alto — o hook contrariava o próprio cabeçalho e o runbook §7.4 (".md **alterados**"), transformando dívida legada em bloqueio permanente de push; runs recentes do CI (43619860226, 43618821664, 43555741240) em FAIL |
| Severidade | Média — dívida documental com efeito de gate |
| Detetado em | Simulação do hook em intervalo histórico: `[FAIL] 30 problema(s) em 427 arquivo(s)` |
| RCA | Validador sem API de escopo; mudanças de vocabulário da norma não propagadas ao acervo (`lgpd-class: dados-pessoais`; `type: analise`/`auditoria`/`registro`; ADRs `status: aprovada`). Causa-raiz: ferramenta e acervo fora de sincronia com a norma (Ishikawa-1: Método; Ishikawa-6: Material). |
| Ação corretiva | (a) Aplicada: validador aceita arquivos posicionais (retrocompatível; uso por arquivo já documentado em `kb-guia-adequacao-pmbok7-hibrido.md:428`), o hook valida só os `.md` alterados, e os 2 `.md` tocados na emenda foram saneados (`type: registro` → `relatorio`). (b) Pendente: sanear as 28 não conformidades restantes do acervo e decidir se o CI mantém o scan integral (recomendado, após saneamento). |
| Rastreabilidade (RTM) | REQ-11 (job lint), REQ-14 (documentação) |

### INC-013 — Cobertura da suíte unitária 77,97% < gate 80% (bloqueia todo push de código)

| Campo | Valor |
|---|---|
| ID | INC-013 |
| Título | Suíte `tests/unit` sozinha em 78% — gate local `--cov-fail-under=80` bloqueia qualquer push com código |
| Data de abertura | 15/11/2026 |
| Status | EM VERIFICAÇÃO — cobertura unitária 84,01% ≥ 80% (ebd0237); gate local liberado |
| Prioridade | P2 (Alto) |
| Impacto | Alto — 1164 passed, porém `TOTAL 78%` < 80%: todo push de código falhava no gate local até elevação de cobertura |
| Severidade | Média — gate corre (fail-closed, P-06), mas o estado da suíte impede o fluxo |
| Detetado em | Simulação end-to-end do hook (15/11/2026), após os ajustes de INC-010 |
| RCA | Módulos com cobertura baixa: `src/backend/routers/common.py` 41%, `src/backend/routers/invoices.py` 39%. Relacionado ao INC-005 (drift 80% plano × 95% CI): o gate local aplica 80% sobre a suíte unitária sozinha, o CI aplica 95% sobre a suíte completa. Causa-raiz: cobertura por camada não gerida como métrica contínua (Ishikawa-4: Medida). |
| Ação corretiva (proposta) | Completar testes de `routers/common.py` e `routers/invoices.py` (maiores lacunas), ou explicitar no plano de qualidade o critério por camada (unit 80% / suíte completa 95%). Pendente de decisão GP/qa-sdet. |
| Rastreabilidade (RTM) | REQ-08 (coverage), REQ-11 |

### INC-014 — HEAD mypy-red; correções apenas no working tree (trabalho não commitado)

| Campo | Valor |
|---|---|
| ID | INC-014 |
| Título | `src/` no HEAD falha em `mypy` (erros em `invoices.py`/repositório); working tree com 11 arquivos modificados corrige, sem commit |
| Data de abertura | 15/11/2026 |
| Status | EM VERIFICAÇÃO — WIP commitado com lint saneado (cf063b6); mypy e flake8 verdes |
| Prioridade | P3 (Médio) |
| Impacto | Médio — push a partir do estado HEAD (sem o WIP) falhava no gate; risco de perda do trabalho não commitado |
| Severidade | Baixa — estado transitório de trabalho em andamento |
| Detetado em | Cenário de teste em worktree a partir de HEAD (15/11/2026): mypy falhou; no checkout principal, verde |
| RCA | Correções de `src/backend/routers/invoices.py`, `models/invoice_repository.py`, `services/invoice_service.py` etc. ainda não commitadas; o WIP também carrega 27 violações de flake8 em `tests/integration/test_invoices_persistence.py` (F401, E501, F541, W292). Causa-raiz: ciclo de commit (código + testes + docs) não fechado (Ishikawa-3: Mão de Obra). |
| Ação corretiva (proposta) | Sanear o flake8 do WIP e commitar conforme runbook §7 (código + testes + documentação no mesmo commit). Pendente. |
| Rastreabilidade (RTM) | REQ-11, P-06 |

### INC-015 — Drift normativo: runbook §3 vs NORMA-TEMPLATES vs dados reais

| Campo | Valor |
|---|---|
| ID | INC-015 |
| Título | Runbook §3 usava `ratificada|aprovado` e `spec-id`, fora do vocabulário fechado da norma e do que o acervo de fato usa (`ativo`, `id:`) |
| Data de abertura | 15/11/2026 |
| Status | Resolvido (pendente ratificação CCB) |
| Prioridade | P3 (Médio) |
| Impacto | Médio — três vocabulários distintos (norma, runbook, acervo) tornavam o gate de specs inoperável (ver INC-009) |
| Severidade | Baixa — documental, com efeito sistêmico no gate |
| Detetado em | Confronto NORMA-TEMPLATES-ARTEFATOS §57 × runbook v1.0.0 §3 × acervo (15/11/2026) |
| RCA | Procedimento emitido sem derivar vocabulário da norma de templates nem validar contra o acervo real. Causa-raiz: falta de sincronização norma↔procedimento (Ishikawa-1: Método). |
| Ação corretiva | Runbook emendado para v1.1.0: `ativo`/`ratificado` liberam; `draft`/`obsoleto`/`arquivado` bloqueiam; rastreabilidade `id:`/`spec-id:`. Pendente ratificação CCB (Art. 9). |
| Evidência | `docs/operacao/proc-ciclo-codificacao-deploy.md` v1.1.0, controle de versões |
| Rastreabilidade (RTM) | REQ-14 (documentação técnica) |

### INC-016 — Runbook §7.3: tipos de Conventional Commits menores que a prática ratificada

| Campo | Valor |
|---|---|
| ID | INC-016 |
| Título | Lista de tipos (`feat..chore`) omite `spec` e `uat`, usados em commits já ratificados no histórico |
| Data de abertura | 15/11/2026 |
| Status | Resolvido (pendente ratificação CCB) |
| Prioridade | P4 (Baixo) |
| Impacto | Baixo — gate local trata divergência como aviso não bloqueante; normativo ficaria sem efeito |
| Severidade | Baixa — documental |
| Detetado em | `git log --format='%s' -30`: commits `spec(ui):`, `uat(rodada-001):` etc. |
| RCA | Lista de tipos definida sem amostragem do histórico real. Causa-raiz: norma sem validação empírica (Ishikawa-1: Método). |
| Ação corretiva | Runbook v1.1.0 adiciona `spec` e `uat` como tipos válidos para artefatos de especificação e UAT. Pendente ratificação CCB. |
| Rastreabilidade (RTM) | REQ-13 (rastreabilidade), REQ-14 |

## 4. Índice de incidentes por status

| Status | Quantidade | IDs |
|---|---|---|
| Resolvido | 9 | INC-001, INC-002, INC-003, INC-007, INC-009, INC-010, INC-011, INC-015, INC-016 |
| EM VERIFICAÇÃO | 4 | INC-008, INC-012, INC-013, INC-014 |
| Pendente/Aberto | 3 | INC-004, INC-005, INC-006 |

**Total:** 16 incidentes (9 resolvidos, 4 em verificação, 3 pendentes). INC-015/016 resolvidos dependem de ratificação CCB (runbook v1.1.0).

## 5. Assinatura

| Papel | Nome/Função | Data |
|---|---|---|
| Registrante | qa-sdet (agent-qa-sdet) | 14/11/2026 |
| Registrante (adenda INC-008..016) | qa-sdet (agent-qa-sdet) | 15/11/2026 |
| Revisor | reviewer (agent-reviewer) | |
| Auditor | auditor (agent-project-auditor) | |
