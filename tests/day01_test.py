import pytest

from aoc_2024 import day01




@pytest.fixture
def input_1():


    return ["3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"]




def test_part_1(input_1):

    result:int = day01.part_1(input_1)
    assert result == 11



def test_part_2(input_1):

    result:int = day01.part_2(input_1)
    assert result == 31






