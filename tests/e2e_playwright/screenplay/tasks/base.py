"""Classe base ``Task`` do Screenplay Pattern."""

from __future__ import annotations


class Task:
    """Tarefa executada por um ator.

    Subclasses implementam ``perform_as(actor)``.
    """

    def perform_as(self, actor: object) -> None:
        """Executa a tarefa por este ator.

        Args:
            actor: Ator que executa a tarefa.
        """
        raise NotImplementedError
