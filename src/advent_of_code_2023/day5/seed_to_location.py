import copy
import re
from pathlib import Path
from typing import List, Dict, Tuple


def create_translation_table(
    dest_src_len_list: List[List[int]],
) -> List[Tuple[int, int]]:
    sort_by_src = sorted(dest_src_len_list, key=lambda x: x[1])
    cols_to_swap = []
    for dest, src, length in sort_by_src:
        if src != 0:
            cols_to_swap.extend(*range(src))
        cols_to_swap.extend(*range(dest, dest + length))
    return list(zip(range(len(cols_to_swap)), cols_to_swap))


def get_next_key(previous: str, remaining_keys: List[str]) -> str:
    lookup_bit = previous.split("-")[-1]
    pattern = re.compile(r"^" + lookup_bit)
    matching_elements = list(filter(pattern.match, remaining_keys))
    return matching_elements[0] if len(matching_elements) != 0 else None


def chain_translations(translations, seeds) -> List[int]:
    new_seeds = copy.deepcopy(seeds)
    conversions = copy.deepcopy(translations)
    key = "seeds"

    while len(keys := conversions.keys()) != 0:
        key = get_next_key(key, keys)
        table = conversions.pop(key)
        new_seeds = [table[seed - 1] for seed in new_seeds]

    return new_seeds


def calculate_minimum_location(
    seed_maps_dict: Dict[str, List[List[int]]]
) -> int:
    dict_copy = copy.deepcopy(seed_maps_dict)
    seed_list = dict_copy.pop("seeds")
    translation_tables = {
        key: create_translation_table(value)
        for key, value in seed_maps_dict.items()
    }
    destination_list = chain_translations(translation_tables, seed_list)

    return min(destination_list)


def parse_digits(line: str) -> List[int]:
    pattern = re.compile(r'\d+')
    return pattern.findall(line)


def parse(file_lines: List[str]) -> Dict[str, List[List[int]]]:
    container = {}
    seed_line, *rest = file_lines
    container["seeds"] = parse_digits(seed_line.split(":")[1])

    rules, key = [], ''
    for line in rest[1:]:
        if "map" in line:
            key = line.split(" ")[0]
            continue
        elif len(line) < 2:
            container[key], rules = rules, []
            continue
        rules.append(parse_digits(line))
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
