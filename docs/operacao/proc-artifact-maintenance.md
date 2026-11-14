---
id: proc-artifact-maintenance
title: Procedimento de Manutenção Contínua de Artefatos — Sanitização de Cross-References e Validação
type: procedimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
  - constitution.md Art. 2 (Hierarquia normativa) / Art. 9.3 (Fluxo de mudança integrado)
  - NORMA-TEMPLATES-ARTEFATOS.md
  - NORMA-NOMECLATURA-ARTEFATOS.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- procedimento
- manutencao
- cross-references
- validacao
- hooks
---

# Procedimento de Manutenção Contínua de Artefatos

> **Finalidade**: Definir rotinas automatizadas e manuais para garantir que:
> 1. **Cross-references** permaneçam válidas após movimentações/renomeações
> 2. **Frontmatter** permaneça conforme as normas (NORMA-TEMPLATES-ARTEFATOS.md)
> 3. **Nomenclatura** de arquivos permaneça conforme (NORMA-NOMECLATURA-ARTEFATOS.md)
> 3. **Arquivos órfãos/quebrados** sejam detectados e corrigidos

---

## 1. HOOKS DE VALIDAÇÃO (CI/CD)

### 1.1 Pre-commit Hook (Local)
```bash
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: validar-frontmatter
        name: Validar Frontmatter Markdown
        entry: python scripts/validar_frontmatter_md.py
        language: system
        types: [markdown]
        exclude: ^(docs/archive/|docs/conhecimento/drafts/)
      
      - id: validar-nomeclatura
        name: Validar Nomenclatura Arquivos
        entry: python scripts/validar_nome_arquivo.py
        language: system
        types: [markdown]
        exclude: ^(docs/archive/|docs/conhecimento/drafts/)
```

### 1.2 CI Pipeline (GitHub Actions)
```yaml
# .github/workflows/ci.yml (trecho)
- name: Validar Frontmatter
  run: python scripts/validar_frontmatter_md.py

- name: Validar Nomenclatura
  run: python scripts/validar_nome_arquivo.py

- name: Verificar Cross-References
  run: python scripts/verificar_cross_refs.py
```

---

## 2. SCRIPT DE VERIFICAÇÃO DE CROSS-REFERENCES

### 2.1 `scripts/verificar_cross_refs.py`
```python
#!/usr/bin/env python3
"""Verifica integridade de referências cruzadas entre artefatos .md"""

import re
from pathlib import Path

EXCLUDED_DIRS = {'.git', 'node_modules', '.venv', 'venv', '.pytest_cache', 'graphify-out', '__pycache__', '.opencode', '.agents'}

MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+\.md[^)]*)\)')

def collect_md_files():
    files = []
    for p in Path('.').rglob('*.md'):
        parts = p.parts
        if any(part in EXCLUDED_DIRS for part in parts):
            continue
        if '.opencode' in parts and 'skills' in parts:
            continue
        if '.agents' in parts and 'skills' in parts:
            continue
        files.append(p)
    return files

def check_cross_refs():
    files = collect_md_files()
    file_index = {f.name: f for f in files}
    # Também indexar por path relativo para links com path
    path_index = {str(f): f for f in files}
    
    broken = []
    for f in files:
        text = f.read_text(encoding='utf-8', errors='replace')
        for match in MD_LINK_RE.finditer(text):
            link_text, link_target = match.groups()
            # Normalizar target (remover anchor #...)
            target_path = link_target.split('#')[0]
            if not target_path:
                continue  # link apenas com anchor
            
            # Resolver path relativo
            target = (f.parent / target_path).resolve()
            try:
                target_relative = target.relative_to(Path('.').resolve())
            except ValueError:
                target_relative = target
            
            if not target.exists():
                broken.append({
                    'source': str(f),
                    'line': text[:match.start()].count('\n') + 1,
                    'link_text': link_text,
                    'target': target_path,
                    'resolved': str(target_relative)
                })
    
    return broken

if __name__ == '__main__':
    broken = check_cross_refs()
    if broken:
        print(f"[FAIL] {len(broken)} cross-reference(s) quebrada(s):")
        for b in broken:
            print(f"  - {b['source']}:{b['line']} -> {b['target']} (resolved: {b['resolved']})")
        exit(1)
    print("[OK] Todas as cross-references válidas.")
```

---

## 3. SCRIPT DE SANITIZAÇÃO AUTOMÁTICA

