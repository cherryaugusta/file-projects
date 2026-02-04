from pathlib import Path
import pytest
from file_projects.personal.finance import parse_budget
from file_projects.parsers import BudgetSummary, BudgetParseError

# Temporary test files will be created using pytest's tmp_path fixture

def test_parse_budget_correct(tmp_path: Path):
    # Create a temporary budget file with valid data
    budget_file = tmp_path / "budget.txt"
    budget_file.write_text(
        "Salary: $3000\n"
        "Freelance: $500\n"
        "Rent: $1200\n"
        "Utilities: $200\n"
        "Groceries: $400\n"
        "Entertainment: $150\n"
        "Savings: $550\n"
    )

    summary: BudgetSummary = parse_budget(budget_file)

    assert summary.income == 3500
    assert summary.expenses == 2500
    assert summary.remaining == 1000

def test_parse_budget_empty_file(tmp_path: Path):
    # Create an empty budget file
    empty_file = tmp_path / "empty_budget.txt"
    empty_file.write_text("")

    summary: BudgetSummary = parse_budget(empty_file)

    assert summary.income == 0
    assert summary.expenses == 0
    assert summary.remaining == 0

def test_parse_budget_invalid_amount(tmp_path: Path):
    # Create a file with an invalid amount
    invalid_file = tmp_path / "invalid_budget.txt"
    invalid_file.write_text("Salary: $3000\nRent: $abc\n")

    # Parsing should raise BudgetParseError for invalid number
    with pytest.raises(BudgetParseError):
        parse_budget(invalid_file)

def test_parse_budget_file_not_found(tmp_path: Path):
    # Point to a non-existent file
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        parse_budget(missing_file)
