---
id: kb-template-post-mortem
title: Template de Post-Mortem (Blameless) — Análise Pós-Incidente
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-digital-security
derived-from:
  - constitution.md Art. 7 (Segurança e resposta a incidentes)
  - docs/conhecimento/licoes-aprendidas/mf1-licoes.md (padrão MFs atuais)
  - PMBOK 7ª — Domínio Medição (Lessons Learned)
  - Blameless Post-Mortem Culture (Google SRE / Atlassian)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - template
  - operacao
  - post-mortem
  - incidentes
  - blameless
  - sre
---

# Template de Post-Mortem (Blameless) — COGME

> **Finalidade**: Análise técnica **sem culpa** (blameless) após incidente grave (P1/P0) para identificar **causa raiz**, documentar **ações preventivas** e evitar recorrência. **Não busca culpados** — busca falhas de sistema, processo, ferramenta ou comunicação.
> **Prazo**: Iniciar em até **24h** pós-resolução; concluir em até **5 dias úteis**.
> **Publicação**: `docs/operacao/proc-post-mortem-PM-YYYY-MM-DD-slug.md` + link no CCB Log + menção no Status Report.

---

## 1. CABEÇALHO DO INCIDENTE

| Campo | Valor |
|---|---|
| **PM-ID** | PM-YYYY-MM-DD-NN (ex: PM-2026-11-15-01) |
| **Título** | Breve descrição do incidente (ex: "Indisponibilidade total API rates por 47min") |
| **Severidade** | [ ] **P0 — Crítico** (produção parada, dados em risco, segurança)  [ ] **P1 — Alto** (funcionalidade principal degradada, SLA violado)  [ ] **P2 — Médio** (funcionalidade secundária, workaround existe) |
| **Status** | [ ] Em Investigação  [ ] Concluído  [ ] Ações Preventivas Em Andamento  [ ] Fechado |
| **Início do Incidente** | YYYY-MM-DD HH:MM:SS (UTC) |
| **Fim do Incidente** | YYYY-MM-DD HH:MM:SS (UTC) |
| **Duração Total** | XX min / HH:MM |
| **Tempo para Detecção (TTD)** | XX min (do início ao alerta) |
| **Tempo para Resolução (TTR)** | XX min (do alerta à resolução) |
| **Relatado Por** | Nome / Sistema (monitoring, usuário, equipe) |
| **Comando do Incidente (IC)** | Nome (quem coordenou a resposta) |
| **Participantes da Análise** | Lista de nomes/papéis |

---

## 2. LINHA DO TEMPO (Timeline) — **Fatos apenas, sem julgamento**

| Horário (UTC) | Evento | Detecção / Ação | Quem | Observação |
|---|---|---|---|---|
| YYYY-MM-DD HH:MM | Início real (estimado) | — | — | Ex: Falha na API Frankfurter |
| YYYY-MM-DD HH:MM | Alerta disparado | Monitoring / Usuário | Sistema / Nome | Ex: Health check `/health` falhou |
| YYYY-MM-DD HH:MM | IC assumiu comando | Escalação Nível 2 | Nome | |
| YYYY-MM-DD HH:MM | Diagnóstico inicial | Logs / Métricas | Nome | Ex: Circuit breaker aberto |
| YYYY-MM-DD HH:MM | Ação de mitigação | Fallback PTAX ativado manual | Nome | |
| YYYY-MM-DD HH:MM | Verificação recuperação | Health check green | Nome | |
| YYYY-MM-DD HH:MM | Incidente encerrado | Confirmação estável 10min | IC | |

> **Regra**: Use logs, métricas, alertas, commits, deploys como evidência. Não use "eu achei", "fulano errou".

---

## 3. IMPACTO

| Dimensão | Detalhe | Quantificação |
|---|---|---|
| **Usuários Afetados** | % da base / nº absoluto | Ex: 100% (todos) / 47 usuários ativos |
| **Funcionalidades Indisponíveis** | Lista | Ex: `/v1/rates`, `/v1/simulate`, `/v1/invoice` |
| **SLA Violado** | Disponibilidade / Latência / Throughput | Ex: SLA 99.5% → 98.2% no mês |
| **Dados** | Perda / Corrupção / Exposição | Ex: Nenhum (apenas indisponibilidade) |
| **Negócio / Reputação** | Reclamações, cancelamentos, mídia | Ex: 3 issues GitHub, 0 cancelamentos |
| **Custo Estimado** | Horas equipe + impacto indireto | Ex: 12h equipe (IC + 3 devs) |

---

## 4. CAUSA RAIZ (Root Cause Analysis) — **Método 5 Porquês ou Fishbone**

### 4.1 Declaração da Causa Raiz (1 frase)
> **Exemplo**: "O circuit breaker do serviço de cotações abriu devido a timeout consecutivo na API Frankfurter (primária), e o fallback automático para PTAX falhou porque a variável de ambiente `PTAX_ENABLED` estava definida como `false` no ambiente de produção, impedindo a troca de provedor."

### 4.2 Árvore de Causas (5 Porquês)

