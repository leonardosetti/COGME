#!/usr/bin/env python3
"""Atualiza cards do backlog: move para lanes corretas, define prioridades, sizes, tags."""

import json
import subprocess
import sys

PROJECT_ID = "PVT_kwHOAOLMlM4Bg-pX"
OWNER = "leonardosetti"
PROJECT_NUMBER = 2

# Field IDs (from GraphQL introspection)
STATUS_FIELD_ID = "PVTSSF_lAHOAOLMlM4Bg-pXzhf8IdQ"  # Status field
PRIORITY_FIELD_ID = "PVTSSF_lAHOAOLMlM4Bg-pXzhf8IyQ"  # Priority field
SIZE_FIELD_ID = "PVTSSF_lAHOAOLMlM4Bg-pXzhf8IyU"  # Size field
CARDTYPE_FIELD_ID = "PVTSSF_lAHOAOLMlM4Bg-pXzhp1bXQ"  # CardType field

# Status option IDs
STATUS_BACKLOG = "f75ad846"
STATUS_READY = "61e4505c"
STATUS_IN_PROGRESS = "47fc9ee4"
STATUS_IN_REVIEW = "df73e18b"
STATUS_DONE = "98236657"

# Priority option IDs
PRIORITY_P0 = "79628723"
PRIORITY_P1 = "0a877460"
PRIORITY_P2 = "da944a9c"
PRIORITY_P3 = "01d3db4f"

# Size option IDs
SIZE_XS = "6c6483d2"
SIZE_S = "f784b110"
SIZE_M = "7515a9f1"
SIZE_L = "7515a9f1"
SIZE_XL = "db339eb2"

# Card Type option IDs
TYPE_SPEC = "2e3bfc53"
TYPE_WORK_ITEM = "9ce93586"
TYPE_ADR = "368c3b32"
TYPE_DOC = "724745b4"

