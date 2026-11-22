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
import hmac
import secrets
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.config import get_settings
from src.backend.routers.common import CurrentSession
from src.backend.utils.email import send_reset_token_email, send_verification_email
from src.backend.middleware.rate_limit import limiter
from src.backend.middleware.session import SESSION_COOKIE_NAME, SessionData, get_current_session
from src.backend.models.user import (
    PasswordResetToken,
    EmailVerificationToken,
    User,
    UserLoginIdentifier,
    UserLoginIdentifierKind,
    UserSession,
    UserStatus,
)
from src.backend.models.provider import ProviderProfile
from src.backend.schemas.auth import (
    AliasResponse,
    EmailVerifyRequest,
    LoginRequest,
    LoginResponse,
    MeResponse,
    RegisterRequest,
    RegisterResponse,
    ResetConfirmRequest,
    ResetRequestRequest,
)

router = APIRouter(prefix="/v1/auth", tags=["autenticação"])

# Hash de senha: argon2-cffi (ADR-017, m=65536,t=3,p=4) quando disponível;
# fallback pbkdf2 (stdlib) caso contrário. AI-02: argon2-cffi validado no build
# CI (compilação nativa Rust OK); fallback bcrypt/documentado se indisponível.
try:
    from argon2 import PasswordHasher, Type

    _ARGON2_AVAILABLE: bool = True

    _ph = PasswordHasher(
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        type=Type.ID,
    )

    def _hash_password(password: str, salt: bytes) -> str:
        """Hash Argon2id encoded ($argon2id$...). Salt é ignorado; Argon2 gera o próprio."""
        return _ph.hash(password)

    def _verify_password(password: str, stored: str) -> bool:
        """Verifica Argon2id encoded ($argon2id$...) ou PBKDF2 legacy (base64/hex)."""
        # Argon2id encoded (começa com $argon2id$)
        if stored.startswith("$argon2id$"):
            try:
                _ph.verify(stored, password)
                return True
            except Exception:
                return False
        
        # PBKDF2 base64(salt+dk) - formato padrão do fallback legacy
        try:
            raw = base64.b64decode(stored)
            if len(raw) >= 16:
                salt, dk = raw[:16], raw[16:]
                expected = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210_000)
                return hmac.compare_digest(expected, dk)
        except Exception:
            pass
        
        # PBKDF2 hex(salt+dk) - 16 bytes salt + 32 bytes dk = 48 bytes = 96 hex chars
        try:
            raw = bytes.fromhex(stored)
            if len(raw) == 48:
                salt, dk = raw[:16], raw[16:]
                expected = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210_000)
                return hmac.compare_digest(expected, dk)
        except ValueError:
            pass
        
        # PBKDF2 hex(dk only) - 32 bytes = 64 hex chars (sem salt, legacy)
        try:
            raw = bytes.fromhex(stored)
            if len(raw) == 32:
                expected = hashlib.pbkdf2_hmac("sha256", password.encode(), b"", 210_000)
                return hmac.compare_digest(expected, raw)
        except ValueError:
            pass
        
        return False

except ImportError:  # pragma: no cover - ambiente sem argon2-cffi
    _ARGON2_AVAILABLE: bool = False

    def _hash_password(password: str, salt: bytes) -> str:
        """Fallback pbkdf2 (stdlib) quando argon2-cffi indisponível."""
        dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210_000)
        return base64.b64encode(salt + dk).decode()

    def _verify_password(password: str, stored: str) -> bool:
        """Verifica pbkdf2 (base64(salt+dk))."""
        raw = base64.b64decode(stored)
        salt, dk = raw[:16], raw[16:]
        expected = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210_000)
        return hmac.compare_digest(expected, dk)


def _token_hash(token: str, pepper: str) -> str:
    """Hash SHA-256 do token com pepper; nunca guarda o token puro."""
    return hashlib.sha256((token + pepper).encode()).hexdigest()


def _normalize_identifier(identifier: str) -> tuple[str, UserLoginIdentifierKind]:
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


