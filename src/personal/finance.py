from pathlib import Path
import argparse
import logging

from file_projects.parsers import parse_budget_lines
from file_projects.io_utils import safe_read

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_budget(file_path: Path):
    content = safe_read(file_path)
    return parse_budget_lines(content.splitlines())

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=Path, required=True)
    args = parser.parse_args()

    summary = parse_budget(args.budget)
    logger.info("Income: $%s", summary.income)
    logger.info("Expenses: $%s", summary.expenses)
    logger.info("Remaining: $%s", summary.remaining)

if __name__ == "__main__":
    main()
