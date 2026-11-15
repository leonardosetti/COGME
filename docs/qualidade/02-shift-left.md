---
id: docs-qualidade-02-shift-left
title: Shift-Left — Qualidade Inserida no Início do Ciclo
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/planos/plano-granular/plano-qualidade.md (§5.2, §5.4, §5.5.1)
- docs/qualidade/00-contexto-disciplina-qualidade.md (§3.2)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- shift-left
- qualidade-precoce
- gates-de-qualidade
- ci
---

# Shift-Left — COGME

Shift-Left significa mover atividades de qualidade (revisão, teste, validação de segurança, conformidade) para a esquerda do ciclo de vida: o mais cedo possível, antes do código chegar à produção ou mesmo antes de ser escrito.

## Princípio

Defeito custo de correção cresce quanto mais tarde é encontrado. No COGME, a detecção ocorre no commit, não na UAT. Qualquer PR sem cobertura de teste para o código novo é rejeitado no gate de revisão.

## Onde o Shift-Left acontece no COGME

| Momento do ciclo | Atividade de Shift-Left | Artefato / ferramenta | Gate |
|---|---|---|---|
| Requisito | Requisito escrito com critérios de aceite GWT e rastreável a REQ | spec, US, RTM | DoR do card |
| Antes/durante o código | Teste unitário escrito para a funcionalidade | `tests/unit` (pytest) | Cobertura do módulo |
| Pull Request | Análise estática: lint, tipos, frontmatter, nomes de arquivo | flake8, mypy, scripts de validação | CI job `lint` |
| Pull Request | Análise de segurança e conformidade FOSS | `scripts/security_scan.py`, pip-audit | CI jobs `foss-compliance` |
| Pull Request | Validação de contratos de agente e DAG SDD | `validate_nexus_yaml.py`, `dag_validator.py` | CI job `sdd-validation` |
| Pull Request | Testes unit + integração com cobertura ≥ 95%, zero skips | `pytest --cov=src --cov-fail-under=95` | CI job `test-suite` |
| Pull Request | Code review obrigatório + tasklist (ADR-004) | Revisão humana | Gatekeeper (merge) |
| Antes da UAT | Execução dos fluxos críticos por ambiente de camadas | UAT rodada 001 (14/14 PASS) | Veredito binário |

## Como o COGME aplica Shift-Left na prática

1. **Critérios de aceite antes do código:** todo card entra em `Ready` apenas com DoR completo (DoR gate rigoroso, Ishikawa-3 ISH3-MET-01). Nenhum desenvolvimento sem requisito rastreável.
2. **Teste como especificação executável:** os testes de unidade e integração são a especificação viva dos requisitos REQ-01 a REQ-07 (ex: `test_rate_service_req07`, `test_simulate_spec_section2_example_gives_exact_strings_req02`).
3. **Falha rápido no CI:** o job `test-suite` bloqueia o merge se coverage < 95% ou houver teste pulado (zero-skipping). O job `lint` bloqueia se flake8/mypy/frontmatter falharem. O job `foss-compliance` bloqueia se houver referência não-FOSS ou credencial versionada.
4. **Segurança à esquerda:** `security_scan.py` e `pip-audit` rodam em cada push, antes dos testes; qualquer alerta é investigado (três falsos positivos já foram investigados e corrigidos via auditorias extraordinárias AUD-2610-09/10/11).
5. **SDD à esquerda:** contratos de agente, topologia DAG e health check validados no CI antes do merge (`sdd-validation`, `agent-health`).

## Métricas de Shift-Left

| Métrica | Meta | Frequência |
|---|---|---|
| Cobertura sobre `src/` | ≥ 95% | Por push (CI) |
| Testes pulados | 0 | Por push (CI) |
| Tempo do feedback lint+testes | ≤ 5 min | Por push (REQ-11) |
| Defeitos encontrados após merge | 0 (meta) | Por marco |

## Rastreabilidade

| Fonte | Onde |
|---|---|
| plano-qualidade.md §5.2 (abordagem 3 dimensões), §5.4.2 (testes), §5.5.1 (CI) | §Princípio, §Onde, §Métricas |
| spec-011 (REQ-11, CI ≤ 5 min) | §Métricas |
| Constitution (P-06, gates de qualidade) | §Onde (CI jobs) |
