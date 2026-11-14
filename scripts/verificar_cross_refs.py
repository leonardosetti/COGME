#!/usr/bin/env python3
"""verificar_cross_refs.py — Verifica integridade de referências cruzadas entre artefatos .md

Uso:
  python scripts/verificar_cross_refs.py          # valida, exit 1 se houver quebradas
  python scripts/verificar_cross_refs.py --fix    # tenta corrigir automaticamente (futuro)
"""

import re
import sys
from pathlib import Path

ROOT = Path(".")
EXCLUDED_DIR_NAMES = {
    ".git", "node_modules", ".venv", "venv", ".pytest_cache", "graphify-out",
    "__pycache__",
}
EXCLUDED_PREFIXES = (".opencode/skills/", ".agents/skills/")

# Regex para links Markdown: [texto](caminho.md) ou [texto](caminho.md#anchor)
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)')

def collect_md_files() -> list[Path]:
    files: list[Path] = []
    for p in ROOT.rglob("*.md"):
        if p.is_symlink():
            continue
        parts = p.parts
        if any(part in EXCLUDED_DIR_NAMES for part in parts):
            continue
        if any(prefix in str(p) for prefix in EXCLUDED_PREFIXES):
            continue
        # Em .opencode/, só agentes COGME nativos
        if ".opencode" in parts:
            idx = parts.index(".opencode")
            resto = parts[idx + 1:]
            if not (len(resto) >= 2 and resto[0] == "agents" and resto[1].startswith("agent-")):
                continue
        files.append(p)
    files.sort()
    return files

def check_cross_refs() -> list[dict]:
    files = collect_md_files()
    # Índice por path relativo para resolução rápida
    path_index = {str(f.relative_to(ROOT)): f for f in files}
    # Também indexar por nome do arquivo para links sem path
    name_index = {}
    for f in files:
        name_index.setdefault(f.name, []).append(f)
    
    broken = []
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        for match in MD_LINK_RE.finditer(text):
            link_text, link_target = match.groups()
            # Separar path do anchor
            if '#' in link_target:
                target_path, anchor = link_target.split('#', 1)
            else:
                target_path, anchor = link_target, None
            
            if not target_path:
                continue  # link apenas com anchor (#section)
            
            # Resolver path relativo ao arquivo fonte
            source_dir = f.parent
            target = (source_dir / target_path).resolve()
            
            try:
                target_relative = target.relative_to(ROOT.resolve())
            except ValueError:
                target_relative = target
            
            if not target.exists():
                # Tentar buscar por nome do arquivo (link sem path)
                target_name = Path(target_path).name
                candidates = name_index.get(target_name, [])
                if candidates:
                    # Encontrou por nome, mas path diferente - avisar
                    broken.append({
                        'source': str(f.relative_to(ROOT)),
                        'line': text[:match.start()].count('\n') + 1,
                        'link_text': link_text,
                        'target': link_target,
                        'issue': f'Arquivo existe mas em outro path: {[str(c.relative_to(ROOT)) for c in candidates]}',
                        'type': 'path_mismatch'
                    })
                else:
                    broken.append({
                        'source': str(f.relative_to(ROOT)),
                        'line': text[:match.start()].count('\n') + 1,
                        'link_text': link_text,
                        'target': link_target,
                        'issue': 'Arquivo não encontrado',
                        'type': 'not_found'
                    })
    
    return broken

def main() -> int:
    broken = check_cross_refs()
    if broken:
        print(f"[FAIL] {len(broken)} cross-reference(s) quebrada(s):")
        for b in broken:
            print(f"  - {b['source']}:{b['line']} -> {b['target']}")
            print(f"    {b['issue']}")
        return 1
    print("[OK] Todas as cross-references válidas.")
    return 0

if __name__ == "__main__":
    sys.exit(main())