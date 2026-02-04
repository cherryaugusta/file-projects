from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

PERSONAL_DATA = DATA_DIR / "personal"
WORK_DATA = DATA_DIR / "work"
STUDY_DATA = DATA_DIR / "study"
