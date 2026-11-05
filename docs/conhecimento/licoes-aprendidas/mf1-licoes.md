---
id: licoes-aprendidas-mf1-licoes
title: Mf1 Licoes
version: '3.0'
class: conhecimento
status: arquivado
owner: agent-project-analyst
derived-from:
- docs/conhecimento/licoes-aprendidas/mf1-licoes.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- licoes-aprendidas
- docs
- normalizado
---
## Lição Aprendida — LA-001: Reestruturação de Repositório em Paralelo com Produção

**Data**: 22/09/2026
**Macro-Fase**: MF1 (Fundação)
**Domínio PMBOK 7ª**: Trabalho do Projeto + Entrega

### O que aconteceu
A reestruturação formal do repositório (aderência à stack SDD canônica) foi executada em paralelo com produção ativa de diagramas e textos de projeto. Durante a movimentação de arquivos (mv do sistema + git add -A), alguns artefatos recentes foram perdidos ou deslocados para localizações incorretas.

### Causa raiz
1. Ausência de branch dedicada para reestruturação (operação em `main` direta)
2. Uso de `mv` do sistema em vez de `git mv` (perda de rastreabilidade de rename)
3. Execução de `git add -A` sem verificação prévia da árvore de destino
4. Produção ativa de artefatos durante a janela de reestruturação

### Impacto
- Perda de 1-2 diagramas recentes (fig-02-fluxo-kanban.mmd.png, possivelmente 1.svg)
- Deslocamento temporário de diagramas canônicos para archive (corrigido em commit subsequente)
- Necessidade de retrabalho estimado em 2-3h

### Ação corretiva (imediata)
- Commit corretivo `fix(diagramas)` para restaurar localização canônica
- Verificação via `git reflog` para recuperação de artefatos perdidos
- Retrabalho priorizado dos itens P0-P2

### Ação preventiva (futuro)
- **Regra**: Reestruturações de diretório SEMPRE em branch dedicada (`chore/restructure-*`)
- **Regra**: Usar `git mv` em vez de `mv` para qualquer movimentação de arquivo versionado
- **Regra**: Congelar produção de artefatos durante reestruturação (janela de manutenção)
- **Regra**: Verificar `tree` da estrutura de destino ANTES de `git add -A`
- **Regra**: Commit único de reestruturação com mensagem descritiva + tag de rollback

### Rastreabilidade
- Commits: `7121d12`, `1aa1515`
- OKB v3.0 §3.2 (SSOT documental)
- Glossário §5 (Stack SDD)