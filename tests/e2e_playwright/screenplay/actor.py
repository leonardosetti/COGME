"""Ator e palco do Screenplay Pattern.

O ator executa tarefas (``perform``) e responde perguntas (``ask``).
O palco guarda o elenco de atores por nome.
"""

from __future__ import annotations

from typing import Final, TypeVar

T = TypeVar("T")


class Actor:
    """Ator que interage com o sistema por meio de habilidades.

    Attributes:
        name: Nome do ator (ex.: ``usuario``).
    """

    def __init__(self, name: str) -> None:
        """Cria o ator sem habilidades.

        Args:
            name: Nome do ator.
        """
        self.name = name
        self._abilities: dict[type, object] = {}

    def add_ability(self, ability: object) -> None:
        """Registra uma habilidade no ator.

        Args:
            ability: Instância de habilidade (ex.: ``BrowseTheWeb``).
        """
        self._abilities[type(ability)] = ability

    def ability(self, ability_type: type) -> object:
        """Devolve a habilidade registrada para o tipo informado.

        Args:
            ability_type: Tipo da habilidade (ex.: ``BrowseTheWeb``).

        Returns:
            A instância da habilidade.

        Raises:
            KeyError: Se o ator não possuir a habilidade.
        """
        return self._abilities[ability_type]

    def perform(self, task: object) -> None:
        """Executa uma tarefa por este ator.

        Args:
            task: Objeto com método ``perform_as(actor)``.
        """
        task.perform_as(self)

    async def ask(self, question: object) -> object:
        """Responde uma pergunta por este ator.

        Args:
            question: Objeto com método ``answered_by(actor)``.

        Returns:
            O resultado da pergunta.
        """
        return await question.answered_by(self)

    def __repr__(self) -> str:
        return f"Actor(name={self.name!r})"


class Stage:
    """Palco que mantém o elenco de atores em cena."""

    def __init__(self) -> None:
        self._cast: dict[str, Actor] = {}

    def cast(self, actor: Actor) -> None:
        """Adiciona o ator ao elenco.

        Args:
            actor: Ator a ser escalado.
        """
        self._cast[actor.name] = actor

    def the(self, name: str) -> Actor:
        """Devolve o ator pelo nome.

        Args:
            name: Nome do ator escalado.

        Returns:
            O ator correspondente.

        Raises:
            KeyError: Se o nome não estiver no elenco.
        """
        return self._cast[name]


stage: Final[Stage] = Stage()
"""Palco global com o elenco de atores dos testes."""


def actor_named(name: str) -> Actor:
    """Devolve (criando se necessário) um ator escalado pelo nome.

    Args:
        name: Nome do ator.

    Returns:
        O ator correspondente, criado e escalado se ainda não existisse.
    """
    actor = stage._cast.get(name)
    if actor is None:
        actor = Actor(name)
        stage.cast(actor)
    return actor
