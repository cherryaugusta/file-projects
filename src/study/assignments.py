from pathlib import Path
import shutil

from file_projects.io_utils import safe_read


def read_assignment(path: Path) -> str:
    """
    Read an assignment file.
    """
    return safe_read(path)


def backup_assignment(source: Path, backup_dir: Path) -> Path:
    """
    Create a backup copy of an assignment file.
    """
    backup_dir.mkdir(parents=True, exist_ok=True)
    destination = backup_dir / source.name
    shutil.copy2(source, destination)
    return destination
