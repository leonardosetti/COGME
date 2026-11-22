"""Testes de unidade de src/backend/utils/email.py.

Cobrem funções puras e o branch de desenvolvimento (fallback de arquivo /
log, sem SMTP real), sem banco nem rede. Essas funções respondem por boa
parte das 51 statements ainda não cobertas de ``email.py`` (22% de cobertura).
"""

from __future__ import annotations

from email.message import EmailMessage
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from src.backend.utils import email as email_module


# ---------- Fixture de settings fake ----------


def _settings(env: str = "development") -> SimpleNamespace:
    return SimpleNamespace(
        smtp_from="noreply@cogme.local",
        smtp_host="smtp.example.local",
        smtp_port=587,
        smtp_use_tls=True,
        smtp_user="user",
        smtp_password="pass",
        env=env,
    )


# ---------- _build_email ----------


def test_build_email_montamensagem_multipart() -> None:
    with patch("src.backend.utils.email.get_settings", return_value=_settings()):
        msg = email_module._build_email(
            to="cliente@exemplo.com",
            subject="Assunto",
            html_body="<b>html</b>",
            text_body="texto",
        )

    assert isinstance(msg, EmailMessage)
    assert msg["To"] == "cliente@exemplo.com"
    assert msg["Subject"] == "Assunto"
    assert msg["From"] == "noreply@cogme.local"
    assert msg.get_content_type() == "multipart/alternative"
    partes = msg.get_payload()
    textos = [p.get_content() for p in partes if p.get_content_type() == "text/plain"]
    assert any("texto" in t for t in textos)


# ---------- _save_dev_fallback ----------


def test_save_dev_fallback_grava_arquivo_0600(tmp_path: Path) -> None:
    token_file = tmp_path / "reset-token"
    with patch.object(email_module, "_DEV_RESET_TOKEN_FILE", token_file):
        email_module._save_dev_fallback("tok-abc", "cliente@exemplo.com", "reset")

    conteudo = token_file.read_text(encoding="utf-8")
    assert "reset|cliente@exemplo.com|tok-abc|" in conteudo
    modo = token_file.stat().st_mode & 0o777
    assert modo == 0o600, f"permissão esperada 0600, obtida {oct(modo)}"


# ---------- send_reset_token_email (branch desenvolvimento) ----------


def test_send_reset_token_email_dev_salva_fallback(tmp_path: Path) -> None:
    token_file = tmp_path / "reset-token"
    with patch.object(email_module, "_DEV_RESET_TOKEN_FILE", token_file), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("development")
    ):
        email_module.send_reset_token_email(
            "cliente@exemplo.com", "tok-123", "http://localhost/reset?token=tok-123"
        )

    conteudo = token_file.read_text(encoding="utf-8")
    assert "reset|cliente@exemplo.com|tok-123|" in conteudo


def test_send_reset_token_email_producao_chama_smtp() -> None:
    chamadas: list[object] = []

    class _FakeSMTP:
        def __init__(self, host, port, timeout):
            chamadas.append((host, port, timeout))

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def starttls(self, context):
            chamadas.append("starttls")

        def login(self, user, password):
            chamadas.append(("login", user))

        def send_message(self, msg):
            chamadas.append(("send_message", msg["To"], msg["Subject"]))

    with patch.object(email_module.smtplib, "SMTP", _FakeSMTP), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("production")
    ):
        email_module.send_reset_token_email(
            "cliente@exemplo.com", "tok-123", "http://localhost/reset?token=tok-123"
        )

    assert any(c[0] == "send_message" for c in chamadas), chamadas
    assert any(c == "starttls" for c in chamadas), chamadas


# ---------- send_verification_email (branch desenvolvimento) ----------


def test_send_verification_email_dev_salva_fallback(tmp_path: Path) -> None:
    token_file = tmp_path / "reset-token"
    with patch.object(email_module, "_DEV_RESET_TOKEN_FILE", token_file), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("development")
    ):
        email_module.send_verification_email(
            "cliente@exemplo.com", "tok-verify", "http://localhost/verify?token=tok-verify"
        )

    conteudo = token_file.read_text(encoding="utf-8")
    assert "verify|cliente@exemplo.com|tok-verify|" in conteudo


# ---------- send_welcome_email (branch desenvolvimento: log, sem arquivo) ----------


def test_send_welcome_email_dev_log_e_nao_grava_arquivo(tmp_path: Path) -> None:
    token_file = tmp_path / "reset-token"
    with patch.object(email_module, "_DEV_RESET_TOKEN_FILE", token_file), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("development")
    ):
        email_module.send_welcome_email("cliente@exemplo.com", "Cliente")

    # Em desenvolvimento o welcome email não grava arquivo de fallback.
    assert not token_file.exists()


