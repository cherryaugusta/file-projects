from pathlib import Path
from datetime import date
from typing import Iterable

from file_projects.io_utils import safe_read, safe_append


def read_diary(path: Path) -> str:
    """
    Read the entire diary file.
    """
    return safe_read(path)


def append_entry(
    path: Path,
    entry_date: date,
    lines: Iterable[str],
) -> None:
    """
    Append a structured diary entry.

    Format:
    Date: YYYY-MM-DD
    - line 1
    - line 2
    """
    header = f"\nDate: {entry_date.isoformat()}\n"
    body = "".join(f"- {line}\n" for line in lines)

    safe_append(path, header + body)
