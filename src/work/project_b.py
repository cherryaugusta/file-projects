from pathlib import Path
from typing import list

from file_projects.io_utils import safe_read


def extract_action_items(path: Path) -> list[str]:
    """
    Extract bullet-point action items from meeting notes.
    """
    lines = safe_read(path).splitlines()
    action_items: list[str] = []

    in_actions = False
    for line in lines:
        if line.strip().lower().startswith("action items"):
            in_actions = True
            continue
        if in_actions:
            if not line.strip():
                break
            action_items.append(line.strip("- ").strip())

    return action_items