# ---------- _send_smtp (mock de servidor, sem rede real) ----------


def test_send_smtp_usa_tls_e_login() -> None:
    chamadas: list[object] = []

    class _FakeSMTP:
        def __init__(self, host, port, timeout):
            chamadas.append(("init", host, port, timeout))

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def starttls(self, context):
            chamadas.append("starttls")

        def login(self, user, password):
            chamadas.append(("login", user, bool(password)))

        def send_message(self, msg):
            chamadas.append(("send_message", msg["To"]))

    msg = EmailMessage()
    msg["To"] = "a@b.c"
    msg["Subject"] = "s"
    with patch.object(email_module.smtplib, "SMTP", _FakeSMTP), patch(
        "src.backend.utils.email.get_settings",
        return_value=_settings("production"),
    ):
        email_module._send_smtp(msg)

    assert ("init", "smtp.example.local", 587, 10) in chamadas, chamadas
    assert "starttls" in chamadas, chamadas
    assert ("login", "user", True) in chamadas, chamadas
    assert ("send_message", "a@b.c") in chamadas, chamadas


def test_send_verification_email_producao_chama_smtp() -> None:
    chamadas: list[object] = []
    with patch.object(email_module, "_send_smtp", lambda msg: chamadas.append(msg)), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("production")
    ):
        email_module.send_verification_email(
            "cliente@exemplo.com", "tok-verify", "http://localhost/verify?token=tok-verify"
        )
    assert len(chamadas) == 1
    assert chamadas[0]["To"] == "cliente@exemplo.com"
    assert chamadas[0]["Subject"] == "COGME — Verifique seu e-mail"


def test_send_welcome_email_producao_chama_smtp() -> None:
    chamadas: list[object] = []
    with patch.object(email_module, "_send_smtp", lambda msg: chamadas.append(msg)), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("production")
    ):
        email_module.send_welcome_email("cliente@exemplo.com", "Cliente")
    assert len(chamadas) == 1
    assert chamadas[0]["To"] == "cliente@exemplo.com"
    assert chamadas[0]["Subject"] == "COGME — Bem-vindo!"

def test_send_smtp_sem_tls_e_sem_auth() -> None:
    chamadas: list[object] = []

    class _FakeSMTP:
        def __init__(self, host, port, timeout):
            chamadas.append(("init", host, port, timeout))

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def starttls(self, context):
            chamadas.append("starttls")

        def login(self, user, password):
            chamadas.append(("login", user, bool(password)))

        def send_message(self, msg):
            chamadas.append(("send_message", msg["To"]))

    msg = EmailMessage()
    msg["To"] = "a@b.c"
    msg["Subject"] = "s"
    settings = _settings("production")
    settings.smtp_use_tls = False
    settings.smtp_user = None
    settings.smtp_password = None
    with patch.object(email_module.smtplib, "SMTP", _FakeSMTP), patch(
        "src.backend.utils.email.get_settings", return_value=settings
    ):
        email_module._send_smtp(msg)

    assert ("init", "smtp.example.local", 587, 10) in chamadas, chamadas
    assert "starttls" not in chamadas, chamadas
    assert not any(c[0] == "login" for c in chamadas), chamadas
    assert ("send_message", "a@b.c") in chamadas, chamadas


def test_send_verification_email_producao_chama_smtp() -> None:
    chamadas: list[object] = []
    with patch.object(email_module, "_send_smtp", lambda msg: chamadas.append(msg)), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("production")
    ):
        email_module.send_verification_email(
            "cliente@exemplo.com", "tok-verify", "http://localhost/verify?token=tok-verify"
        )
    assert len(chamadas) == 1
    assert chamadas[0]["To"] == "cliente@exemplo.com"
    assert chamadas[0]["Subject"] == "COGME — Verifique seu e-mail"


def test_send_welcome_email_producao_chama_smtp() -> None:
    chamadas: list[object] = []
    with patch.object(email_module, "_send_smtp", lambda msg: chamadas.append(msg)), patch(
        "src.backend.utils.email.get_settings", return_value=_settings("production")
    ):
        email_module.send_welcome_email("cliente@exemplo.com", "Cliente")
    assert len(chamadas) == 1
    assert chamadas[0]["To"] == "cliente@exemplo.com"
    assert chamadas[0]["Subject"] == "COGME — Bem-vindo!"