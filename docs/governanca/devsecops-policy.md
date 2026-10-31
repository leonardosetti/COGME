---
id: DEVSECOPS-001
title: Política DevSecOps — COGME
version: 1.0.0
status: ratified
date: 2026-10-31
decisor: GP Leonardo (CCB único)
domain: DevSecOps, Segurança (P-07), Qualidade (P-06), Governança (Art. 4)
derived-from:
  - constitution.md v1.2.1 (Art. 4.6, 4.7, P-01..P-13, Art. 7)
  - AFA-ULTIMATE v1.3.0-FINAL (Kill Switch, FAIL-CLOSED)
  - OWASP ASVS-lite (referência, não norma autônoma)
lgpd-class: n/a
jurisdiction: LGPD primária (Brasil)
---

# Política DevSecOps — COGME

## 1. Propósito

Definir as práticas de segurança, devops e governança aplicadas aos pipelines de CI/CD e ao ecossistema de agentes do COGME, assegurando conformidade com a Constituição e os princípios inalienáveis (Art. 3).

## 2. Princípios DevSecOps Aplicados

### 2.1. Shift-Left Security

Verificações de segurança executam **antes** de qualquer passo funcional:

1. **Kill Switch** — verifica se não há veto constitucional ativo
2. **FOSS compliance** — valida stack FOSS-only, sem CUDA, sem cloud inference
3. **Credential scan** — verifica ausência de credenciais reais versionadas
4. **SDD/DAG** — valida topologia de agentes e contratos YAML
5. **Agent health** — verifica saúde do roster
6. **Testes** — valida qualidade do código

### 2.2. Fail-Closed por Padrão

Todo pipeline é fail-closed: qualquer passo com `exit != 0` interrompe a execução imediatamente. Não há "continue on error" em nenhum workflow.

### 2.3. Zero Secrets in Repository

Nenhuma credencial real, token, chave de API ou segredo pode ser versionado. Apenas chaves dummy (ex: `sk-local-dummy-key`) são admitidas para serviços locais (Art. 7.2).

### 2.4. Local-First Compute

Toda inferência e processamento ocorre localmente (hardware AMD 8700G, 58GB RAM, llama.cpp CPU-only). Provedores de nuvem em free tier são admitidos apenas para tarefas não sensíveis, sem envio de código-fonte, especificações, handoffs ou dados pessoais (P-02, P-03).

### 2.5. LGPD by Design

Nenhum PII (dados pessoais identificáveis) é incluído em artefatos técnicos de agentes, workflows CI/CD ou relatórios de pipeline. O ledger mantém apenas task IDs (sem nomes civis) (P-04, Art. 7.3).

## 3. Matriz de Controles

| Controle | Implementação | Pipeline | Frequência |
|----------|--------------|----------|------------|
| Kill Switch check | `kill_switch.trigger` ausente | CI, SDDAI Verify | Cada execução |
| FOSS compliance | grep CUDA/cloud/inference | CI | Cada execução |
| Credential scan | grep sk_live/AKIA/secret_key | CI | Cada execução |
| SDD validation | `validate_nexus_yaml.py` | CI | Cada execução |
| DAG validation | `dag_validator.py --strict` | CI | Cada execução |
| Agent health | `agent_health_check.py --strict` | CI | Cada execução |
| Test suite | `pytest tests/` | CI | Cada execução |
| SDDAI Verify | `sddai_verify_pipeline.py --strict` | SDDAI Verify | Cada execução |

## 4. Regras de Engajamento

### 4.1. Sem Bypassing

Não é permitido desabilitar, pular ou contornar qualquer etapa de segurança nos pipelines. O Bypass Protocol **não se aplica** a infraestrutura de CI/CD.

### 4.2. Sem Cloud para Inferência

A inferência de modelo ocorre exclusivamente localmente (llama.cpp, CPU-only). GitHub Actions runners são usados apenas para execução de scripts de validação, nunca para inferência de IA.

### 4.3. Sem Dados Sensíveis em Workflows

Os workflows CI/CD não processam, não armazenam e não transmitem dados pessoais, segredos, código-fonte proprietário ou handoffs sensíveis.

## 4. Auditoria e Traces

Cada execução de pipeline gera:
- Relatório JSON estruturado (quando aplicável)
- Entrada no ledger `.ai/agents/ledger.yaml`
- Hash do commit Git associado

Auditorias ocorrem a cada milestone (M1-M4) ou sob demanda do GP/CCB.

## 5. Assinatura

| Campo | Valor |
|-------|-------|
| Decisor | GP Leonardo — CCB de membro único |
| Data | 31/10/2026 |
| Instrumento | Prompt expresso do CCB + este documento |
| Status | VIGENTE |
