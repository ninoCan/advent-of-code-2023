import re
from pathlib import Path
from typing import Set


def parse_numbers(line_with_numbers: str) -> Set[int]:
    pattern = re.compile(r"\d+")
    return set(pattern.findall(line_with_numbers))


def calculate_row_matches(
    card_numbers: Set[int],
    winning_numbers: Set[int],
) -> int:
    return len([num for num in card_numbers if num in winning_numbers])


def calculate_row_points(card_matches: int) -> int:
    return 0 if card_matches == 0 else 2 ** (card_matches - 1)


def calculate_victory_points(all_lines):
    number_of_matches = [
        calculate_row_matches(
            parse_numbers(card_string),
            parse_numbers(winning_string),
        )
        for line in all_lines
        for _, content in [line.split(":")]
        for card_string, winning_string in [content.split("|")]
    ]
    return sum([calculate_row_points(matches) for matches in number_of_matches])


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = calculate_victory_points(lines)
    print("The answer is", first_answer)
