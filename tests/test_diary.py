from pathlib import Path
from datetime import date

from file_projects.personal.diary import read_diary, append_entry


def test_append_and_read_diary(tmp_path: Path):
    diary = tmp_path / "diary.txt"

    append_entry(
        diary,
        date(2026, 2, 3),
        ["Worked on file parsing", "Added unit tests"],
    )

    content = read_diary(diary)

    assert "Date: 2026-02-03" in content
    assert "- Worked on file parsing" in content
    assert "- Added unit tests" in content
