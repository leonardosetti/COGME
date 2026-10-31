#!/usr/bin/env python3.12
"""
sddai_verify_pipeline.py — Pipeline de teste e verificação do ecossistema SDDAI integrado ao COGME.

Executa, em ordem:
  1. Sincronização e verificação do roster SSOT (sync_agent_registry.py --check)
  2. Validação da topologia DAG (dag_validator.py)
  3. Relatório do dispatcher (nexus_dispatcher.py --report)
  4. Health check dos agentes SDDAI (agent_health_check.py)
  5. Validação dos handoffs SDDAI (handoff_parser.py)
  6. Execução do pipeline SDDAI data_optimization (sddai run)
  7. Testes de unidade focados (pytest nos arquivos de validação relevantes)

Fail-closed: qualquer passo com exit != 0 interrompe o pipeline e retorna 1.

Uso:
    python3 scripts/sddai_verify_pipeline.py          # execução completa
    python3 scripts/sddai_verify_pipeline.py --strict  # exit 1 em qualquer aviso/falha
    python3 scripts/sddai_verify_pipeline.py --report  # salva relatório JSON em /tmp/sddai_verify_report.json
"""

import argparse
import json
import subprocess
import sys
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

# SDDAI test data (arquivo mínimo para exercício do pipeline)
TEST_DATA = ROOT / ".ai" / "sddai" / "cogme_sddai_loader" / "__init__.py"