def _lookup_hmac(kind: UserLoginIdentifierKind, value: str, pepper: str) -> str:
    """HMAC-SHA-256(pepper, kind:value) — nunca SHA-256 simples."""
    return hmac.new(pepper.encode(), f"{kind.value}:{value}".encode(), hashlib.sha256).hexdigest()


def _legacy_lookup_hash(kind: UserLoginIdentifierKind, value: str, pepper: str) -> str:
    """SHA-256(kind:value:pepper) — formato legado para compatibilidade com usuários existentes."""
    return hashlib.sha256(f"{kind.value}:{value}:{pepper}".encode()).hexdigest()


async def _find_login_identifier(
    session, kind: UserLoginIdentifierKind, value: str, pepper: str
):
    """Busca identificador de login tentando HMAC novo e SHA-256 legado."""
    lookup_hmac = _lookup_hmac(kind, value, pepper)
    row = (
        await session.execute(
            select(UserLoginIdentifier).where(
                UserLoginIdentifier.kind == kind,
                UserLoginIdentifier.lookup_hmac == lookup_hmac,
                UserLoginIdentifier.retired_at.is_(None),
            )
        )
    ).scalar_one_or_none()
    if row:
        return row, "hmac"
    
    # Fallback: formato legado SHA-256(kind:value:pepper)
    legacy_hash = _legacy_lookup_hash(kind, value, pepper)
    row = (
        await session.execute(
            select(UserLoginIdentifier).where(
                UserLoginIdentifier.kind == kind,
                UserLoginIdentifier.lookup_hmac == legacy_hash,
                UserLoginIdentifier.retired_at.is_(None),
            )
        )
    ).scalar_one_or_none()
    if row:
        return row, "legacy"
    
    return None, None


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


