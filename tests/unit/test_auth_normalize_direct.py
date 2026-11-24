"""Testes de unidade para _normalize_identifier de auth.py."""
from __future__ import annotations

from fastapi import HTTPException
from src.backend.routers.auth import _normalize_identifier
from src.backend.models.user import UserLoginIdentifierKind


def test_normalize_email() -> None:
    value, kind = _normalize_identifier("Joao.Silva@Example.COM")
    assert value == "joao.silva@example.com"
    assert kind is UserLoginIdentifierKind.EMAIL


def test_normalize_cpf() -> None:
    value, kind = _normalize_identifier("123.456.789-09")
    assert value == "12345678909"
    assert kind is UserLoginIdentifierKind.CPF


def test_normalize_cnpj() -> None:
    value, kind = _normalize_identifier("12.345.678/0001-95")
    assert value == "12345678000195"
    assert kind is UserLoginIdentifierKind.CNPJ


def test_normalize_invalid() -> None:
    from fastapi import HTTPException
    try:
        _normalize_identifier("invalido")
        assert False
    except HTTPException as exc:
        assert exc.status_code == 400
