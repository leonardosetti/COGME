"""Rota de saúde (spec backend-mvp-v1, §3)."""

from __future__ import annotations

from fastapi import APIRouter

from src.shared.schemas import HealthResponse

router = APIRouter(prefix="/v1", tags=["saúde"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Verifica se a API está no ar",
)
async def get_health() -> HealthResponse:
    """Responde que a API está no ar, sem consultar banco nem rede.

    Returns:
        ``{"status": "ok"}``.
    """
    return HealthResponse(status="ok")
