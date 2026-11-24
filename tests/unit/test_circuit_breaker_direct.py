"""Testes de unidade para src/backend/services/circuit_breaker.py."""
from __future__ import annotations

from src.backend.services.circuit_breaker import CircuitBreaker


def test_circuit_breaker_closed_allows() -> None:
    cb = CircuitBreaker(failure_threshold=3, reset_seconds=60.0, clock=lambda: 0.0)
    assert cb.allow() is True


def test_circuit_breaker_opens_after_failures() -> None:
    clock = [0.0]
    cb = CircuitBreaker(failure_threshold=2, reset_seconds=60.0, clock=lambda: clock[0])
    cb.allow()
    cb.record_failure()
    cb.allow()
    cb.record_failure()
    assert cb.allow() is False


def test_circuit_breaker_opens_after_reset_seconds() -> None:
    clock = [0.0]
    cb = CircuitBreaker(failure_threshold=1, reset_seconds=60.0, clock=lambda: clock[0])
    cb.allow()
    cb.record_failure()
    assert cb.allow() is False
    clock[0] = 61.0
    assert cb.allow() is True
    assert cb._probing is True


def test_circuit_breaker_record_success_closes() -> None:
    clock = [0.0]
    cb = CircuitBreaker(failure_threshold=1, reset_seconds=60.0, clock=lambda: clock[0])
    cb.allow()
    cb.record_failure()
    assert cb.allow() is False
    clock[0] = 61.0
    cb.allow()
    cb.record_success()
    assert cb._probing is False
    assert cb._failures == 0
