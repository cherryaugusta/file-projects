from file_projects.parsers import parse_budget_lines

def test_parse_budget_lines():
    lines = [
        "Salary: $1000",
        "Rent: $400",
        "Groceries: $100"
    ]

    summary = parse_budget_lines(lines)

    assert summary.income == 1000
    assert summary.expenses == 500
    assert summary.remaining == 500
