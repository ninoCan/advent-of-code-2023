from pathlib import Path
from typing import List


def order_by_rank(lines):
    pass


def main(lines: List[str]) -> int:
    ordered_by_rank = order_by_rank(lines)
    bid_times_rank = [index * bid for index, bid in enumerate(ordered_by_rank)]


def part_two_main(lines: List[str]) -> int:
    pass


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = main(lines)
    print("The first answer is", first_answer)
    second_answer = part_two_main(lines)
    print("The second answer is", second_answer)
