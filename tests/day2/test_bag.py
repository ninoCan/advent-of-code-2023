import pytest

from advent_of_code_2023.day2.bag import Bag


@pytest.mark.parametrize(
    'test_input, constraint, expected',
    [
        ((1, 2, 3), (12, 13, 14), True),
        ((1, 2, 3), (1, 13, 14), True),
        ((1, 2, 3), (1, 2, 14), True),
        ((1, 2, 3), (1, 2, 3), True),
        ((1, 2, 3), (1, 2), False),
        ((1, 2, 3), (1,), False),
        ((1, 2, 3), (0, 0, 0), False),
    ],
)
def test_satisfy_constraint(test_input, constraint, expected):
    under_test = Bag(*test_input)
    con_bag = Bag(*constraint)
    actual = under_test.satisfy_constraint(con_bag)
    assert actual == expected


@pytest.mark.parametrize(
    'init_string, expected_values',
    [
        ('1 red, 1 green, 2 blue', (1, 1, 3)),
        ('1 red, 2 green', (1, 2)),
        ('1 red, 2 blue', (1, 0, 2)),
        ('1 green, 2 red', (2, 1, 0)),
        ('1 green, 2 blue', (0, 1, 2)),
        ('2 blue, 1 green', (0, 1, 2)),
        ('1 red', (1,)),
        ('23 green', (0, 23)),
        ('4 blue', (0, 0, 4)),
    ],
)
def test_init_from_string(init_string, expected_values):
    actual = Bag.init_from_string(init_string)
    expected = Bag(*expected_values)
    assert actual == expected
