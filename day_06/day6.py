from itertools import product

from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def part1(lines):
    grid = [line.split() for line in lines]
    transpose = list(zip(*grid))
    out = 0
    for row in transpose:
        nums = map(int, row[:-1])
        if row[-1] == '+':
           out += sum(nums)
        else:
            prod = 1
            for num in nums:
                prod *= num
            out += prod

    return out


def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=None)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")