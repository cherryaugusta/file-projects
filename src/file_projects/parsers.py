from dataclasses import dataclass
from typing import Iterable

class BudgetParseError(ValueError):
    pass

@dataclass(frozen=True)
class BudgetSummary:
    income: int
    expenses: int

    @property
    def remaining(self) -> int:
        return self.income - self.expenses

def _parse_amount(line: str) -> int | None:
    if "$" not in line:
        return None
    try:
        return int(line.split("$", 1)[1])
    except ValueError as exc:
        raise BudgetParseError(f"Invalid amount: {line}") from exc

def parse_budget_lines(lines: Iterable[str]) -> BudgetSummary:
    income_keywords = {"Salary", "Freelance"}
    expense_keywords = {"Rent", "Utilities", "Groceries", "Entertainment", "Savings"}

    income = 0
    expenses = 0

    for line in lines:
        amount = _parse_amount(line)
        if amount is None:
            continue
        if any(k in line for k in income_keywords):
            income += amount
        elif any(k in line for k in expense_keywords):
            expenses += amount

    return BudgetSummary(income=income, expenses=expenses)
