#!/usr/bin/env python3
"""auditoria_compliance.py — Orquestrador de auditoria de compliance COGME (TA-0100 / HF-0500).

Executa, em ordem e com fail-closed:
  1. security_scan.py
  2. registry_drift_monitor.py --strict
  3. sync_agent_registry.py --check
  4. nexus_dispatcher.py --report
  5. sddai_verify_pipeline.py

Gera relatorio consolidado em docs/auditorias/ e registra violacoes
(append-only) em docs/auditorias/vio-register.md.

Qualquer passo com exit != 0 interrompe o pipeline e retorna 1 (fail-closed).

Uso:
    python3 scripts/auditoria_compliance.py          # execucao completa
    python3 scripts/auditoria_compliance.py --report  # salva JSON em docs/auditorias/

Restricoes: sem PII, sem credenciais, CPU-only, FOSS-only (stdlib Python).
kill_switch: inherited
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
AUDITORIAS = ROOT / "docs" / "auditorias"
VIO_REGISTER = AUDITORIAS / "vio-register.md"

PASSOS = [
    ("security_scan.py", [sys.executable, str(SCRIPTS / "security_scan.py"), "--strict", "--report", None]),
    ("registry_drift_monitor.py", [sys.executable, str(SCRIPTS / "registry_drift_monitor.py"), "--strict", "--report", None]),
    ("sync_agent_registry.py", [sys.executable, str(SCRIPTS / "sync_agent_registry.py"), "--check"]),
    ("nexus_dispatcher.py", [sys.executable, str(SCRIPTS / "nexus_dispatcher.py"), "--report"]),
    ("sddai_verify_pipeline.py", [sys.executable, str(SCRIPTS / "sddai_verify_pipeline.py"), "--strict"]),
]


def proximo_vio_numero() -> int:
    """Lê o ultimo VIO-NNN do registro e retorna o proximo numero."""
    if not VIO_REGISTER.exists():
        return 1
    ultimo = 0
    import re
    for line in VIO_REGISTER.read_text(encoding="utf-8").splitlines():
        m = re.search(r"\|\s*(VIO-(\d+))\s*\|", line)
        if m:
            n = int(m.group(2))
            if n > ultimo:
                ultimo = n
    return ultimo + 1


def append_vio(violacoes: list[dict]) -> None:
    """Append de linhas VIO-NNN ao registro (nunca reescreve linhas existentes)."""
    if not violacoes:
        return
    agora = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    n = proximo_vio_numero()
    linhas = []
    for v in violacoes:
        linhas.append(
            f"| VIO-{n:03d} | {agora} | scheduler auditoria compliance (TA-0100) | "
            f"falha no passo '{v['passo']}' (exit {v['rc']}) | "
            f"execucao agendada de auditoria compliance; passo retornou nao-zero | ABERTO |\n"
        )
        n += 1
    with VIO_REGISTER.open("a", encoding="utf-8") as fh:
        fh.writelines(linhas)


def run_passos(report_path: Path | None) -> tuple[list[dict], list[dict]]:
    """Executa os passos em ordem. Retorna (passos_ok, violacoes)."""
    resultados = []
    violacoes = []
    for nome, cmd in PASSOS:
        # substitui o placeholder do --report por um caminho por passo
        cmd = [c if c is not None else str(AUDITORIAS / f"relatorio-{nome}.json") for c in cmd]
        try:
            proc = subprocess.run(
                cmd, cwd=ROOT, capture_output=True, text=True,
            )
            rc = proc.returncode
            stdout = proc.stdout
            stderr = proc.stderr
        except FileNotFoundError:
            rc = 127
            stdout = ""
            stderr = f"script nao encontrado: {cmd[1]}"
        ok = rc == 0
        resultados.append({
            "passo": nome,
            "rc": rc,
            "ok": ok,
            "stdout_tail": stdout[-2000:] if stdout else "",
            "stderr_tail": stderr[-2000:] if stderr else "",
        })
        if not ok:
            violacoes.append({"passo": nome, "rc": rc})
            break  # fail-closed: para no primeiro passo com falha
    return resultados, violacoes


def salvar_relatorio(resultados: list[dict], overall_ok: bool, report_path: Path) -> None:
    agora = datetime.now(timezone.utc).isoformat()
    relatorio = {
        "pipeline": "auditoria_compliance",
        "versao": "1.0.0",
        "executado_em": agora,
        "ok": overall_ok,
        "passos": resultados,
    }
    AUDITORIAS.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(relatorio, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(relatorio, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Orquestrador de auditoria de compliance COGME (fail-closed)")
    parser.add_argument("--report", action="store_true",
                        help="salva relatorio JSON em docs/auditorias/")
    args = parser.parse_args()

    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    report_path = AUDITORIAS / f"aud-{ts}-auditoria-compliance.json"

    resultados, violacoes = run_passos(report_path if args.report else None)
    overall_ok = len(violacoes) == 0

    if args.report:
        salvar_relatorio(resultados, overall_ok, report_path)
        print(f"[RELATORIO] {report_path}")

    if violacoes:
        append_vio(violacoes)
        print(f"[FALHA] {len(violacoes)} passo(s) com falha — registro VIO atualizado", file=sys.stderr)
        return 1

    print("[OK] auditoria compliance concluida sem falhas", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
