from pathlib import Path
from typing import List


def hasher(string_to_hash: str) -> int:
    pass


def main(input_lines: list[str]) -> int:
    pass


def part_two_main(input_lines: list[str]) -> int:
    pass


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = main(lines)
    print("The first answer is", first_answer)
    second_answer = part_two_main(lines)
    print("The second answer is", second_answer)


def hasher(string_to_hash):
    pass
