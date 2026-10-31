# Pipeline de Teste e Verificação — SDDAI integrado ao COGME

Este documento descreve o pipeline acionável para teste e verificação dos componentes SDDAI (`cogme-sddai-*`) integrados ao ecossistema COGME.

## Visão Geral

O pipeline `sddai_verify_pipeline` executa 7 passos sequenciais (fail-closed) para garantir a integridade do ecossistema SDDAI:

| Passo | Comando | Objetivo |
|-------|---------|----------|
| 1 | `sync_agent_registry.py --check` | Sincroniza e verifica o roster SSOT (`.ai/agents/registry.yaml`) |
| 2 | `dag_validator.py` | Valida a topologia DAG (sem ciclos, camadas corretas) |
| 3 | `nexus_dispatcher.py --report` | Relatório do dispatcher (sem `missing_from_dag`) |
| 4 | `agent_health_check.py` | Health check dos agentes, incluindo os 5 SDDAI |
| 5 | `handoff_parser.py --dir .ai/handoffs` | Valida handoffs SDDAI (HF-0400 a HF-0404) |
| 6 | `sddai run data_optimization` | Executa o pipeline completo (loader → memory → engineer → trainer) |
| 7 | `pytest` (focado) | Testes de unidade focados no SDDAI e dispatcher |

## Execução Local

```bash
# A partir da raiz do repositório COGME
python3 scripts/sddai_verify_pipeline.py
```

### Opções

| Opção | Descrição |
|-------|-----------|
| (nenhuma) | Execução completa, exibe saída passo a passo |
| `--strict` | Retorna exit 1 se qualquer passo falhar (útil para CI) |
| `--report /tmp/relatorio.json` | Salva relatório JSON detalhado do pipeline |

### Exemplo de saída

```
PASSO 1/7 — Sincronização e verificação do roster SSOT
[OK] registry em sincronia com o disco
PASSO 2/7 — Validação da topologia DAG (dag_validator.py)
[DAG] OK: 45 slugs, topologia aciclica
...
RELATÓRIO FINAL — SDDAI VERIFY PIPELINE
============================================================
  Passo 1: roster_sync_check — ✅ PASS (rc=0)
  Passo 2: dag_validation — ✅ PASS (rc=0)
  Passo 3: dispatcher_report — ✅ PASS (rc=0)
  Passo 4: agent_health_check — ✅ PASS (rc=0)
  Passo 5: handoff_validation — ✅ PASS (rc=0)
  Passo 6: sddai_pipeline_run — ✅ PASS (rc=0)
  Passo 7: pytest_focused — ✅ PASS (rc=0)
------------------------------------------------------------
Resultado geral: SUCESSO
Passos aprovados: 7/7
```

## CI/CD (GitHub Actions)

O workflow está definido em `.github/workflows/sddai-verify.yml` e dispara em:
- `push` para `main` e `develop`
- `pull_request` para `main`
- `workflow_dispatch` (execução manual)

O job roda em `ubuntu-latest`, instala Python 3.12 + PyYAML + pytest, e executa `sddai_verify_pipeline.py --strict`.

## Componentes SDDAI Verificados

O pipeline valida especificamente os 5 agentes SDDAI:

| Agente | Slug | Camada | Componente |
|--------|------|--------|------------|
| Loader | `agent-sddai-loader` | L2 | `cogme-sddai-loader` |
| Memory | `agent-sddai-memory` | L2 | `cogme-sddai-memory` |
| Engineer | `agent-sddai-engineer` | L2 | `cogme-sddai-engineer` |
| Trainer | `agent-sddai-trainer` | L2 | `cogme-sddai-trainer` |
| CLI | `agent-sddai-cli` | L2 | `cogme-sddai-cli` |

Todos residem em `.ai/sddai/cogme_sddai_*/` e são instaláveis via `pip install -e .` a partir de seus respectivos `pyproject.toml`.

## Arquivos do Pipeline

| Arquivo | Descrição |
|---------|-----------|
| `scripts/sddai_verify_pipeline.py` | Script principal do pipeline (7 passos, fail-closed) |
| `.github/workflows/sddai-verify.yml` | Workflow GitHub Actions para CI/CD |
| `.ai/sddai/sddai` | CLI unificado do SDDAI (entry point `sddai run`) |
| `.ai/handoffs/HF-040*.md` | 5 handoffs SDDAI validados pelo parser |
| `.ai/agents/ledger.yaml` | Ledger com audit trail da integração SDDAI |

## Princípios Aplicados

- **Fail-closed:** qualquer passo com exit != 0 interrompe o pipeline.
- **Sem dependências externas:** apenas stdlib Python + PyYAML + pytest.
- **CPU-only:** nenhuma inferência CUDA/cloud; treinamento determinístico.
- **FOSS-first:** zero dependências proprietárias.
- **LGPD:** nenhum dado pessoal em artefatos de teste; uso de arquivo interno do próprio pacote SDDAI como dado de entrada.

## Histórico

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0.0 | 31/10/2026 | Criação do pipeline de verificação SDDAI integrado ao COGME |
