# Python File Projects – File Handling

## Disclaimer

This repository is intended strictly for educational and portfolio demonstration purposes.
All data files are synthetic examples. Do not use real personal, financial, or sensitive data.

## Overview

This repository demonstrates professional Python file handling using modern engineering standards, including clean architecture, testability, static typing, automation, and CI.

It is organized by project domain:

- `src/file_projects/personal/` – personal tools like diary and finance scripts
- `src/file_projects/work/` – work-related scripts and project management
- `src/file_projects/study/` – study materials, assignments, and notes
- `data/` – synthetic data files for personal, work, and study
- `scripts/` – executable scripts such as budget report generation
- `tests/` – unit tests for core modules and business logic

## Engineering Highlights

- `src/` layout compliant with modern Python packaging standards
- `pathlib`-based, cross-platform file handling
- Pure functions and domain modeling (e.g., `BudgetSummary`)
- Defensive parsing with explicit error semantics (`BudgetParseError`)
- Unit testing with pytest for all modules (`io_utils`, `parsers`, `finance`)
- Pre-commit hooks (`mypy`, `ruff`) and CI enforcement
- Backup file handling demonstrated with `data/study/backups/python_notes_backup.txt`

## Running

Run the budget report script:

```bash
python scripts/run_budget_report.py --budget data/personal/budget.txt
```

Run tests:

```bash
pytest
```

## Engineering Decisions

- Domain objects replace primitive tuples for clarity and maintainability
- Parsing logic fully separated from I/O for testability
- Logging used instead of print statements
- CI validates all commits for quality enforcement
- Backup files demonstrate safe file operations and versioning
```
file-projects/
├── src/
│   └── file_projects/
│       ├── __init__.py
│       ├── config.py
│       ├── io_utils.py
│       ├── parsers.py
│       ├── personal/
│       │   ├── __init__.py
│       │   ├── diary.py
│       │   └── finance.py
│       ├── work/
│       │   ├── __init__.py
│       │   ├── project_a.py
│       │   └── project_b.py
│       └── study/
│           ├── __init__.py
│           ├── notes.py
│           └── assignments.py
├── data/
│   ├── personal/
│   │   ├── budget.txt
│   │   └── daily_log.txt
│   ├── work/
│   │   ├── report.txt
│   │   └── meeting_notes.txt
│   └── study/
│       ├── python_notes.txt
│       ├── assignment1.txt
│       └── backups/
│           └── python_notes_backup.txt
├── scripts/
│   └── run_budget_report.py
├── tests/
│   ├── test_io_utils.py
│   ├── test_parsers.py
│   ├── test_finance.py
│   └── test_diary.py
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