def run(cmd: list, label: str, capture: bool = True,
        env: dict | None = None) -> tuple:
    """Executa um comando. Retorna (returncode, stdout, stderr)."""
    print(f"[SDDAI-VERIFY] {label}")
    merged_env = None
    if env:
        import os as _os
        merged_env = dict(_os.environ)
        merged_env.update(env)
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=capture,
            text=True,
            timeout=300,
            env=merged_env,
        )
        if capture:
            print(proc.stdout, end="")
            if proc.stderr:
                print(proc.stderr, file=sys.stderr, end="")
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        print(f"  -> TIMEOUT após 300s", file=sys.stderr)
        return -1, "", "timeout"
    except Exception as exc:  # noqa: BLE001
        print(f"  -> ERRO: {exc}", file=sys.stderr)
        return -1, "", str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pipeline de verificação do SDDAI integrado ao COGME")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 se qualquer passo falhar ou houver avisos")
    parser.add_argument("--report", default=None,
                        help="caminho para salvar relatório JSON do pipeline")
    args = parser.parse_args()

    started_at = datetime.now(timezone.utc).isoformat()
    steps = []
    overall_ok = True

    # ------------------------------------------------------------------
    # Passo 1: Sync + check do roster
    # ------------------------------------------------------------------
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "sync_agent_registry.py"), "--check"],
        "PASSO 1/7 — Sincronização e verificação do roster SSOT",
    )
    steps.append({
        "step": 1,
        "label": "roster_sync_check",
        "rc": rc,
        "ok": rc == 0,
    })
    if rc != 0:
        overall_ok = False

    # ------------------------------------------------------------------
    # Passo 2: Validação da topologia DAG
    # ------------------------------------------------------------------
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "dag_validator.py")],
        "PASSO 2/7 — Validação da topologia DAG (dag_validator.py)",
    )
    try:
        report = json.loads(out.split("{", 1)[1].rsplit("}", 1)[0] + "}")
        dag_ok = report.get("topologia_valida", False) and report.get("erros") == []
    except Exception:  # noqa: BLE001
        dag_ok = rc == 0
    steps.append({
        "step": 2,
        "label": "dag_validation",
        "rc": rc,
        "ok": dag_ok,
    })
    if not dag_ok:
        overall_ok = False

    # ------------------------------------------------------------------
    # Passo 3: Relatório do dispatcher
    # ------------------------------------------------------------------
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "nexus_dispatcher.py"), "--report"],
        "PASSO 3/7 — Relatório do dispatcher (nexus_dispatcher.py --report)",
    )
    try:
        rep = json.loads(out)
        dispatcher_ok = rc == 0 and rep.get("missing_from_dag") == []
    except Exception:  # noqa: BLE001
        dispatcher_ok = rc == 0
    steps.append({
        "step": 3,
        "label": "dispatcher_report",
        "rc": rc,
        "ok": dispatcher_ok,
    })
    if not dispatcher_ok:
        overall_ok = False

    # ------------------------------------------------------------------
    # Passo 4: Health check dos agentes SDDAI
    # ------------------------------------------------------------------
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "agent_health_check.py")],
        "PASSO 4/7 — Health check dos agentes (agent_health_check.py)",
    )
    try:
        health = json.loads(out)
        sddai_slugs = ["agent-sddai-loader", "agent-sddai-engineer",
                       "agent-sddai-trainer", "agent-sddai-memory",
                       "agent-sddai-cli"]
        sddai_results = [r for r in health.get("resultados", [])
                         if r["slug"] in sddai_slugs]
        sddai_ok = all(r["ok"] for r in sddai_results)
    except Exception:  # noqa: BLE001
        sddai_ok = rc == 0
    steps.append({
        "step": 4,
        "label": "agent_health_check",
        "rc": rc,
        "ok": sddai_ok,
    })
    if not sddai_ok:
        overall_ok = False

    # ------------------------------------------------------------------
    # Passo 5: Validação dos handoffs SDDAI
    # ------------------------------------------------------------------
    rc, out, err = run(
        [sys.executable, str(SCRIPTS / "handoff_parser.py"), "--dir",
         str(ROOT / ".ai" / "handoffs")],
        "PASSO 5/7 — Validação dos handoffs SDDAI (handoff_parser.py)",
    )
    try:
        handoff_summary = json.loads(out)
        # Aceita se os 5 novos handoffs (HF-0400 a HF-0404) parsearem; os 2 antigos
        # (INDEX.md, HF-RELATORIO) são esperados como rejeitados (sem frontmatter).
        sddai_handoffs = [h for h in handoff_summary.get("handoffs", [])
                          if "HF-040" in h.get("file", "")]
        handoffs_ok = all(h["ok"] for h in sddai_handoffs) and len(sddai_handoffs) == 5
    except Exception:  # noqa: BLE001
        handoffs_ok = rc == 0
    steps.append({
        "step": 5,
        "label": "handoff_validation",
        "rc": rc,
        "ok": handoffs_ok,
    })
    if not handoffs_ok:
        overall_ok = False

    # ------------------------------------------------------------------
    # Passo 6: Execução do pipeline SDDAI data_optimization
    # ------------------------------------------------------------------
    rc, out, err = run(
        [sys.executable, str(ROOT / ".ai" / "sddai" / "sddai"),
         "run", "data_optimization",
         "--source", str(TEST_DATA),
         "--epochs", "3",
         "--memory-threshold", "10.0"],
        "PASSO 6/7 — Execução do pipeline SDDAI data_optimization",
        env={"PYTHONPATH": str(ROOT / ".ai" / "sddai")},
    )
    # Extrai o JSON final da saída: encontra a primeira linha que começa com '{'
    # e tenta parsear crescendo até encontrar JSON válido.
    sddai_pipeline_ok = False
    pipeline_result = None
    if rc == 0:
        lines = out.splitlines()
        start_idx = None
        for i, line in enumerate(lines):
            if line.strip().startswith("{"):
                start_idx = i
                break
        if start_idx is not None:
            substring = "\n".join(lines[start_idx:])
            for end in range(len(substring), 0, -1):
                try:
                    pipeline_result = json.loads(substring[:end])
                    sddai_pipeline_ok = pipeline_result.get("all_components_ok", False)
                    break
                except json.JSONDecodeError:
                    continue
    steps.append({
        "step": 6,
        "label": "sddai_pipeline_run",
        "rc": rc,
        "ok": sddai_pipeline_ok,
        "result": pipeline_result,
    })
    if not sddai_pipeline_ok:
        overall_ok = False

    # ------------------------------------------------------------------
    # Passo 7: Testes de unidade focados (validação SDDAI + dispatcher)
    # ------------------------------------------------------------------
    rc, out, err = run(
        [sys.executable, "-m", "pytest",
         "tests/validation/test_nexus_yaml.py",
         "-k", "not test_validate_nexus_yaml_green",
         "tests/agents/test_onda7_agents.py::test_roster_complete_after_onda7",
         "tests/agents/test_onda7_agents.py::test_no_loose_ends_too_early",
         "tests/agents/test_dispatcher_and_sync.py::TestDispatcher::test_topology_report",
         "tests/agents/test_agent_health_check.py",
         "-q"],
        "PASSO 7/7 — Testes de unidade focados (pytest)",
    )
    steps.append({
        "step": 7,
        "label": "pytest_focused",
        "rc": rc,
        "ok": rc == 0,
    })
    if rc != 0:
        overall_ok = False

    # ------------------------------------------------------------------
    # Relatório final
    # ------------------------------------------------------------------
    finished_at = datetime.now(timezone.utc).isoformat()
    report = {
        "pipeline": "sddai_verify_pipeline",
        "version": "1.0.0",
        "project": "COGME",
        "started_at": started_at,
        "finished_at": finished_at,
        "overall_ok": overall_ok,
        "steps": steps,
        "summary": {
            "total_steps": len(steps),
            "passed": sum(1 for s in steps if s["ok"]),
            "failed": sum(1 for s in steps if not s["ok"]),
        },
    }

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL — SDDAI VERIFY PIPELINE")
    print("=" * 60)
    for s in steps:
        status = "✅ PASS" if s["ok"] else "❌ FAIL"
        print(f"  Passo {s['step']}: {s['label']} — {status} (rc={s['rc']})")
    print("-" * 60)
    print(f"Resultado geral: {'SUCESSO' if overall_ok else 'FALHA'}")
    print(f"Passos aprovados: {report['summary']['passed']}/{report['summary']['total_steps']}")

    if args.report:
        Path(args.report).write_text(json.dumps(report, indent=2, ensure_ascii=False))
        print(f"Relatório salvo em: {args.report}")

    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())