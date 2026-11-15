---
id: docs-qualidade-14-regras-resolucao-incidentes
title: Regras de Resolução de Incidentes — COGME
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/08-relatorio-incidente-de-teste.md (escala P/I/S)
- docs/qualidade/13-ciclo-incidentes-bugs.md
- docs/planos/plano-granular/plano-qualidade.md (regra de ouro, gatilhos corretivos)
- .ai/specs/spec-010-qualidade-pdca-ishikawa-v1.spec.md (Ishikawa 6M)
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
- resolucao-de-incidentes
- prioridade
- impacto
- severidade
- rca
- sla
- hotfix
---

# Regras de Resolução de Incidentes — COGME

Escala de prioridade/impacto/severidade, SLA por classe, regras de RCA e regras específicas para E2E, exploratórios e hotfixes.

## 1. Escala de prioridade (P), impacto (I) e severidade (S)

| Nível | Prioridade (P) | Impacto (I) | Severidade (S) |
|---|---|---|---|
| P1 / Crítico | Correção imediata; bloqueia merge/release | Bloqueia fluxo crítico ou CI | Bloqueante: impossibilita entrega ou validação |
| P2 / Alto | Correção nesta iteração | Afeta funcionalidade importante sem bloqueio total | Maior: degrada função, workaround disponível |
| P3 / Médio | Correção no próximo ciclo | Afeta funcionalidade secundária | Menor: incômodo, sem perda de função |
| P4 / Baixo | Correção por oportunidade | Cosmético/documentação | Trivial: sem efeito sobre função |

**Regra de combinação:** prioridade final = máximo entre severidade e impacto. Ex.: severidade alta + impacto médio = P2.

## 2. SLA de correção por classe

| Classe | SLA de triagem | SLA de correção | Bloqueia marco/release? |
|---|---|---|---|
| P1 (crítico) | ≤ 24h | ≤ 24h | Sim (veredito UAT reprovado, merge travado) |
| P2 (alto) | ≤ 48h | ≤ 1 sprint | Não bloqueia, mas deve fechar antes do próximo release |
| P3 (médio) | ≤ 3 dias | próximo ciclo | Não |
| P4 (baixo) | ≤ 5 dias | por oportunidade | Não |

P1 que não for corrigido dentro do SLA escala para GP e congela novas features (gatilho corretivo, plano-qualidade §5.3).

## 3. Regras gerais de resolução

1. **Não bypassar CI:** toda correção passa por PR com CI completo verde (inclusive hotfix, salvo aprovação escrita do gatekeeper + auditoria pós-mortem).
2. **Correção mínima:** hotfix altera só o necessário para resolver o defeito; refatoração acompanha em PR separado.
3. **Regressão obrigatória:** ao fechar, executar a suíte de testes afetados + regressão dos módulos tocados.
4. **RCA obrigatório:** todo P1/P2 tem causa-raiz documentada (doc 08, seção 3) com classificação 6M (spec-010 §3.2).
5. **Não fechar sem evidência:** caso de teste que reproduz o defeito e passa após correção, anexado ao incidente.

## 4. Regras específicas por escopo

### E2E (Playwright Screenplay)
- Defeito em E2E que não reproduz em unit/integração → abrir incidente e verificar se é gap de cobertura (RTM doc 10).
- Falha intermitente no E2E → investigar estabilidade do stack efêmero antes de classificar como defeito de código.
- Correção de defeito E2E exige reexecução de todos os CT-FUNC-* (não apenas o falho).

### Exploratórios
- Defeito encontrado em sessão exploratória vira incidente com ID INC-NNN e é mapeado ao REQ/US na RTM.
- Se o defeito for de usabilidade (não de função), classificar P3/P4 e registrar como sugestão de melhoria, não bloqueante.

### Hotfixes (P1/P2)
- Abertura: branch `hotfix/inc-NNN` a partir de `main`.
- Validação: E2E do fluxo afetado + regressão da suíte relacionada + CI verde.
- Aprovação: gatekeeper + auditor (pós-mortem obrigatório para P1).
- Registro: ação corretiva no board (doc 11) e lição no ciclo PDCA correspondente (spec-010 §3.1).

## 5. Reabertura

Incidente reabre se:
- Defeito reaparecer em release subsequente (regressão).
- Correção não resolveu o sintoma reportado.
- Nova evidência invalida a resolução anterior.

Ao reabrir, o estado volta a `EM RESOLUÇÃO` e o SLA de correção é reiniciado.

## 6. Rastreabilidade

| Requisito | Regra ligada |
|---|---|
| REQ-08 (coverage gate) | não fechar incidente de cobertura sem suíte verde |
| REQ-10 (PDCA/Ishikawa) | RCA de P1/P2 alimenta Ishikawa 6M (spec-010 §3.2) |
| REQ-11 (CI ≤ 5 min) | correção não pode ampliar o tempo do CI além do orçamento |
