#!/usr/bin/env python3
"""generate_user_stories.py — Gera User Stories/Epics GitHub Issues a partir de Specs ratificadas.

Uso:
  python scripts/generate_user_stories.py --spec-dir .ai/specs --dry-run
  python scripts/generate_user_stories.py --spec-dir .ai/specs --create
"""

import argparse
import re
import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime

SPEC_DIR = Path(".ai/specs")
RATIFIED_SPEC_PATTERN = re.compile(r'spec-(\d+)-([^.]+)\.spec\.md$')

# Mapeamento de spec_id -> informações para User Story
SPEC_METADATA = {
    "004": {
        "title": "Backend MVP - API Rates, Simulate, Invoice",
        "epic": "M1 - MVP Core",
        "area": "integracao",
        "priority": "P0",
        "estimate": 13,
        "labels": ["area:integracao", "area:backend", "epic", "must"],
        "ac": [
            "GET /v1/rates/{currency} retorna cotação com fonte e timestamp",
            "POST /v1/simulate converte valor com latência ≤2s",
            "POST /v1/invoice gera PDF bilingue PT/EN ≤3s",
            "GET /health, /health/db, /health/metrics respondem corretamente"
        ]
    },
    "008": {
        "title": "Frontend Web Responsiva - Simulador + Invoice View",
        "epic": "M1 - MVP Core",
        "area": "frontend",
        "priority": "P0",
        "estimate": 8,
        "labels": ["area:frontend", "area:ux", "epic", "must"],
        "ac": [
            "Página inicial com simulador funcional (Hero + Features + CTA)",
            "Visualização de Invoice PDF com botão download",
            "Responsivo: breakpoints 375/768/1024/1440",
            "Acessibilidade WCAG 2.1 AA (axe-core 0 violações)"
        ]
    },
    "007": {
        "title": "Invoice Data Model - Schema + Templates PT/EN",
        "epic": "M1 - MVP Core",
        "area": "integracao",
        "priority": "P0",
        "estimate": 5,
        "labels": ["area:integracao", "area:backend", "epic", "must"],
        "ac": [
            "Tabela invoices com campos completos (owner_user_id, client_id, simulation_id, status, locale, client_country_code)",
            "Templates Jinja2: invoice_pt_br.html + invoice_en.html com macros compartilhadas",
            "Numeração sequencial INV-YYYY-NNNN sem PostgreSQL Sequence",
            "Snapshot de cotação e dados do cliente na invoice finalizada"
        ]
    },
    "009": {
        "title": "UAT Produto - Critérios de Aceite + Testes E2E",
        "epic": "M1 - Qualidade",
        "area": "qualidade",
        "priority": "P1",
        "estimate": 8,
        "labels": ["area:qualidade", "area:uat", "epic", "must"],
        "ac": [
            "Cenários Gherkin para REQ-01 a REQ-10",
            "E2E: Simulador → Resultado → Invoice PDF",
            "E2E: Fallback automático Frankfurter→PTAX",
            "Relatório UAT com evidências por critério"
        ]
    },
    "006": {
        "title": "NFRs Consolidados - 28 Requisitos Não-Funcionais ISO 25010",
        "epic": "M1 - Arquitetura",
        "area": "arquitetura",
        "priority": "P0",
        "estimate": 5,
        "labels": ["area:arquitetura", "area:nfr", "epic", "must"],
        "ac": [
            "Performance: P95 simulate ≤2s, PDF ≤3s",
            "Security: 0 High/Crit vulns, 0 secrets, Argon2id OWASP",
            "Reliability: Circuit Breaker, Availability ≥99.5%",
            "Maintainability: Coverage ≥80%, Arquitetura ortogonal"
        ]
    },
    "011": {
        "title": "CI/CD Pipeline - Fail-Closed + FOSS + SDD/DAG Validation",
        "epic": "M1 - DevOps",
        "area": "operacao",
        "priority": "P0",
        "estimate": 8,
        "labels": ["area:operacao", "area:ci", "epic", "must"],
        "ac": [
            "Kill Switch check (Art. 4.6)",
            "FOSS compliance (0 non-OSI deps)",
            "SDD/DAG validation (46 agents promulgados)",
            "Agent Health check (contratos válidos)",
            "Test Suite (coverage ≥80%)"
        ]
    },
    "010": {
        "title": "Qualidade PDCA + Ishikawa - 12 PDCAs + 6M Ishikawa",
        "epic": "M1 - Qualidade",
        "area": "qualidade",
        "priority": "P1",
        "estimate": 5,
        "labels": ["area:qualidade", "area:pdca", "epic", "must"],
        "ac": [
            "12 PDCAs documentados (Plan-Do-Check-Act)",
            "6M Ishikawa (Mão de obra, Máquina, Método, Material, Meio Ambiente, Medição)",
            "Integração com Quality Gates CI/CD",
            "Métricas de qualidade rastreadas no Kanban"
        ]
    },
    "005": {
        "title": "Container Layers - Docker Compose Multi-Stage",
        "epic": "M1 - Infraestrutura",
        "area": "operacao",
        "priority": "P0",
        "estimate": 5,
        "labels": ["area:operacao", "area:infra", "epic", "must"],
        "ac": [
            "db (PostgreSQL 15) + migrate (Alembic) + back (FastAPI) + front (Nginx/Jinja2) + proxy (Nginx)",
            "Redes isoladas: cogme-internal + cogme-external",
            "Usuários não-root, base images por digest",
            "Health checks em todos containers"
        ]
    },
    "003": {
        "title": "Métricas de Fluxo - Cycle Time, Throughput, WIP, Coverage (substituem EVM)",
        "epic": "M1 - Métricas",
        "area": "cronograma",
        "priority": "P1",
        "estimate": 3,
        "labels": ["area:cronograma", "area:metricas", "epic", "must"],
        "ac": [
            "Cycle Time médio ≤3 dias",
            "Throughput ≥5 cards/semana",
            "WIP ≤9 (3×3 pessoas)",
            "Coverage ≥80% (por push CI)"
        ]
    },
    "001": {
        "title": "Stack Tecnológica FOSS - Python/FastAPI/PostgreSQL/Docker/Nginx/Jinja2/HTMX/Tailwind/llama.cpp/Qwen",
        "epic": "M1 - Stack",
        "area": "arquitetura",
        "priority": "P0",
        "estimate": 8,
        "labels": ["area:arquitetura", "area:stack", "epic", "must"],
        "ac": [
            "100% FOSS, zero custo recorrente",
            "PostgreSQL 15+ canônico (não SQLite)",
            "llama.cpp + Qwen3-30B-A3B Q4_K_M CPU-only",
            "Docker Compose + Nginx proxy + Tailscale"
        ]
    },
    "002": {
        "title": "Kanban como Método de Execução - Colunas, WIP Limits, Rituais",
        "epic": "M1 - Processo",
        "area": "integracao",
        "priority": "P0",
        "estimate": 3,
        "labels": ["area:integracao", "area:processo", "epic", "must"],
        "ac": [
            "Colunas: Backlog → Ready → In Progress → Code Review → Done",
            "WIP Limits: ≤3 cards/pessoa",
            "Rituais: Daily async, Weekly sync, Gate reviews, Retrospectivas",
            "Mapeamento Domínios PMBOK 7ª → Kanban"
        ]
    },
    "012": {
        "title": "Rastreabilidade Prompts SDD - Req→Spec→Impl→Test→AC",
        "epic": "M1 - SDD",
        "area": "integracao",
        "priority": "P1",
        "estimate": 5,
        "labels": ["area:integracao", "area:sdd", "epic", "must"],
        "ac": [
            "RTM automatizado (CSV + validação CI)",
            "Prompts versionados com parcel.dod",
            "Nenhum código em main sem rastreabilidade completa",
            "Gap/Gold Plating detection automatizado"
        ]
    },
}

