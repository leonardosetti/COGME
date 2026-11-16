"""Esquemas de autenticação (spec-004 §5.1; SPEC-017)."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from src.shared.schemas import _Schema


class RegisterRequest(_Schema):
    identifier: str = Field(
        description="Email, CPF (11 dígitos) ou CNPJ (14 dígitos).",
        min_length=1,
        max_length=255,
    )
    password: str = Field(
        description="Senha: 8 a 128 caracteres.",
        min_length=8,
        max_length=128,
    )
    name: str = Field(
        description="Nome completo.",
        min_length=1,
        max_length=255,
    )


class RegisterResponse(_Schema):
    user_id: int
    message: str = "Conta criada. Faça login."


class LoginRequest(_Schema):
    identifier: str = Field(
        description="Email, CPF ou CNPJ normalizado.",
        min_length=1,
        max_length=255,
    )
    password: str


class LoginResponse(_Schema):
    message: str = "Login realizado"


class ResetRequestRequest(_Schema):
    identifier: str = Field(
        description="Email, CPF ou CNPJ.",
        min_length=1,
        max_length=255,
    )


class ResetConfirmRequest(_Schema):
    token: str
    new_password: str = Field(
        description="Nova senha: 8 a 128 caracteres.",
        min_length=8,
        max_length=128,
    )


class AliasResponse(_Schema):
    kind: Literal["email", "cpf", "cnpj"]
    masked: str


class MeResponse(_Schema):
    user_id: int
    name: str
    email: str | None = None
    created_at: datetime
