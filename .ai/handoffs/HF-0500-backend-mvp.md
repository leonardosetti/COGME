---
id: ai-handoffs-hf-0500-backend-mvp
title: 'Handoff: Scheduler de auditoria de compliance (REQ-13)'
type: handoff
version: 1.0.0
status: ativo
owner: agent-devops
derived-from:
- .ai/handoffs/HF-0500-backend-mvp.md (adequado à norma em 2026-11-06)
last-revised: '2026-11-06'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---
# Handoff: Scheduler de auditoria de compliance (REQ-13)

## Contexto

Execução de auditoria de compliance para COGME, disparada a cada 90 minutos (1:30) 24/7, substituindo o registro anterior de backend MVP. Não há push, PR nem merge pendentes; este handoff define a especificação de implementação do scheduler/temporizador.

Orquestrador: `agent-devops`.

## Tarefa

Criar scheduler/temporizador de auditoria de compliance com dois canais de disparo:

1. GitHub Actions `schedule` cron em workflow dedicado (`.github/workflows/`).
2. Timer systemd/cron local em `.ai/workflows/`.

Orquestrar scripts existentes:
- `security_scan.py`
- `registry_drift_monitor.py`
- `sync_agent_registry.py --check`
- `nexus_dispatcher.py --report`
- `sddai_verify_pipeline.py`

Gerar relatório consolidado em `docs/auditorias/` e registrar violações em `docs/auditorias/vio-register.md`.

Fail-closed: qualquer falha retorna `exit 1` e bloqueia o fluxo.

Restrições: sem PII, sem credenciais, CPU-only, FOSS-only.

## Critérios de Aceite

- [ ] Workflow GitHub Actions `schedule` cron configurado com intervalo de 90 minutos.
- [ ] Timer systemd/cron local criado em `.ai/workflows/` com intervalo de 90 minutos.
- [ ] Orquestração dos cinco scripts existentes implementada com verificação de código de saída.
- [ ] Relatório consolidado gerado em `docs/auditorias/` a cada execução.
- [ ] Violações registradas em `docs/auditorias/vio-register.md`.
- [ ] Fail-closed: falha de qualquer script retorna `exit 1`.
- [ ] Sem PII e sem credenciais nos relatórios e registros.
- [ ] Execução CPU-only e dependências FOSS-only.
- [ ] `kill_switch: inherited` mantido.

## Restrições

- kill_switch: inherited
- CPU-only, sem CUDA; provedor externo não utilizado.
- FOSS-only; sem telemetria, sem lock-in.
