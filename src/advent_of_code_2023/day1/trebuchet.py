from pathlib import Path
from typing import List
import re


def sum_all_digits_in_file(file_content: List[str]) -> int:
    """ Cycle lines of input file, extract first and last digit to compose the
    number, and sum them all to get the total"""
    numbers_to_sum = [extract_first_and_last_digits_with_words(line) for line in file_content]
    return sum(numbers_to_sum)


def extract_first_and_last_digits(line_content: str) -> int:
    digits = re.findall(r'\d', line_content)
    if len(digits) == 0:
        return 0
    first, last = digits[0], digits[-1]
    return int(f"{first}{last}")


def extract_first_and_last_digits_with_words(line_content: str) -> int:
    digits_pattern = r"\d"
    word_pattern = r"one|two|three|four|five|six|seven|eight|nine"
    pattern = re.compile(f"{digits_pattern}|{word_pattern}")
    digits_and_words = pattern.findall(line_content)
    if not digits_and_words:
        return 0
    digits = [word_to_digit(el) for el in digits_and_words]
    return int(f"{digits[0]}{digits[-1]}")


def word_to_digit(el: str) -> int:
    if len(el) == 1:
        return int(el)
    word_to_digit_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        }
    return word_to_digit_mapping.get(el)


if __name__ == "__main__":
    file: Path = Path('input.txt')
    answer: int = sum_all_digits_in_file(file.read_text().split("\n"))
    print(answer)