from pathlib import Path
from typing import List, Tuple


def calculate_row_points(card_numbers: int) -> int:
    pass


def parse_row(line: str) -> Tuple[List[int], List[int]]:
    pass


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