def get_existing_issues():
    """Busca issues existentes no GitHub para evitar duplicatas."""
    result = subprocess.run(
        ["gh", "issue", "list", "--json", "number,title,labels", "--limit", "200"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return {}
    issues = json.loads(result.stdout)
    existing = {}
    for issue in issues:
        title = issue['title']
        labels = [l['name'] for l in issue['labels']]
        existing[title] = {"number": issue['number'], "labels": labels}
    return existing

def create_issue(spec_id, metadata, dry_run=True):
    """Cria User Story/Epic Issue no GitHub."""
    title = f"[US-{spec_id}] {metadata['title']}"
    
    # Verifica se já existe
    existing = get_existing_issues()
    if title in existing:
        print(f"⏭️  Já existe: {title} (#{existing[title]['number']})")
        return existing[title]['number']
    
    labels_str = ",".join(metadata['labels'])
    epic = metadata['epic']
    area = metadata['area']
    priority = metadata['priority']
    estimate = metadata['estimate']
    ac = "\n".join([f"- [ ] {c}" for c in metadata['ac']])
    
    body = f"""## User Story: {metadata['title']}

**Épico**: {epic}  
**Área**: {area}  
**Prioridade**: {priority}  
**Estimativa**: {estimate} SP  
**Spec Fonte**: spec-{spec_id} (ratificada)  
**Rastreabilidade**: RTM → REQ ↔ SPEC-{spec_id} ↔ IMPL ↔ TEST ↔ AC

---

### Critérios de Aceite
{ac}

---

### Definition of Done
- [ ] Código implementado conforme Spec-{spec_id}
- [ ] Testes: Unit (≥80%) + Integration + E2E
- [ ] Quality Gates: 8/8 verdes (Lint, Unit, Int, E2E, Perf, Sec, FOSS, A11y, Cross-refs)
- [ ] Code Review: 1 aprovação humana + Agent Review
- [ ] Deploy Staging + Smoke Tests
- [ ] Gate 3 (CCB Go/No-Go)
- [ ] Deploy Produção + Health Checks
- [ ] Release Notes + RTM atualizado
- [ ] Kanban movido Done + Issue fechada
- [ ] Ratificação CCB + Hash + Promulgação

---

### Rastreabilidade
- **Spec Fonte**: `.ai/specs/spec-{spec_id}-*.spec.md`
- **RTM**: `docs/planos/plan-rtm.md` (REQ ↔ SPEC-{spec_id} ↔ IMPL ↔ TEST ↔ AC)
- **CR Relacionado**: (se aplicável)
- **Quality Gates**: CI/CD Pipeline (8 Gates)

---

**Estimativa**: {estimate} Story Points  
**Sprint/Marco**: {epic}  
**Owner**: Área {area}"""

    if dry_run:
        print(f"\n{'='*60}")
        print(f"DRY-RUN: {title}")
        print(f"Labels: {labels_str}")
        print(f"Body preview (first 500 chars):")
        print(body[:500] + "...")
        return None

    # Cria issue via gh CLI
    cmd = [
        "gh", "issue", "create",
        "--title", title,
        "--body", body,
        "--label", labels_str,
        "--milestone", epic
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        # Extrai número da issue da URL retornada
        url = result.stdout.strip()
        issue_num = url.split("/")[-1]
        print(f"✅ Criado: {title} (#{issue_num})")
        return issue_num
    else:
        print(f"❌ Erro ao criar {title}: {result.stderr}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Gera User Stories/Epics a partir de Specs ratificadas")
    parser.add_argument("--spec-dir", default=".ai/specs", help="Diretório das specs")
    parser.add_argument("--dry-run", action="store_true", help="Apenas mostra o que seria criado")
    parser.add_argument("--create", action="store_true", help="Cria as issues no GitHub")
    parser.add_argument("--spec", help="Criar apenas uma spec específica (ex: 004)")
    args = parser.parse_args()

    if not args.dry_run and not args.create:
        print("Use --dry-run ou --create")
        return 1

    created = 0
    skipped = 0

    for spec_id, metadata in SPEC_METADATA.items():
        if args.spec and spec_id != args.spec:
            continue
        
        # Verifica se spec está ratificada (arquivo existe em .ai/specs/)
        spec_file = Path(args.spec_dir) / f"spec-{spec_id}-*.spec.md"
        matches = list(Path(args.spec_dir).glob(f"spec-{spec_id}-*.spec.md"))
        if not matches:
            print(f"⏭️  Spec {spec_id} não ratificada (arquivo não encontrado em {args.spec_dir})")
            skipped += 1
            continue

        result = create_issue(spec_id, metadata, dry_run=args.dry_run)
        if result:
            created += 1
        elif result is None and not args.dry_run:
            skipped += 1

    print(f"\n{'='*60}")
    print(f"Resumo: {created} criadas, {skipped} puladas")
    return 0

if __name__ == "__main__":
    sys.exit(main())