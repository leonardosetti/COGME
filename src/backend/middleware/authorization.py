"""Dependência de autorização por proprietário (spec-004 §6; P-14, ADR-019 ST-03).

Toda rota de recurso usa ``require_owner``: consulta a linha do recurso filtrando
por ``owner_user_id`` (ou ``user_id`` para provider_profile/bank_accounts) e
responde **404** (não 403) quando o recurso não existe ou pertence a outro
usuário, evitando enumeração via IDOR.
"""

from __future__ import annotations

from typing import Callable

from fastapi import Depends, HTTPException, Path, Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

from src.backend.middleware.session import SessionData, get_current_session


def require_owner(
    resource_type: str,
    resource_id_param: str = "id",
) -> Callable:
    """Dependency FastAPI: valida o ``owner_user_id`` do recurso.

    Args:
        resource_type: Chave do ``RESOURCE_MAP`` (simulation, invoice, client,
            provider_profile, provider_bank_account).
        resource_id_param: Nome do parâmetro de caminho que carrega o ID.

    Returns:
        Dependency que devolve a linha do recurso (dict-like) ou levanta 401/404.
    """

    resource_map: dict[str, tuple[str, str]] = {
        "simulation": ("simulations", "owner_user_id"),
        "invoice": ("invoices", "owner_user_id"),
        "client": ("clients", "owner_user_id"),
        "provider_profile": ("provider_profiles", "user_id"),
        "provider_bank_account": ("provider_bank_accounts", "user_id"),
    }

    table, owner_col = resource_map[resource_type]

    async def _check(
        request: Request,
        resource_id: int = Path(..., alias=resource_id_param),
        session_factory: async_sessionmaker[AsyncSession] = Depends(
            lambda r: r.app.state.session_factory
        ),
        pepper: str = Depends(lambda r: r.app.state.login_pepper),
        session: SessionData | None = Depends(
            lambda r, sf, p: get_current_session(r, sf, p)
        ),
    ):
        if session is None:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Não autenticado",
                headers={"WWW-Authenticate": "Cookie"},
            )

        from sqlalchemy import select, text

        async with session_factory() as db:
            query = text(
                f"SELECT * FROM {table} WHERE id = :id AND {owner_col} = :owner"
            )
            row = (
                await db.execute(
                    query, {"id": resource_id, "owner": session.user_id}
                )
            ).mappings().one_or_none()
            if row is None:
                raise HTTPException(
                    status_code=HTTP_404_NOT_FOUND,
                    detail="Recurso não encontrado",
                )
            return dict(row)

    return _check