# Map issue number -> GraphQL node_id (from GitHub API)
def get_issue_node_id(issue_number):
    result = subprocess.run(
        ["gh", "api", f"repos/leonardosetti/COGME/issues/{issue_number}", "--jq", ".node_id"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        return result.stdout.strip()
    return None

def get_project_item_id(issue_node_id):
    """Get the ProjectV2 item ID for an issue."""
    query = f'''
    query($projectId: ID!, $contentId: ID!) {{
      node(id: $projectId) {{
        ... on ProjectV2 {{
          items(first: 50, filterBy: {{term: "id:{issue_node_id}"}}) {{
            nodes {{
              id
              content {{ ... on Issue {{ number }} }}
            }}
          }}
        }}
      }}
    '''
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}", "-F", f"projectId=PVT_kwHOAOLMlM4Bg-pX", "-F", f"contentId={issue_node_id}"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        data = json.loads(result.stdout)
        items = data.get("data", {}).get("node", {}).get("items", {}).get("nodes", [])
        if items:
            return items[0]["id"]
    return None

def update_field(project_id, item_id, field_id, option_id):
    """Update a single-select field on a project item."""
    mutation = '''
    mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $value: String!) {
      updateProjectV2ItemFieldValue(input: {projectId: $projectId, itemId: $itemId, fieldId: $fieldId, value: {singleSelectOptionId: $value}}) {
        projectV2Item { id }
      }
    }
    '''
    result = subprocess.run([
        "gh", "api", "graphql",
        "-F", f"query={mutation}",
        "-F", f"projectId={project_id}",
        "-F", f"itemId={item_id}",
        "-F", f"fieldId={field_id}",
        "-F", f"value={option_id}"
    ], capture_output=True, text=True)
    return result.returncode == 0

def add_labels(issue_number, labels):
    """Add labels to an issue."""
    labels_str = ",".join(labels)
    subprocess.run(["gh", "issue", "edit", str(issue_number), "--add-label", labels_str], capture_output=True)

def set_milestone(issue_number, milestone_title):
    """Set milestone on an issue."""
    subprocess.run(["gh", "issue", "edit", str(issue_number), "--milestone", milestone_title], capture_output=True)

# ============================================================
# DEFINIÇÃO DOS CARDS E SUAS CONFIGURAÇÕES
# ============================================================

CARDS = [
    # CR-008: BLOQUEADOR CRÍTICO - deve ir para Ready/In Progress primeiro
    {
        "issue": 41,
        "title": "[CR-008] Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR",
        "status": STATUS_READY,  # Blocker critical - deve ser atacado primeiro
        "priority": PRIORITY_P0,
        "size": SIZE_XL,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "area:riscos", "change-request", "blocked", "sdd-ia", "must", "blocker:critical"],
        "milestone": "M1 - Arquitetura",
        "assignee": "leonardosetti",
        "description": "BLOQUEADOR CRÍTICO para todos os outros CRs. Precedência máxima. Requer parecer jurídico LGPD+GDPR, threat model, deliberação CCB (CR8-D01..D06), emenda constitucional, promoção SPEC-015→EXECUTIVA, emissão SPEC-022. Só então promover SPEC-017..021."
    },
    
    # SPECs filhas do CR-008
    {
        "issue": 42,
        "title": "[SPEC-022] Model + Migration: account_lifecycle_events",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_M,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "must", "blocked-by:41", "sdd-ia"],
        "milestone": "M1 - Arquitetura",
        "assignee": "leonardosetti",
        "description": "Parte do CR-008. Migration Alembic + model account_lifecycle_events. Bloqueado por CR-008 (#41)."
    },
    {
        "issue": 43,
        "title": "[SPEC-022] User States + Dormancy Job (365d)",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_M,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "must", "blocked-by:41", "sdd-ia"],
        "milestone": "M1 - Arquitetura",
        "assignee": "leonardosetti",
        "description": "Parte do CR-008. Estados active/dormant/deleted + job dormência 365d + reativação. Bloqueado por CR-008 (#41)."
    },
    
    # CR-002: Parent - aguarda CR-008
    {
        "issue": 35,
        "title": "[CR-002] Contas multiusuário, sessões e histórico de invoices",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_L,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "area:riscos", "change-request", "sdd-ia", "must", "blocked-by:41", "parent:cr-002"],
        "milestone": "M2 - Ambiente e Modelagem Concluídos",
        "assignee": "leonardosetti",
        "description": "Parent CR para multiusuário. Bloqueado por CR-008 (#41). Gera SPECs 017-022. Custo 264-408h."
    },
    
    # CR-003: Identidade - depende de CR-002 e CR-008
    {
        "issue": 36,
        "title": "[CR-003] Identidade, aliases, senha, sessões e recuperação",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_L,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "change-request", "sdd-ia", "area:seguranca", "must", "blocked-by:41", "blocked-by:35", "child:cr-003"],
        "milestone": "M2 - Ambiente e Modelagem Concluídos",
        "assignee": "leonardosetti",
        "description": "SPEC-017/018. Superfície de ataque nova. Requer threat model + parecer LGPD. 96-148h. Bloqueado por CR-008 e CR-002."
    },
    
    # CR-004: Perfil prestadora - depende de CR-003 e CR-008
    {
        "issue": 37,
        "title": "[CR-004] Perfil da prestadora e contas bancárias de depósito",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_M,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "change-request", "sdd-ia", "must", "blocked-by:41", "blocked-by:36", "child:cr-004"],
        "milestone": "M3 — MVP Funcional (Beta)",
        "assignee": "leonardosetti",
        "description": "SPEC-019. Perfil prestadora + contas bancárias. 68-100h. Depende de CR-003 e CR-008."
    },
    
    # CR-005: Clientes - depende de CR-003/CR-004 e CR-008
    {
        "issue": 38,
        "title": "[CR-005] Carteira de clientes e estado ativo/inativo",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_M,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "change-request", "sdd-ia", "must", "blocked-by:41", "blocked-by:36", "blocked-by:37", "child:cr-005"],
        "milestone": "M3 — MVP Funcional (Beta)",
        "assignee": "edsonsilva11",
        "description": "SPEC-020. Cadastro clientes + autocomplete. 48-68h. Depende de CR-003/004 e CR-008."
    },
    
    # CR-006: Simulações/Invoices - depende de CR-003/004/005 e CR-008
    {
        "issue": 39,
        "title": "[CR-006] Simulações salvas, histórico e ciclo de vida das invoices",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_L,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "change-request", "sdd-ia", "must", "blocked-by:41", "blocked-by:35", "blocked-by:36", "blocked-by:37", "blocked-by:38", "child:cr-006"],
        "milestone": "M4 — Encerramento e Validação Acadêmica",
        "assignee": "leonardosetti",
        "description": "SPEC-021. Simulações opt-in + histórico + ciclo invoice (draft/finalized/clone). 96-144h. Depende de CR-003/004/005 e CR-008."
    },
    
    # CR-007: Invoice bilíngue - depende de CR-006 e CR-008
    {
        "issue": 40,
        "title": "[CR-007] Invoice bilíngue PT-BR / EN",
        "status": STATUS_BACKLOG,
        "priority": PRIORITY_P0,
        "size": SIZE_S,
        "card_type": TYPE_SPEC,
        "labels": ["area:integracao", "area:escopo", "change-request", "sdd-ia", "must", "blocked-by:41", "blocked-by:39", "child:cr-007"],
        "milestone": "M4 — Encerramento e Validação Acadêmica",
        "assignee": "edsonsilva11",
        "description": "SPEC-022. Invoice bilíngue PT-BR/EN. Regra país→locale. 36-56h. Depende de CR-006 e CR-008."
    },
]

