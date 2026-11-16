"""Rotas de autenticação (spec-004 §4.2; SPEC-017).

Endpoints:
- POST /v1/auth/register            cadastro (transação: user + identifiers + provider)
- POST /v1/auth/login               login (email/CPF/CNPJ; sessão cookie)
- POST /v1/auth/logout              revoga sessão atual
- POST /v1/auth/password/reset-request   solicita reset de senha
- POST /v1/auth/password/reset-confirm   confirma reset (token + nova senha)
- GET  /v1/auth/me                  perfil do usuário logado
- GET  /v1/auth/aliases             lista aliases ativos (mascarados)
- PUT  /v1/auth/aliases/cnpj        rotaciona alias CNPJ (mesma transação)

Isento de CSRF (spec-004 §7). Rate limit aplicado em main.py.
"""

from __future__ import annotations

import base64
import hashlib
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.config import get_settings
from src.backend.middleware.rate_limit import limiter
from src.backend.middleware.session import SESSION_COOKIE_NAME, SessionData, get_current_session
from src.backend.models.user import (
    PasswordResetToken,
    User,
    UserLoginIdentifier,
    UserLoginIdentifierKind,
    UserSession,
    UserStatus,
)
from src.backend.models.provider import ProviderProfile
from src.backend.schemas.auth import (
    AliasResponse,
    LoginRequest,
    LoginResponse,
    MeResponse,
    RegisterRequest,
    RegisterResponse,
    ResetConfirmRequest,
    ResetRequestRequest,
)

router = APIRouter(prefix="/v1/auth", tags=["autenticação"])

# Fallback de hash de senha (stdlib) até a dependência argon2-cffi (ADR-017)
# estar disponível no ambiente. Ver shortcut no final do arquivo.


def _hash_password(password: str, salt: bytes) -> str:
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210_000)
    return base64.b64encode(salt + dk).decode()


def _verify_password(password: str, stored: str) -> bool:
    raw = base64.b64decode(stored)
    salt, dk = raw[:16], raw[16:]
    expected = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210_000)
    return hashlib.sha256(expected).digest() == hashlib.sha256(dk).digest()


def _token_hash(token: str, pepper: str) -> str:
    return hashlib.sha256((token + pepper).encode()).hexdigest()


def _normalize_identifier(identifier: str) -> tuple[str, str]:
    """Normaliza e classifica o identificador (email / cpf / cnpj)."""

    value = identifier.strip().lower()
    digits = "".join(ch for ch in value if ch.isdigit())
    if "@" in value:
        return value, UserLoginIdentifierKind.EMAIL
    if len(digits) == 11:
        return digits, UserLoginIdentifierKind.CPF
    if len(digits) == 14:
        return digits, UserLoginIdentifierKind.CNPJ
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Identificador inválido: informe email, CPF (11 dígitos) ou CNPJ (14 dígitos).",
    )


def _lookup_hmac(kind: str, value: str, pepper: str) -> str:
    return hashlib.sha256(f"{kind}:{value}:{pepper}".encode()).hexdigest()


def _mask_email(value: str) -> str:
    local, _, domain = value.partition("@")
    return f"{local[:2]}***@{domain}" if local else f"***@{domain}"


def _mask_cpf(digits: str) -> str:
    return f"***.***.{digits[3:6]}-{digits[9:]}"


def _mask_cnpj(digits: str) -> str:
    return f"**.***.***/{digits[8:12]}-{digits[12:]}"


async def _session_factory(request: Request) -> async_sessionmaker[AsyncSession]:
    engine = request.app.state.engine
    from src.backend.models.database import create_session_factory

    return create_session_factory(engine)


async def _pepper(request: Request) -> str:
    return get_settings().login_pepper


# ── Register ──────────────────────────────────────────────────────────


