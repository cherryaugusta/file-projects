from pathlib import Path
from file_projects.personal.finance import parse_budget

summary = parse_budget(Path("data/personal/budget.txt"))

print(f"Income: ${summary.income}")
print(f"Expenses: ${summary.expenses}")
print(f"Remaining: ${summary.remaining}")
