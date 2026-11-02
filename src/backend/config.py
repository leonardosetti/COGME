"""Configuração do backend COGME lida de variáveis de ambiente.

Todas as variáveis usam o prefixo ``COGME_``. A URL do banco é obrigatória e
não tem valor padrão: sem ela a aplicação não inicia (fail-closed, spec §7).
Nenhum valor de configuração deve ser registrado em log.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Final

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DATABASE_URL_SCHEME: Final[str] = "postgresql+asyncpg://"
LOG_LEVELS: Final[frozenset[str]] = frozenset(
    {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}
)


class Settings(BaseSettings):
    """Configuração imutável do backend, carregada do ambiente.

    Attributes:
        database_url: URL SQLAlchemy async do PostgreSQL
            (``postgresql+asyncpg://...``). Obrigatória e sem padrão.
        rate_ttl_seconds: Idade máxima, em segundos, de uma cotação em cache
            para ser reutilizada sem consultar a rede.
        provider_timeout_seconds: Timeout, em segundos, de cada provedor de
            cotação.
        log_level: Nível de log do módulo ``logging``.
    """

    model_config = SettingsConfigDict(
        env_prefix="COGME_",
        extra="ignore",
        frozen=True,
        # Evita que o valor inválido (ex.: URL com credencial) apareça na
        # mensagem de ValidationError e vaze para logs.
        hide_input_in_errors=True,
    )

    database_url: str = Field(repr=False)
    rate_ttl_seconds: int = Field(default=3600, gt=0)
    provider_timeout_seconds: float = Field(default=0.9, gt=0)
    log_level: str = "INFO"

    @field_validator("database_url")
    @classmethod
    def _validate_database_url(cls, value: str) -> str:
        """Garante que a URL do banco usa o driver PostgreSQL assíncrono.

        Args:
            value: URL informada em ``COGME_DATABASE_URL``.

        Returns:
            A URL sem espaços nas extremidades.

        Raises:
            ValueError: Se a URL não começar com ``postgresql+asyncpg://``.
        """
        cleaned = value.strip()
        if not cleaned.startswith(DATABASE_URL_SCHEME):
            raise ValueError(
                "A URL do banco deve começar com 'postgresql+asyncpg://'."
            )
        return cleaned

    @field_validator("log_level", mode="before")
    @classmethod
    def _normalize_log_level(cls, value: Any) -> Any:
        """Normaliza o nível de log para maiúsculas e valida o conjunto.

        Args:
            value: Valor bruto de ``COGME_LOG_LEVEL``.

        Returns:
            O nível em maiúsculas.

        Raises:
            ValueError: Se o nível não for um dos níveis padrão do logging.
        """
        if not isinstance(value, str):
            raise ValueError("O nível de log deve ser um texto.")
        level = value.strip().upper()
        if level not in LOG_LEVELS:
            raise ValueError(
                "Nível de log inválido; use CRITICAL, ERROR, WARNING, "
                "INFO ou DEBUG."
            )
        return level


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Devolve a configuração do processo, lida do ambiente uma única vez.

    Em testes, use ``get_settings.cache_clear()`` após alterar o ambiente ou
    construa ``Settings(database_url=...)`` diretamente.

    Returns:
        A instância única de ``Settings``.

    Raises:
        pydantic.ValidationError: Se ``COGME_DATABASE_URL`` estiver ausente
            ou qualquer variável for inválida.
    """
    return Settings()
