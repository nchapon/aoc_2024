import pytest

from aoc_2024 import day02




@pytest.fixture
def puzzle():


    return ["7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"]



def test_part_1(puzzle):

    result:int = day02.part_1(puzzle)
    assert result == 2



def test_part_2(puzzle):

    result:int = day02.part_2(puzzle)
    assert result == 4





        