| Porquê | Resposta | Evidência |
|---|---|---|
| 1. Por que o serviço ficou indisponível? | Circuit breaker abriu + fallback não ativou | Logs: `circuit_breaker.open=True`, `fallback_attempted=False` |
| 2. Por que o circuit breaker abriu? | 5 timeouts consecutivos na API Frankfurter (primária) | Métricas: `rate_provider.frankfurter.timeout.count=5` |
| 3. Por que o fallback PTAX não ativou? | Variável `PTAX_ENABLED=false` no `.env` de produção | Config audit: `grep PTAX_ENABLED .env.prod` |
| 4. Por que a variável estava `false`? | Deploy anterior (v1.2.3) removeu a flag por engano no `.env.example` | Diff: `git show v1.2.3:.env.example vs v1.2.2:.env.example` |
| 5. Por que não foi pego no deploy? | Checklist de deploy não valida variáveis de feature flags; CI não testa fallback | Runbook §Deploy checklist; CI pipeline steps |

### 4.3 Fatores Contribuintes (Contributing Factors)
- [ ] Falha de processo (checklist, revisão, validação)
- [ ] Falha de ferramenta (monitoring, alerting, CI/CD)
- [ ] Falha de arquitetura (single point of failure, acoplamento)
- [ ] Falha de comunicação (handoff, documentação, onboarding)
- [ ] Falha de capacidade (conhecimento, treinamento, documentação)
- [ ] Fator externo (provedor, rede, regulatório)
- [ ] Outro: ___________

---

## 5. AÇÕES CORRETIVAS (Implementadas Durante o Incidente)

| Ação | Descrição | Quem | Quando | Efetividade |
|---|---|---|---|---|
| 1. | Ex: Ativar PTAX manualmente via `docker exec ... env PTAX_ENABLED=true` | Nome | HH:MM | Resolveu imediato |
| 2. | | | | |
| 3. | | | | |

---

## 6. AÇÕES PREVENTIVAS (Preventive Actions) — **Para não recorrrer**

| ID | Ação Preventiva | Tipo | Responsável | Prazo | Critério de Conclusão | Status | Link PR/Issue |
|---|---|---|---|---|---|---|---|
| PA-001 | Adicionar validação de `PTAX_ENABLED` no checklist de deploy (Runbook) | Processo | agent-devops | 2026-11-20 | Checklist atualizado + revisão par a par | Planejada | |
| PA-002 | Criar teste de integração que simula falha primária e valida fallback automático | Técnico (Teste) | agent-qa-sdet | 2026-11-25 | Teste no CI green; coverage fallback path | Planejada | |
| PA-003 | Adicionar alerta específico: "Circuit breaker aberto + fallback desabilitado" | Monitoramento | agent-devops | 2026-11-18 | Alerta dispara em staging; runbook atualizado | Planejada | |
| PA-004 | Incluir variáveis de feature flag no `.env.example` com validação no CI (script) | Técnico (CI) | agent-backend-dev | 2026-11-22 | CI falha se flag obrigatória ausente | Planejada | |
| PA-005 | Revisar arquitetura: tornar fallback PTAX obrigatório (não feature flag) ou default true | Arquitetura | agent-architect | 2026-12-01 | ADR emitida/emendada; implementado | Planejada | |

> **Regra**: Cada ação preventiva deve ter **dono**, **prazo**, **critério de conclusão verificável** e **link para issue/PR de rastreamento**. Ações sem dono/prazo não são ações — são intenções.

---

## 7. LIÇÕES APRENDIDAS (Lessons Learned) — **Para o conhecimento organizacional**

| Lição | Categoria | Aplicabilidade Futura |
|---|---|---|
| Ex: Feature flags de resiliência (fallback) devem ter default `true` e validação obrigatória no deploy | Processo / Arquitetura | Todo novo provedor externo com fallback |
| Ex: Checklist de deploy deve incluir variáveis de ambiente críticas, não apenas "build passed" | Processo / Operação | Todo deploy produção |
| Ex: Testes de caos (chaos engineering) periódicos teriam pego isso | Qualidade / Teste | Próxima wave de melhoria de confiabilidade |

---

## 8. MÉTRICAS DO INCIDENTE (Para Análise de Tendência)

| Métrica | Valor | Benchmark / Meta |
|---|---|---|
| **MTTD** (Mean Time to Detect) | XX min | < 5 min (alerting) |
| **MTTR** (Mean Time to Resolve) | XX min | < 30 min (P1) |
| **MTBF** (Mean Time Between Failures) | XX dias | > 30 dias |
| **Change Failure Rate** (últimos 30 dias) | X% | < 15% |
| **Availability** (período) | XX.XX% | ≥ 99.5% |

---

## 9. ANEXOS E EVIDÊNCIAS

- [ ] Logs relevantes (links ou trechos)
- [ ] Gráficos de métricas (Grafana/Prometheus/CloudWatch screenshots)
- [ ] Diff de configuração/deploy causador
- [ ] Comunicações durante incidente (Slack/Discord export)
- [ ] Runbook seguido (ou desvios)
- [ ] Resultados de testes de regressão pós-fix

---

## 10. APROVAÇÃO E FECHAMENTO

| Papel | Nome | Assinatura / Confirmação | Data |
|---|---|---|---|
| **Incident Commander** | | | |
| **Tech Lead / Arquiteto** | | | |
| **GP / CCB** | | | |
| **Segurança (se P0)** | | | |

> **Fechamento**: Todas as ações preventivas (PA-XXX) devem ter **issue/PR criado** e **status "Planejada" ou "Em Andamento"** antes do fechamento. Acompanhamento no Status Report semanal até conclusão.

---

## 11. CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-digital-security | Criação inicial (template aprovado) |
| 1.0.1 | YYYY-MM-DD | Nome | Atualização pós-incidente PM-XXXX |