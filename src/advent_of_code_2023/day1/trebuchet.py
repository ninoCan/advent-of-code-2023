from pathlib import Path
from typing import List
import re


def sum_all_digits_in_file(file_content: List[str]) -> int:
    """ Cycle lines of input file, extract first and last digit to compose the
    number, and sum them all to get the total"""
    return sum([extract_first_and_last_digits(line) for line in file_content])


def extract_first_and_last_digits(line_content: str) -> int:
    digits = re.findall(r'\d', line_content)
    if len(digits) == 0:
        return 0
    first, last = digits[0], digits[-1]
    return int(f"{first}{last}")


if __name__ == "__main__":
    file: Path = Path('input.txt')
    answer: int = sum_all_digits_in_file(file.read_text().split("\n"))
    print(answer)