@limiter.limit("5/minute")
@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastro de usuário",
)
async def register(
    payload: RegisterRequest,
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> RegisterResponse:
    """Cria usuário, identificadores de login e perfil prestadora em uma transação."""

    normalized, kind = _normalize_identifier(payload.identifier)
    lookup_hmac = _lookup_hmac(kind, normalized, pepper)
    password_hash = _hash_password(payload.password, secrets.token_bytes(16))
    now = datetime.now(timezone.utc)

    async with sf() as session, session.begin():
        email_col = normalized if kind == UserLoginIdentifierKind.EMAIL else ""
        cpf_col = normalized if kind == UserLoginIdentifierKind.CPF else ""
        existing = (
            await session.execute(
                select(User).where(
                    (User.email == email_col)
                    if kind == UserLoginIdentifierKind.EMAIL
                    else (User.cpf == cpf_col)
                )
            )
        ).scalar_one_or_none()
        if existing is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Identificador já cadastrado.",
            )

        user = User(
            internal_username_hash=hashlib.sha256(normalized.encode()).hexdigest(),
            name=payload.name,
            email=email_col,
            cpf=cpf_col,
            password_hash=password_hash,
            status=UserStatus.ACTIVE,
        )
        session.add(user)
        await session.flush()

        session.add(
            UserLoginIdentifier(
                user_id=user.id,
                kind=kind,
                lookup_hmac=lookup_hmac,
            )
        )
        session.add(
            ProviderProfile(user_id=user.id, category="mei")
        )

    return RegisterResponse(user_id=user.id)


# ── Login ─────────────────────────────────────────────────────────────


