from aoc_2024 import utils
import aoc_2024.day01 as day01
import aoc_2024.day02 as day02

def main():
    input = utils.get_puzzle_input("input/day01.txt")
    print("###### Day01 #####")
    print(day01.part_1(input))
    print(day01.part_2(input))

    print("###### Day02 #####")
    input = utils.get_puzzle_input("input/day02.txt")
    print(day02.part_1(input))
    print(day02.part_2(input))
   


if __name__ == "__main__":
    main()
