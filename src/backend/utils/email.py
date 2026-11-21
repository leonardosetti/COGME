"""Utilitários de envio de e-mail transacional (reset senha, verificação, boas-vindas).

SMTP próprio no container; fallback de desenvolvimento para arquivo local.
"""

from __future__ import annotations

import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from typing import Final

from src.backend.config import get_settings

# Caminho do fallback de desenvolvimento (permissão 0600)
_DEV_FALLBACK_DIR: Final[Path] = Path("/tmp/secrets")
_DEV_RESET_TOKEN_FILE: Final[Path] = _DEV_FALLBACK_DIR / "reset-token"


def _ensure_dev_fallback_dir() -> None:
    """Cria o diretório de fallback com permissão 0700."""
    _DEV_FALLBACK_DIR.mkdir(mode=0o700, exist_ok=True)


def _build_email(
    to: str,
    subject: str,
    html_body: str,
    text_body: str,
) -> EmailMessage:
    """Constrói mensagem MIME multipart (text + html)."""
    settings = get_settings()
    msg = EmailMessage()
    msg["From"] = settings.smtp_from
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(text_body, subtype="plain", charset="utf-8")
    msg.add_alternative(html_body, subtype="html", charset="utf-8")
    return msg


def _send_smtp(msg: EmailMessage) -> None:
    """Envia via SMTP com TLS opcional."""
    settings = get_settings()
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=10) as server:
        if settings.smtp_use_tls:
            server.starttls(context=context)
        if settings.smtp_user and settings.smtp_password:
            server.login(settings.smtp_user, settings.smtp_password)
        server.send_message(msg)


def _save_dev_fallback(token: str, email: str, purpose: str) -> None:
    """Salva token no arquivo de fallback de desenvolvimento (perm 0600).

    Formato: purpose|email|token|timestamp
    """
    _ensure_dev_fallback_dir()
    from datetime import datetime, timezone
    line = f"{purpose}|{email}|{token}|{datetime.now(timezone.utc).isoformat()}\n"
    # Escrita atômica via arquivo temporário + rename
    tmp = _DEV_RESET_TOKEN_FILE.with_suffix(".tmp")
    with tmp.open("a", encoding="utf-8") as f:
        f.write(line)
    tmp.chmod(0o600)
    tmp.replace(_DEV_RESET_TOKEN_FILE)


def send_reset_token_email(
    email: str,
    token: str,
    reset_url: str,
) -> None:
    """Envia e-mail com link de reset de senha.

    Em produção: SMTP real.
    Em desenvolvimento: salva em `.secrets/reset-token` (perm 0600).
    """
    settings = get_settings()
    
    text_body = f"""
Olá,

Você solicitou a redefinição de senha para sua conta COGME.

Acesse o link abaixo para definir uma nova senha:
{reset_url}

Este link expira em 1 hora e pode ser usado apenas uma vez.

Se você não solicitou este reset, ignore este e-mail.

---
COGME - Simulador de recebimentos do exterior
"""

    html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Redefinição de senha - COGME</title>
</head>
<body style="font-family: system-ui, sans-serif; line-height: 1.6; max-width: 600px; margin: 0 auto; padding: 20px;">
    <h2 style="color: #1f2937;">Redefinição de senha</h2>
    <p>Olá,</p>
    <p>Você solicitou a redefinição de senha para sua conta COGME.</p>
    <p style="text-align: center; margin: 30px 0;">
        <a href="{reset_url}" style="background-color: #2563eb; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block;">Redefinir senha</a>
    </p>
    <p><small>Este link expira em 1 hora e pode ser usado apenas uma vez.</    <p>Se você não solicitou este reset, ignore este e-mail.</p>
    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 20px 0;">
    <p style="color: #6b7280; font-size: 12px;">COGME — Simulador de recebimentos do exterior</p>
</body>
</html>
"""

    msg = _build_email(
        to=email,
        subject="COGME — Redefinição de senha",
        html_body=html_body,
        text_body=text_body,
    )
    
    if settings.env == "production":
        _send_smtp(msg)
    else:
        # Desenvolvimento: salva token em arquivo local (não envia email)
        _save_dev_fallback(token, email, "reset")
        # Loga apenas que o fallback foi usado (sem PII)
        import logging
        logging.getLogger(__name__).info(
            "Reset token saved to dev fallback (email not sent)"
        )


def send_verification_email(
    email: str,
    token: str,
    verify_url: str,
) -> None:
    """Envia e-mail de verificação de posse do e-mail (duplo opt-in)."""
    settings = get_settings()
    
    text_body = f"""
Olá,

Bem-vindo ao COGME! Verifique seu e-mail para ativar sua conta.

Acesse o link abaixo para confirmar seu e-mail:
{verify_url}

Este link expira em 24 horas e pode ser usado apenas uma vez.

Se você não criou esta conta, ignore este e-mail.

---
COGME - Simulador de recebimentos do exterior
"""

    html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Verificação de e-mail - COGME</title>
</head>
<body style="font-family: system-ui, sans-serif; line-height: 1.6; max-width: 600px; margin: 0 auto; padding: 20px;">
    <h2 style="color: #1f2937;">Verifique seu e-mail</h2>
    <p>Olá,</p>
    <p>Bem-vindo ao COGME! Verifique seu e-mail para ativar sua conta.</p>
    <p style="text-align: center; margin: 30px 0;">
        <a href="{verify_url}" style="background-color: #16a34a; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block;">Verificar e-mail</a>
    </p>
    <p><small>Este link expira em 24 horas e pode ser usado apenas uma vez.</    <p>Se você não criou esta conta, ignore este e-mail.</p>
    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 20px 0;">
    <p style="color: #6b7280; font-size: 12px;">COGME — Simulador de recebimentos do exterior</p>
</body>
</html>
"""

    msg = _build_email(
        to=email,
        subject="COGME — Verifique seu e-mail",
        html_body=html_body,
        text_body=text_body,
    )
    
    if settings.env == "production":
        _send_smtp(msg)
    else:
        _save_dev_fallback(token, email, "verify")
        import logging
        logging.getLogger(__name__).info(
            "Verification token saved to dev fallback (email not sent)"
        )


def send_welcome_email(email: str, name: str) -> None:
    """Envia e-mail de boas-vindas após verificação/criação."""
    settings = get_settings()
    
    text_body = f"""
Olá {name},

Bem-vindo ao COGME! Sua conta está ativa.

Você pode agora acessar o simulador e emitir invoices.

---
COGME - Simulador de recebimentos do exterior
"""

    html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Bem-vindo ao COGME</title>
</head>
<body style="font-family: system-ui, sans-serif; line-height: 1.6; max-width: 600px; margin: 0 auto; padding: 20px;">
    <h2 style="color: #1f2937;">Bem-vindo, {name}!</h2>
    <p>Sua conta está ativa e pronta para uso.</p>
    <p style="text-align: center; margin: 30px 0;">
        <a href="https://localhost:8080/dashboard" style="background-color: #2563eb; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block;">Acessar dashboard</a>
    </p>
    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 20px 0;">
    <p style="color: #6b7280; font-size: 12px;">COGME — Simulador de recebimentos do exterior</p>
</body>
</html>
"""

    msg = _build_email(
        to=email,
        subject="COGME — Bem-vindo!",
        html_body=html_body,
        text_body=text_body,
    )
    
    if settings.env == "production":
        _send_smtp(msg)
    else:
        import logging
        logging.getLogger(__name__).info(
            "Welcome email skipped in dev (email not sent)"
        )