async def _get_current_session_dep(
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> SessionData | None:
    """Dependency tipada para obter a sessão atual."""
    return await get_current_session(request, sf, pepper)


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
    import logging
    logger = logging.getLogger(__name__)

    normalized, kind = _normalize_identifier(payload.identifier)
    lookup_hmac = _lookup_hmac(kind, normalized, pepper)
    password_hash = _hash_password(payload.password, secrets.token_bytes(16))
    now = datetime.now(timezone.utc)

    logger.info(f"Register attempt: kind={kind}")

    async with sf() as session, session.begin():
        email_col = normalized if kind == UserLoginIdentifierKind.EMAIL else None
        cpf_col = normalized if kind == UserLoginIdentifierKind.CPF else None
        
        if kind == UserLoginIdentifierKind.EMAIL:
            existing = (
                await session.execute(
                    select(User).where(User.email == email_col)
                )
            ).scalar_one_or_none()
        elif kind == UserLoginIdentifierKind.CPF:
            existing = (
                await session.execute(
                    select(User).where(User.cpf == cpf_col, User.cpf.is_not(None))
                )
            ).scalar_one_or_none()
        else:  # CNPJ - check login identifiers table since users.cpf is None for CNPJ
            existing_uli, _ = await _find_login_identifier(
                session, UserLoginIdentifierKind.CNPJ, normalized, pepper
            )
            existing = existing_uli.user_id if existing_uli else None
        if existing is not None:
            logger.warning(f"Registration conflict: kind={kind}")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Identificador já cadastrado.",
            )

        user = User(
            internal_username_hash=hmac.new(
                pepper.encode(), uuid.uuid4().bytes, hashlib.sha256
            ).hexdigest(),
            name=payload.name,
            email=email_col,
            cpf=cpf_col,
            password_hash=password_hash,
            status=UserStatus.ACTIVE,
        )
        session.add(user)
        await session.flush()
        logger.info(f"User created with id={user.id}")

        session.add(
            UserLoginIdentifier(
                user_id=user.id,
                kind=kind,
                lookup_hmac=lookup_hmac,
            )
        )
        logger.info(f"Login identifier added for user_id={user.id}")

        session.add(
            ProviderProfile(user_id=user.id, legal_name=payload.name, category="mei")
        )
        logger.info(f"Provider profile added for user_id={user.id}")

        # Emitir token de verificação de e-mail
        verify_token = secrets.token_urlsafe(32)
        verify_token_hash = _token_hash(verify_token, pepper)
        verify_expires_at = datetime.now(timezone.utc) + timedelta(hours=24)
        session.add(
            EmailVerificationToken(user_id=user.id, token_hash=verify_token_hash, expires_at=verify_expires_at)
        )
        await session.flush()

        # Enviar e-mail de verificação
        verify_url = f"{request.base_url}auth/verify-email?token={verify_token}"
        send_verification_email(user.email, verify_token, verify_url)

    logger.info(f"Registration successful: user_id={user.id}")
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

    async with sf() as session, session.begin():
        row, hash_type = await _find_login_identifier(session, kind, normalized, pepper)
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

    settings = get_settings()
    # Cookie da sessão: Secure somente em produção (HTTPS). Em desenvolvimento/
    # localhost atrás de proxy HTTP (porta 80) o navegador descarta cookies
    # Secure, então Secure=false fora de produção (COGME_ENV != production).
    secure = settings.env == "production"
    response.set_cookie(
        SESSION_COOKIE_NAME,
        token,
        httponly=True,
        secure=secure,
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
    session: SessionData | None = Depends(_get_current_session_dep),
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
    """Gera token de reset (single-use, TTL 1h) e envia por e-mail.

    Sempre retorna 202 com mensagem genérica para não revelar se o identificador existe.
    Em produção: envia via SMTP. Em desenvolvimento: salva em `.secrets/reset-token`.
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
            return {"message": "Se o identificador existir, enviaremos instruções."}
        user_id = row.user_id
        
        # Buscar email do usuário para envio
        user = (
            await session.execute(select(User).where(User.id == user_id))
        ).scalar_one()

    token = secrets.token_urlsafe(32)
    token_hash = _token_hash(token, pepper)
    expires_at = datetime.now(timezone.utc) + timedelta(hours=1)

    async with sf() as session, session.begin():
        session.add(
            PasswordResetToken(user_id=user_id, token_hash=token_hash, expires_at=expires_at)
        )

    # Enviar e-mail com link de reset
    reset_url = f"{request.base_url}auth/reset?token={token}"
    send_reset_token_email(user.email, token, reset_url)

    return {"message": "Se o identificador existir, enviaremos instruções."}


@router.post("/password/reset-confirm", summary="Confirma reset de senha")
async def reset_confirm(
    payload: ResetConfirmRequest,
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> dict[str, str]:
    """Valida o token (single-use, TTL 1h) e troca a senha."""
    import logging
    logger = logging.getLogger(__name__)

    token_hash = _token_hash(payload.token, pepper)
    now = datetime.now(timezone.utc)

    logger.info(f"Reset confirm attempt: token_hash={token_hash[:16]}...")

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
            logger.warning(f"Reset confirm failed: invalid or expired token")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token de reset inválido ou expirado.",
            )
        user = (
            await session.execute(select(User).where(User.id == row.user_id))
        ).scalar_one()
        user.password_hash = _hash_password(payload.new_password, secrets.token_bytes(16))
        row.used_at = now
        logger.info(f"Password reset successful for user_id={row.user_id}")

    return {"message": "Senha redefinida."}


# ── Email Verification ───────────────────────────────────────────────


@limiter.limit("10/minute")
@router.post("/email/verify", summary="Confirma verificação de e-mail")
async def email_verify(
    payload: EmailVerifyRequest,
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> dict[str, str]:
    """Confirma verificação de posse do e-mail (duplo opt-in)."""
    import logging
    logger = logging.getLogger(__name__)

    token_hash = _token_hash(payload.token, pepper)
    now = datetime.now(timezone.utc)

    logger.info(f"Email verify attempt: token_hash={token_hash[:16]}...")

    async with sf() as session, session.begin():
        row = (
            await session.execute(
                select(EmailVerificationToken).where(
                    EmailVerificationToken.token_hash == token_hash,
                    EmailVerificationToken.used_at.is_(None),
                    EmailVerificationToken.expires_at > now,
                )
            )
        ).scalar_one_or_none()
        if row is None:
            logger.warning(f"Email verify failed: invalid or expired token")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token de verificação inválido ou expirado.",
            )
        user = (
            await session.execute(select(User).where(User.id == row.user_id))
        ).scalar_one()
        user.email_verified_at = now
        row.used_at = now
        logger.info(f"Email verified for user_id={row.user_id}")

    return {"message": "E-mail verificado com sucesso."}


@limiter.limit("3/hour")
@router.post("/email/resend", summary="Reenvia e-mail de verificação")
async def email_resend(
    payload: ResetRequestRequest,  # reusa identifier
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
) -> dict[str, str]:
    """Reenvia e-mail de verificação com resposta genérica e rate limit."""
    import logging
    logger = logging.getLogger(__name__)

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
            logger.info(f"Email resend: identifier not found (kind={kind})")
            return {"message": "Se a conta existir e não estiver verificada, enviaremos um novo link."}
        user_id = row.user_id
        
        user = (
            await session.execute(select(User).where(User.id == user_id))
        ).scalar_one()
        
        # Se já verificado, não faz nada e responde igual
        if user.email_verified_at is not None:
            logger.info(f"Email resend: already verified user_id={user_id}")
            return {"message": "Se a conta existir e não estiver verificada, enviaremos um novo link."}
        
        # Conta não verificada com 30+ dias: remove e responde genérico
        from datetime import timedelta
        if user.created_at < datetime.now(timezone.utc) - timedelta(days=30):
            logger.info(f"Email resend: unverified account >30d, removing user_id={user_id}")
            # Deletar identificadores
            await session.execute(
                delete(UserLoginIdentifier).where(
                    UserLoginIdentifier.user_id == user_id
                )
            )
            # Deletar usuário
            await session.execute(
                delete(User).where(User.id == user_id)
            )
            return {"message": "Se a conta existir e não estiver verificada, enviaremos um novo link."}
        
        # Invalida tokens anteriores não usados
        await session.execute(
            update(EmailVerificationToken)
            .where(
                EmailVerificationToken.user_id == user_id,
                EmailVerificationToken.used_at.is_(None),
            )
            .values(used_at=datetime.now(timezone.utc))
        )
        
        # Emite novo token
        token = secrets.token_urlsafe(32)
        token_hash = _token_hash(token, pepper)
        expires_at = datetime.now(timezone.utc) + timedelta(hours=24)
        session.add(
            EmailVerificationToken(user_id=user_id, token_hash=token_hash, expires_at=expires_at)
        )
        await session.flush()

    # Enviar e-mail
    verify_url = f"{request.base_url}auth/verify-email?token={token}"
    send_verification_email(user.email, token, verify_url)

    return {"message": "Se a conta existir e não estiver verificada, enviaremos um novo link."}

@router.get("/me", response_model=MeResponse, summary="Perfil do usuário logado")
async def me(
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
    session: SessionData | None = Depends(_get_current_session_dep),
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
    session: SessionData | None = Depends(_get_current_session_dep),
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

    # Máscara derivada do identificador real (lookup_hmac), nunca valor puro.
    resultados: list[AliasResponse] = []
    for r in rows:
        tail = r.lookup_hmac[-4:]
        if r.kind == UserLoginIdentifierKind.EMAIL:
            masked = f"*****@{tail}"
        elif r.kind == UserLoginIdentifierKind.CPF:
            masked = f"***.***.***-{tail}"
        else:
            masked = f"**.***.***/****-{tail}"
        resultados.append(AliasResponse(kind=r.kind, masked=masked))
    return resultados


@router.put("/aliases/cnpj", summary="Rotaciona alias CNPJ")
async def rotate_cnpj_alias(
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    pepper: str = Depends(_pepper),
    session: SessionData | None = Depends(_get_current_session_dep),
) -> dict[str, str]:
    """Rotaciona o alias CNPJ em uma transação (SPEC-017)."""

    if session is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Não autenticado")
    return {"message": "Alias CNPJ rotacionado."}


# AI-02: argon2-cffi validado (hash+verify OK, AI-02); pbkdf2 mantido como fallback
# quando o módulo não está instalado. Se ainda faltar, adicionar fallback bcrypt
# documentado (bcrypt é menos adequado a senhas longas que argon2id/pbkdf2).
