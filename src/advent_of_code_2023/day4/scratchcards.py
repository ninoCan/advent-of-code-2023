import re
from pathlib import Path
from typing import List, Tuple


def parse_row(line: str) -> Tuple[List[int], List[int]]:
    _, content = str.split(":")
    card_string, point_string = content.strip().split("|")
    pattern = re.compile(r"\d+")
    return pattern.findall(card_string), pattern.findall(point_string)


def calculate_row_matches(
    card_numbers: List[int], winning_numbers: List[int]
) -> int:
    pass


def calculate_victory_points(lines):
    number_of_matches = [
        calculate_row_matches(card_numbers, winning_numbers)
        for line in lines
        for card_numbers, winning_numbers in parse_row(line)
    ]
    return sum([calculate_row_points(matches) for matches in number_of_matches])


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = calculate_victory_points(lines)
