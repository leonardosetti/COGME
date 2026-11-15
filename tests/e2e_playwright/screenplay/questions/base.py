"""Classe base ``Question`` do Screenplay Pattern."""

from __future__ import annotations


class Question:
    """Pergunta respondida por um ator sobre o estado do sistema.

    Subclasses implementam ``answered_by(actor)``.
    """

    def answered_by(self, actor: object) -> object:
        """Responde a pergunta por este ator.

        Args:
            actor: Ator que responde a pergunta.

        Returns:
            O resultado da pergunta.
        """
        raise NotImplementedError
