"""Testes unitários dos componentes SDDAI (cogme-sddai-*).

Cobre: loader, memory, engineer, trainer, cli.
Zero dependências externas — apenas stdlib Python.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SDDAI_DIR = ROOT / ".ai" / "sddai"
PYTHONPATH = str(SDDAI_DIR)


def _run(module: str, args: list, timeout: int = 60) -> subprocess.CompletedProcess:
    """Executa um módulo SDDAI via python -m com PYTHONPATH injetado."""
    env = dict(__import__("os").environ)
    env["PYTHONPATH"] = PYTHONPATH
    return subprocess.run(
        [sys.executable, "-m", module] + args,
        capture_output=True,
        text=True,
        timeout=timeout,
        env=env,
    )


def _extract_json_from_proc(proc: subprocess.CompletedProcess, output_file: Path | None = None) -> dict:
    """Extrai JSON de stdout ou de arquivo de saída quando --output é usado."""
    if output_file is not None and output_file.exists():
        return json.loads(output_file.read_text(encoding="utf-8"))
    return _extract_json(proc.stdout)


def _extract_json(stdout: str) -> dict:
    """Extrai objeto JSON de stdout que pode conter linhas de progresso antes."""
    lines = stdout.splitlines()
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("{"):
            start_idx = i
            break
    if start_idx is None:
        raise ValueError(f"Nenhum JSON encontrado no stdout: {stdout[:200]}")
    substring = "\n".join(lines[start_idx:])
    for end in range(len(substring), 0, -1):
        try:
            return json.loads(substring[:end])
        except json.JSONDecodeError:
            continue
    raise ValueError(f"Não foi possível extrair JSON do stdout: {stdout[:200]}")


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

def test_loader_ingest_valid_file(tmp_path):
    """Loader deve ingerir arquivo existente e retornar metadados completos."""
    src = tmp_path / "dados.txt"
    src.write_text("Linha 1 de teste.\nLinha 2 para ingestão.\n", encoding="utf-8")

    out_file = tmp_path / "out.json"
    proc = _run("cogme_sddai_loader.cli", ["--source", str(src), "--output", str(out_file)])
    assert proc.returncode == 0, proc.stderr

    result = _extract_json_from_proc(proc, out_file)
    assert result["ok"] is True
    assert result["package"] == "cogme-sddai-loader"
    r = result["result"]
    assert r["path"] == str(src.resolve())
    assert r["size_bytes"] > 0
    assert r["lines"] == 2
    assert len(r["checksum_sha256"]) == 64
    assert "Linha 1" in r["content"]


def test_loader_missing_file_returns_error(tmp_path):
    """Loader deve retornar código 1 para arquivo inexistente."""
    proc = _run("cogme_sddai_loader.cli", ["--source", str(tmp_path / "nao_existe.txt")])
    assert proc.returncode == 1
    result = json.loads(proc.stderr)
    assert result["ok"] is False


# ---------------------------------------------------------------------------
# Memory
# ---------------------------------------------------------------------------

def test_memory_optimize_within_threshold(tmp_path):
    """Memory optimizer deve reportar status dentro do threshold."""
    out_file = tmp_path / "out.json"
    proc = _run("cogme_sddai_memory.cli", ["--threshold", "10.0", "--output", str(out_file)])
    assert proc.returncode == 0, proc.stderr

    result = _extract_json_from_proc(proc, out_file)
    assert result["ok"] is True
    assert result["package"] == "cogme-sddai-memory"
    r = result["result"]
    assert "memory_threshold_gb" in r
    assert "total_memory_gb" in r
    assert "used_memory_gb" in r
    assert "within_threshold" in r
    assert "status" in r
    assert r["status"] in ("optimized", "warning")


# ---------------------------------------------------------------------------
# Engineer
# ---------------------------------------------------------------------------

def test_engineer_transform_valid_input(tmp_path):
    """Engineer deve transformar saída do loader em features estruturadas."""
    loader_out = {
        "ok": True,
        "package": "cogme-sddai-loader",
        "result": {
            "path": "/tmp/fake.txt",
            "size_bytes": 42,
            "lines": 2,
            "checksum_sha256": "a" * 64,
            "content": "palavra um\ndois palavras tres\n",
        },
    }
    inp = tmp_path / "loader.json"
    inp.write_text(json.dumps(loader_out), encoding="utf-8")

    out_file = tmp_path / "out.json"
    proc = _run("cogme_sddai_engineer.cli", ["--input", str(inp), "--output", str(out_file)])
    assert proc.returncode == 0, proc.stderr

    result = _extract_json_from_proc(proc, out_file)
    assert result["ok"] is True
    assert result["package"] == "cogme-sddai-engineer"
    r = result["result"]
    assert r["word_count"] > 0
    assert r["char_count"] > 0
    assert r["unique_words"] > 0
    assert len(r["feature_checksum"]) == 64
    assert "lexical_diversity" in r["features"]
    assert "avg_words_per_line" in r["features"]


# ---------------------------------------------------------------------------
# Trainer
# ---------------------------------------------------------------------------

def test_trainer_deterministic_output(tmp_path):
    """Trainer deve produzir saída determinística para mesma entrada."""
    eng_out = {
        "ok": True,
        "package": "cogme-sddai-engineer",
        "result": {
            "source": "/tmp/fake.txt",
            "word_count": 10,
            "char_count": 50,
            "unique_words": 8,
            "lines_non_empty": 2,
            "feature_checksum": "b" * 64,
            "features": {"lexical_diversity": 0.8, "avg_words_per_line": 5.0},
        },
    }
    inp = tmp_path / "engineer.json"
    inp.write_text(json.dumps(eng_out), encoding="utf-8")

    out1 = tmp_path / "out1.json"
    out2 = tmp_path / "out2.json"
    proc1 = _run("cogme_sddai_trainer.cli", ["--input", str(inp), "--epochs", "1", "--output", str(out1)])
    proc2 = _run("cogme_sddai_trainer.cli", ["--input", str(inp), "--epochs", "1", "--output", str(out2)])
    assert proc1.returncode == 0, proc1.stderr
    assert proc2.returncode == 0, proc2.stderr

    r1 = _extract_json_from_proc(proc1, out1)["result"]
    r2 = _extract_json_from_proc(proc2, out2)["result"]
    assert r1["model_id"] == r2["model_id"]
    assert r1["final_loss"] == r2["final_loss"]
    assert r1["accuracy"] == r2["accuracy"]


# ---------------------------------------------------------------------------
# CLI pipeline
# ---------------------------------------------------------------------------

def test_cli_pipeline_full_run(tmp_path):
    """CLI deve executar pipeline completo loader -> memory -> engineer -> trainer."""
    src = tmp_path / "dados.txt"
    src.write_text("dados de teste para pipeline SDDAI completo\nsegunda linha para validar ingestão\n", encoding="utf-8")

    proc = _run("cogme_sddai_cli.main", ["--source", str(src), "--epochs", "2", "--memory-threshold", "10.0"])
    assert proc.returncode == 0, proc.stderr

    result = _extract_json(proc.stdout)
    assert result["status"] == "completed"
    assert result["all_components_ok"] is True
    assert result["failed_stage"] is None
    assert result["summary"]["loader_ok"] is True
    assert result["summary"]["memory_ok"] is True
    assert result["summary"]["engineer_ok"] is True
    assert result["summary"]["trainer_ok"] is True