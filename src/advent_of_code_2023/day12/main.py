import itertools
import logging
import math
import re
from pathlib import Path
from typing import List, Dict, Tuple

from advent_of_code_2023.day5.seed_to_location import parse_digits


def parse(rows: List[str]) -> Dict[str, List[int]]:
    container = {}
    for row in rows:
        string, integers = row.split()
        container[string] = parse_digits(integers)
    return container


def signature(input_string):
    """Returns the number of question marks, hashtags, and dots in the given string"""
    return {char: input_string.count(char) for char in '?#.'}


def reduce_redundant_dots(springs):
    pattern = re.compile(r'\?|\#|\.+')
    return str(
        "".join([char[0] for char in re.findall(pattern, springs)])
    ).strip('.')


def count_arrangements(springs: str, summary: List[int]) -> int:
    minimal_bits = ['#' * length for length in summary]
    minimal_string = '.'.join(minimal_bits)

    reduced = reduce_redundant_dots(springs)
    springs_signature = signature(reduced)
    minimal_signature = signature(minimal_string)

    # if (
    #     len_delta := sum(springs_signature.values())
    #     - sum(minimal_signature.values())
    # ) == 0:
    #     return 1
    number_of_dots_to_fill = (
        len(springs) - minimal_signature["#"] - springs_signature['.']
    )
    number_of_spots_for_dots = (
        len(springs) - len(summary) - springs_signature["."]
    )
    # delta_hash = abs(springs_signature["#"] - minimal_signature["#"])
    # delta_dots = abs(springs_signature["."] - minimal_signature["."])
    # unconstrained = abs(springs_signature["?"] - delta_dots - delta_hash)
    # unknown = springs_signature["?"]
    return math.comb(number_of_spots_for_dots, number_of_dots_to_fill)


def main(input_lines: List[str]) -> int:
    springs_and_summary = parse(input_lines)
    return sum(
        count_arrangements(springs, summary)
        for springs, summary in springs_and_summary.items()
    )


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