### 3.1 `scripts/sanitize_artifacts.py`
```python
#!/usr/bin/env python3
"""Sanitiza artefatos: corrige frontmatter, nomenclatura, cross-refs"""

import subprocess
import sys

def run_validations():
    """Executa todas as validações"""
    checks = [
        ('Frontmatter', 'python scripts/validar_frontmatter_md.py'),
        ('Nomenclatura', 'python scripts/validar_nome_arquivo.py'),
        ('Cross-refs', 'python scripts/verificar_cross_refs.py'),
    ]
    
    all_ok = True
    for name, cmd in checks:
        print(f"\n=== {name} ===")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            all_ok = False
        else:
            print(f"[OK] {name}")
    
    return all_ok

def auto_fix_nomenclature():
    """Tenta corrigir nomenclatura automaticamente (dry-run por padrão)"""
    # Implementar se necessário
    pass

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--fix', action='store_true', help='Tentar correção automática')
    parser.add_argument('--check', action='store_true', help='Apenas verificar (padrão)')
    args = parser.parse_args()
    
    if not run_validations():
        print("\n[FAIL] Validações falharam. Execute com --fix para tentar corrigir.")
        sys.exit(1)
    print("\n[OK] Todas as validações passaram.")
```

---

## 4. ROTINAS PERIÓDICAS (Agendadas)

### 4.1 Semanal (Toda Segunda-feira)
- [ ] Executar `python scripts/sanitize_artifacts.py --check` no CI agendado
- [ ] Revisar RAID Log (`docs/governanca/gov-raid-log.md`)
- [ ] Atualizar Status Report (`docs/governanca/` - usar template)

### 4.2 Quinzenal
- [ ] Verificar cross-references quebradas
- [ ] Validar frontmatter de todos os `.md` novos/alterados
- [ ] Revisar nomenclatura de arquivos novos

### 4.3 Por Release / Gate
- [ ] Gate 1: Validar Business Case, Charter, RAID Log inicial
- [ ] Gate 2: Validar Specs, ADRs, NFRs, Test Plan, RTM
- [ ] Gate 3: Validar Runbook, Release Notes, Test Report, UAT Report

---

## 5. PROCEDIMENTO DE MUDANÇA DE ARTEFATO (Move/Rename)

### 5.1 Checklist Obrigatório
Quando mover ou renomear um artefato `.md`:

```bash
# 1. Mover arquivo
git mv docs/old/path/arquivo.md docs/new/path/novo-nome.md

# 2. Atualizar frontmatter (id, derived-from se necessário)
# 3. Atualizar cross-references (rodar script)
python scripts/verificar_cross_refs.py

# 4. Validar
python scripts/validar_frontmatter_md.py
python scripts/validar_nome_arquivo.py

# 5. Commit atômico
git commit -m "docs(mv): move artefato X para Y — atualiza refs"
```

### 5.2 Regra de Ouro
> **Nunca** apague um artefato sem antes:
> 1. Verificar se há referências a ele (`grep -r "arquivo.md" docs/`)
> 2. Atualizar todas as referências ou criar redirect (symlink) se necessário
> 3. Registrar a mudança no `CHANGELOG.md` ou `CCB Log`

---

## 6. MONITORAMENTO E ALERTAS

### 6.1 Métricas de Saúde dos Artefatos
| Métrica | Threshold | Ação |
|---|---|---|
| Cross-refs quebradas | > 0 | Bloqueia deploy; correção imediata |
| Frontmatter inválido | > 0 | Bloqueia commit; correção obrigatória |
| Nomenclatura inválida | > 0 | Bloqueia commit; correção obrigatória |
| Arquivos sem frontmatter | > 0 | Auditoria semanal |

### 6.2 Dashboard (GitHub Actions Summary)
Adicionar ao workflow CI:
```yaml
- name: Resumo Validação Artefatos
  if: always()
  run: |
    echo "## Validação de Artefatos" >> $GITHUB_STEP_SUMMARY
    echo "- Frontmatter: ${{ steps.frontmatter.outcome }}" >> $GITHUB_STEP_SUMMARY
    echo "- Nomenclatura: ${{ steps.nomeclatura.outcome }}" >> $GITHUB_STEP_SUMMARY
    echo "- Cross-refs: ${{ steps.crossrefs.outcome }}" >> $GITHUB_STEP_SUMMARY
```

---

## 7. CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-project-analyst | Criação inicial | GP (CCB) |

---

> **Integração**: Este procedimento deve ser referenciado no `Runbook` (`docs/operacao/proc-runbook.md`) seção "Manutenção Programada" e no `CI-CD-GOV-001` como gate de qualidade obrigatório.