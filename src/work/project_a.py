from pathlib import Path
from dataclasses import dataclass

from file_projects.io_utils import safe_read


@dataclass(frozen=True)
class ProjectReport:
    title: str
    content: str


def load_report(path: Path) -> ProjectReport:
    """
    Load a project report from disk.
    """
    text = safe_read(path)
    lines = text.splitlines()

    title = lines[0] if lines else "Untitled Project"
    content = "\n".join(lines[1:])

    return ProjectReport(title=title, content=content)
