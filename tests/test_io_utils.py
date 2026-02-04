from pathlib import Path
from file_projects.io_utils import safe_read, safe_append

def test_safe_append_and_read(tmp_path: Path):
    file = tmp_path / "test.txt"
    safe_append(file, "hello")
    safe_append(file, " world")

    content = safe_read(file)
    assert content == "hello world"
