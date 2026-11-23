"""Testes de unidade das funções puras de src/backend/routers/auth.py.

Cobrem helpers sem dependência de banco: normalização de identificador,
hash/verificação de senha (Argon2id disponível no ambiente), HMAC de lookup,
hash de token e máscaras. Essas funções respondem por boa parte das linhas
ainda não cobertas de ``auth.py`` (23% de cobertura).
"""

from __future__ import annotations

import asyncio
import pytest
from fastapi import HTTPException
from starlette import status

from src.backend.routers.auth import (
    _find_login_identifier,
    _hash_password,
    _legacy_lookup_hash,
    _lookup_hmac,
    _mask_cnpj,
    _mask_cpf,
    _mask_email,
    _normalize_identifier,
    _token_hash,
    _verify_password,
)
from src.backend.models.user import UserLoginIdentifierKind


# ---------- Normalização de identificador ----------


def test_normalize_identifier_email() -> None:
    value, kind = _normalize_identifier("Joao.Silva@Example.COM")
    assert value == "joao.silva@example.com"
    assert kind is UserLoginIdentifierKind.EMAIL


def test_normalize_identifier_cpf() -> None:
    value, kind = _normalize_identifier("123.456.789-09")
    assert value == "12345678909"
    assert kind is UserLoginIdentifierKind.CPF


def test_normalize_identifier_cnpj() -> None:
    value, kind = _normalize_identifier("12.345.678/0001-95")
    assert value == "12345678000195"
    assert kind is UserLoginIdentifierKind.CNPJ


def test_normalize_identifier_invalido_leva_400() -> None:
    with pytest.raises(HTTPException) as exc:
        _normalize_identifier("não é um identificador")
    assert exc.value.status_code == status.HTTP_400_BAD_REQUEST


# ---------- Hash de token ----------


def test_token_hash_é_hex_sha256() -> None:
    h = _token_hash("um-token-qualquer", "pepper-teste")
    assert len(h) == 64
    int(h, 16)  # garante que é hexadecimal válido


# ---------- HMAC / hash legado de lookup ----------


def test_lookup_hmac_retorna_hex() -> None:
    h = _lookup_hmac(UserLoginIdentifierKind.EMAIL, "a@b.c", "pepper")
    assert len(h) == 64
    int(h, 16)


def test_legacy_lookup_hash_retorna_hex() -> None:
    h = _legacy_lookup_hash(UserLoginIdentifierKind.CPF, "12345678909", "pepper")
    assert len(h) == 64
    int(h, 16)


# ---------- Hash / verificação de senha (Argon2id) ----------


def test_hash_password_e_verifica() -> None:
    hashed = _hash_password("senha-secreta-123", b"0123456789abcdef")
    # No CI o argon2-cffi está instalado (requirements.txt) e estas linhas
    # executam o ramo Argon2id (64-117); localmente, sem o pacote, executam
    # o fallback pbkdf2 (119-132). Em ambos o round-trip de verificação vale.
    assert _verify_password("senha-secreta-123", hashed) is True
    assert _verify_password("senha-errada", hashed) is False


# ---------- Máscaras ----------


def test_mask_email() -> None:
    assert _mask_email("joao.silva@example.com") == "jo***@example.com"


def test_mask_cpf() -> None:
    assert _mask_cpf("12345678909") == "***.***.456-09"


def test_mask_cnpj() -> None:
    assert _mask_cnpj("12345678000195") == "**.***.***/0001-95"


# ---------- find_login_identifier (sem linha correspondente no banco) ----------


class _FakeResult:
    def __init__(self, row: object | None) -> None:
        self._row = row

    def scalar_one_or_none(self):
        return self._row


class _FakeSession:
    def __init__(self, row: object | None) -> None:
        self._row = row

    async def execute(self, statement: object) -> _FakeResult:
        return _FakeResult(self._row)


def test_find_login_identifier_sem_linha_retorna_none() -> None:
    session = _FakeSession(None)
    resultado = asyncio.run(
        _find_login_identifier(
            session, UserLoginIdentifierKind.EMAIL, "a@b.c", "pepper"
        )
    )
    assert resultado == (None, None)
