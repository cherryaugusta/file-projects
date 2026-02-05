from pathlib import Path
from typing import Iterable

from file_projects.io_utils import safe_read, safe_append


def read_notes(path: Path) -> str:
    """
    Read study notes.
    """
    return safe_read(path)


def append_notes(path: Path, notes: Iterable[str]) -> None:
    """
    Append additional study notes safely.
    """
    content = "".join(f"{note}\n" for note in notes)
    safe_append(path, content)
