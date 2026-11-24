"""Testes de unidade diretos para src/backend/middleware/session.py."""
from __future__ import annotations

from src.backend.middleware.session import _token_hash


def test_token_hash_returns_sha256_hex() -> None:
    h = _token_hash("meu-token-secreto", "meu-pepper")
    assert len(h) == 64
    int(h, 16)  # deve ser hex válido


def test_token_hash_is_deterministic() -> None:
    h1 = _token_hash("token", "pepper")
    h2 = _token_hash("token", "pepper")
    assert h1 == h2


def test_token_hash_is_different_for_different_inputs() -> None:
    h1 = _token_hash("token-a", "pepper")
    h2 = _token_hash("token-b", "pepper")
    assert h1 != h2


def test_token_hash_is_different_for_different_peppers() -> None:
    h1 = _token_hash("token", "pepper-a")
    h2 = _token_hash("token", "pepper-b")
    assert h1 != h2