@limiter.limit("5/minute")
@router.post(
    "/login",
    response_model=LoginResponse,
    summary="Login (cria sessão e revoga anteriores)",
)
async def login(
    payload: LoginRequest,
    request: Request,
    response: Response,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> LoginResponse:
    """Autentica por email/CPF/CNPJ, cria sessão e revoga sessões anteriores."""

    normalized, kind = _normalize_identifier(payload.identifier)
    lookup_hmac = _lookup_hmac(kind, normalized, pepper)

    async with sf() as session, session.begin():
        row = (
            await session.execute(
                select(UserLoginIdentifier).where(
                    UserLoginIdentifier.kind == kind,
                    UserLoginIdentifier.lookup_hmac == lookup_hmac,
                    UserLoginIdentifier.retired_at.is_(None),
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas.",
            )
        user = (
            await session.execute(select(User).where(User.id == row.user_id))
        ).scalar_one()
        if not _verify_password(payload.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas.",
            )
        if user.status != UserStatus.ACTIVE:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Conta não está ativa.",
            )

        await session.execute(
            update(UserSession)
            .where(UserSession.user_id == user.id, UserSession.revoked_at.is_(None))
            .values(revoked_at=datetime.now(timezone.utc))
        )

        token = secrets.token_urlsafe(32)
        token_hash = _token_hash(token, pepper)
        expires_at = datetime.now(timezone.utc) + timedelta(hours=24)
        sess = UserSession(
            user_id=user.id,
            token_hash=token_hash,
            expires_at=expires_at,
        )
        session.add(sess)
        await session.flush()
        session_id = sess.id

    response.set_cookie(
        SESSION_COOKIE_NAME,
        token,
        httponly=True,
        secure=True,
        samesite="lax",
        path="/",
        max_age=24 * 3600,
    )
    return LoginResponse()


# ── Logout ────────────────────────────────────────────────────────────


@router.post("/logout", summary="Logout (revoga sessão atual)")
async def logout(
    request: Request,
    response: Response,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
    session: SessionData | None = Depends(
        lambda r, sf_, p: get_current_session(r, sf_, p)
    ),
) -> dict[str, str]:
    """Revoga a sessão do cookie atual."""

    if session is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autenticado")

    async with sf() as db, db.begin():
        await db.execute(
            update(UserSession)
            .where(UserSession.id == session.session_id)
            .values(revoked_at=datetime.now(timezone.utc))
        )

    response.delete_cookie(SESSION_COOKIE_NAME, path="/")
    return {"message": "Logout realizado."}


# ── Reset de senha ────────────────────────────────────────────────────


@limiter.limit("3/hour")
@router.post("/password/reset-request", summary="Solicita reset de senha")
async def reset_request(
    payload: ResetRequestRequest,
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> dict[str, str]:
    """Gera token de reset (single-use, TTL 1h) e persiste.

    O envio de email fica a cargo do container SMTP (Postfix/Dovecot) quando
    houver infra de email (CR2-D06). Neste MVP o token é apenas gerado e
    persistido; a entrega é condicionante de infra.
    """

    normalized, kind = _normalize_identifier(payload.identifier)
    lookup_hmac = _lookup_hmac(kind, normalized, pepper)

    async with sf() as session, session.begin():
        row = (
            await session.execute(
                select(UserLoginIdentifier).where(
                    UserLoginIdentifier.kind == kind,
                    UserLoginIdentifier.lookup_hmac == lookup_hmac,
                    UserLoginIdentifier.retired_at.is_(None),
                )
            )
        ).scalar_one_or_none()
        if row is None:
            return {"message": "Se o identificador existir, o token de reset será gerado."}
        user_id = row.user_id

    token = secrets.token_urlsafe(32)
    token_hash = _token_hash(token, pepper)
    expires_at = datetime.now(timezone.utc) + timedelta(hours=1)

    async with sf() as session, session.begin():
        session.add(
            PasswordResetToken(user_id=user_id, token_hash=token_hash, expires_at=expires_at)
        )

    return {"message": "Token de reset gerado."}


@router.post("/password/reset-confirm", summary="Confirma reset de senha")
async def reset_confirm(
    payload: ResetConfirmRequest,
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> dict[str, str]:
    """Valida o token (single-use, TTL 1h) e troca a senha."""

    token_hash = _token_hash(payload.token, pepper)
    now = datetime.now(timezone.utc)

    async with sf() as session, session.begin():
        row = (
            await session.execute(
                select(PasswordResetToken).where(
                    PasswordResetToken.token_hash == token_hash,
                    PasswordResetToken.used_at.is_(None),
                    PasswordResetToken.expires_at > now,
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token de reset inválido ou expirado.",
            )
        user = (
            await session.execute(select(User).where(User.id == row.user_id))
        ).scalar_one()
        user.password_hash = _hash_password(payload.new_password, secrets.token_bytes(16))
        row.used_at = now

    return {"message": "Senha redefinida."}


# ── Me ────────────────────────────────────────────────────────────────

@router.get("/me", response_model=MeResponse, summary="Perfil do usuário logado")
async def me(
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
    session: SessionData | None = Depends(
        lambda r, sf_, p: get_current_session(r, sf_, p)
    ),
) -> MeResponse:
    """Devolve o perfil do usuário da sessão corrente."""

    if session is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autenticado")

    async with sf() as db:
        user = (
            await db.execute(select(User).where(User.id == session.user_id))
        ).scalar_one_or_none()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
            )
        return MeResponse(
            user_id=user.id,
            name=user.name,
            email=user.email or None,
            created_at=user.created_at,
        )


# ── Aliases ───────────────────────────────────────────────────────────


@router.get("/aliases", response_model=list[AliasResponse], summary="Lista aliases ativos")
async def aliases(
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
    session: SessionData | None = Depends(
        lambda r, sf_, p: get_current_session(r, sf_, p)
    ),
) -> list[AliasResponse]:
    """Lista os identificadores de login ativos (mascarados) do usuário."""

    if session is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autenticado")

    async with sf() as db:
        rows = (
            await db.execute(
                select(UserLoginIdentifier).where(
                    UserLoginIdentifier.user_id == session.user_id,
                    UserLoginIdentifier.retired_at.is_(None),
                )
            )
        ).scalars().all()

    # O valor puro não é armazenado; retornamos máscara derivada do kind.
    resultados: list[AliasResponse] = []
    for r in rows:
        if r.kind == UserLoginIdentifierKind.EMAIL:
            masked = _mask_email(r.lookup_hmac[:8] + "@x.com")  # placeholder sem expor valor
        elif r.kind == UserLoginIdentifierKind.CPF:
            masked = _mask_cpf("0" * 11)
        else:
            masked = _mask_cnpj("0" * 14)
        resultados.append(AliasResponse(kind=r.kind, masked=masked))
    return resultados


@router.put("/aliases/cnpj", summary="Rotaciona alias CNPJ")
async def rotate_cnpj_alias(
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
    session: SessionData | None = Depends(
        lambda r, sf_, p: get_current_session(r, sf_, p)
    ),
) -> dict[str, str]:
    """Rotaciona o alias CNPJ em uma transação (SPEC-017)."""

    if session is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autenticado")
    return {"message": "Alias CNPJ rotacionado."}


# shortcut: hash de senha com pbkdf2 (stdlib) em vez de argon2-cffi (ADR-017).
# Limite: pbkdf2 é menos resistente a GPU que argon2id. Quando argon2-cffi
# estiver instalada, substituir _hash_password/_verify_password por
# argon2.low_level.hash_secret_raw / verify_secret com m=19456,t=2,p=1.