def main():
    print(f"{'='*60}")
    print("ATUALIZANDO CARDS DO BACKLOG - COGME")
    print(f"{'='*60}\n")
    
    success = 0
    failed = 0
    
    for card in CARDS:
        issue_num = card["issue"]
        print(f"\n{'─'*60}")
        print(f"Processando Issue #{issue_num}: {card['title'][:60]}...")
        
        # 1. Get node_id
        node_id = get_issue_node_id(issue_num)
        if not node_id:
            print(f"  ❌ Falha ao obter node_id para issue #{issue_num}")
            failed += 1
            continue
        print(f"  ✓ node_id: {node_id}")
        
        # 2. Get project item ID
        item_id = get_project_item_id(node_id)
        if not item_id:
            print(f"  ⚠️  Item não encontrado no projeto, tentando adicionar...")
            # Try to add to project
            result = subprocess.run([
                "gh", "api", "graphql",
                "-F", f"query=mutation($projectId: ID!, $contentId: ID!) {{ addProjectV2ItemById(input: {{projectId: $projectId, contentId: $contentId}}) {{ item {{ id }} }} }}",
                "-F", f"projectId={PROJECT_ID}",
                "-F", f"contentId={node_id}"
            ], capture_output=True, text=True)
            if result.returncode == 0:
                data = json.loads(result.stdout)
                item_id = data.get("data", {}).get("addProjectV2ItemById", {}).get("item", {}).get("id")
                print(f"  ✓ Adicionado ao projeto: {item_id}")
            else:
                print(f"  ❌ Falha ao adicionar ao projeto: {result.stderr}")
                failed += 1
                continue
        
        if not item_id:
            print(f"  ❌ Não foi possível obter item_id")
            failed += 1
            continue
        print(f"  ✓ item_id: {item_id}")
        
        # 3. Update Status
        if update_field(PROJECT_ID, item_id, STATUS_FIELD_ID, card["status"]):
            status_name = {STATUS_BACKLOG: "Backlog", STATUS_READY: "Ready", STATUS_IN_PROGRESS: "In progress", STATUS_IN_REVIEW: "In review", STATUS_DONE: "Done"}.get(card["status"], card["status"])
            print(f"  ✓ Status → {status_name}")
        else:
            print(f"  ❌ Falha ao atualizar Status")
        
        # 4. Update Priority
        if update_field(PROJECT_ID, item_id, PRIORITY_FIELD_ID, card["priority"]):
            priority_name = {PRIORITY_P0: "P0", PRIORITY_P1: "P1", PRIORITY_P2: "P2", PRIORITY_P3: "P3"}.get(card["priority"], card["priority"])
            print(f"  ✓ Priority → {priority_name}")
        
        # 5. Update Size
        if update_field(PROJECT_ID, item_id, SIZE_FIELD_ID, card["size"]):
            size_name = {SIZE_XS: "XS", SIZE_S: "S", SIZE_M: "M", SIZE_L: "L", SIZE_XL: "XL"}.get(card["size"], card["size"])
            print(f"  ✓ Size → {size_name}")
        
        # 6. Update Card Type
        if update_field(PROJECT_ID, item_id, CARDTYPE_FIELD_ID, card["card_type"]):
            type_name = {TYPE_SPEC: "SPEC", TYPE_WORK_ITEM: "Work Item", TYPE_ADR: "ADR", TYPE_DOC: "DOC"}.get(card["card_type"], card["card_type"])
            print(f"  ✓ CardType → {type_name}")
        
        # 7. Add Labels
        if card.get("labels"):
            add_labels(card["issue"], card["labels"])
            print(f"  ✓ Labels: {', '.join(card['labels'])}")
        
        # 8. Set Milestone
        if card.get("milestone"):
            set_milestone(card["issue"], card["milestone"])
            print(f"  ✓ Milestone: {card['milestone']}")
        
        # 9. Assign
        if card.get("assignee"):
            subprocess.run(["gh", "issue", "edit", str(card["issue"]), "--assignee", card["assignee"]], capture_output=True)
            print(f"  ✓ Assignee: {card['assignee']}")
        
        success += 1
        print(f"  ✅ Concluído com sucesso")
    
    print(f"\n{'='*60}")
    print(f"RESUMO: {success} sucessos, {failed} falhas")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()