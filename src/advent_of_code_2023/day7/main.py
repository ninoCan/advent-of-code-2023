from pathlib import Path
from typing import List


def order_by_rank(hands_list: List[str]) -> List[str]:
    order = 'AKQJT98765432'
    card_bid_list = [
        (char, bid) for line in hands_list for (char, bid) in [line.split()]
    ]
    return sorted(
        hands_list,
        key=lambda line: [
            [order.index(char) for char in card] for (card, _) in card_bid_list
        ],
    )


def card_type(card):
    different_cards = len(set([char for char in card]))
    match different_cards:
        case 1: return 0 # poker
        case 2:
            if any([card.count(char) == 4 for char in card]):
                return 1 # four of a kind
            else:
                return 2 # full house
        case 3:
            if any([card.count(char) == 3 for char in card]):
                return 3 # tree of a kind
            else:
                return 4 # double pair
        case 4:
            return 5     # pair
        case 5:
            return 6     # all different



def order_by_type(hands_list: List[str]) -> List[str]:
    card_bid_list = [
        (card, bid) for line in hands_list for (card, bid) in line.split()
    ]
    return ["".join(card, bid) for card, bid in  sorted(
        card_bid_list,
        key=lambda line: [
            card_type(card_string) for (card_string, _) in card_bid_list
            ],
        )
    )]


def main(lines: List[str]) -> int:
    ordered_by_type = order_by_type(linea)
    ordered_by_rank = order_by_rank(ordered_by_type)
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
