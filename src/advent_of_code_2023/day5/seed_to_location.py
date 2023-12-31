import copy
import collections
import re
from pathlib import Path
from typing import List, OrderedDict


def reroute_point(map_lines: List[str], point: int) -> int:
    for line in map_lines:
        destination, source, length = tuple(parse_digits(line))
        if (point < source + length) and (point > source):
            delta = point - source
            return destination + delta
    else:
        return point


def calculate_minimum_location(
    seed_maps_dict: OrderedDict[str, List[str]]
) -> int:
    dict_copy = copy.deepcopy(seed_maps_dict)
    seeds = parse_digits(str(dict_copy.pop("seeds")))

    points = seeds
    for key in dict_copy.keys():
        points = [reroute_point(dict_copy[key], point) for point in points]

    return min(points)


def parse_digits(line: str) -> List[int]:
    pattern = re.compile(r'\d+')
    return [int(number) for number in pattern.findall(line)]


def parse(file_lines: List[str]) -> OrderedDict[str, List[str]]:
    container = collections.OrderedDict()
    seed_line, *rest = file_lines
    container["seeds"] = seed_line

    rules, key = [], ''
    for line in rest[1:]:
        if "map" in line:
            key = line.split(" ")[0]
            continue
        elif len(line) < 2:
            container[key], rules = rules, []
            continue
        rules.append(line)
    else:
        container[key] = rules

    return container


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    seeds_and_maps = parse(lines)
    first_answer = calculate_minimum_location(seeds_and_maps)
    print("The answer is", first_answer)
    second_answer = None
    print("The final answer is", second_answer)
