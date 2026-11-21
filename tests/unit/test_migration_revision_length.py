"""Teste para validar que todas as revisões Alembic têm <= 32 caracteres.

Este teste garante que o campo `alembic_version.version_num` (VARCHAR(32))
não seja violado por revisões com IDs longos.
"""

from pathlib import Path
import re


def test_migration_revision_length():
    """Todas as revisões em migrations/versions/*.py devem ter <= 32 chars."""
    migrations_dir = Path("migrations/versions")
    pattern = re.compile(r'^revision\s*=\s*["\']([^"\']+)["\']', re.MULTILINE)

    violations = []
    for migration_file in sorted(migrations_dir.glob("*.py")):
        content = migration_file.read_text()
        match = pattern.search(content)
        if match:
            revision = match.group(1)
            if len(revision) > 32:
                violations.append((migration_file.name, revision, len(revision)))

    if violations:
        msg = "\n".join(f"  {f}: '{r}' ({l} chars)" for f, r, l in violations)
        raise AssertionError(f"Revisões Alembic excedem 32 caracteres:\n{msg}")


def test_migration_revision_format():
    """Revisões devem seguir o padrão NN_descrição (ex: 0009_fix_users_nullable)."""
    migrations_dir = Path("migrations/versions")
    pattern = re.compile(r'^revision\s*=\s*["\']([^"\']+)["\']', re.MULTILINE)

    violations = []
    for migration_file in sorted(migrations_dir.glob("*.py")):
        content = migration_file.read_text()
        match = pattern.search(content)
        if match:
            revision = match.group(1)
            # Padrão: 4 dígitos + _ + descrição
            if not re.match(r'^\d{4}_.+', revision):
                violations.append((migration_file.name, revision))

    if violations:
        msg = "\n".join(f"  {f}: '{r}' (esperado: 0000_descricao)" for f, r in violations)
        raise AssertionError(f"Revisões Alembic não seguem padrão NN_descrição:\n{msg}")
