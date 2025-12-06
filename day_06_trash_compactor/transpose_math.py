from itertools import product

from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks, read_lines_literal
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
    longest_line = max(map(len, lines))
    lines = [line + " " * (longest_line - len(line)) for line in lines]
    transpose_str = list("".join(row) for row in zip(*lines))
    problems = []
    problem = []
    for row in transpose_str:
        if len(row.strip()) == 0:
            problems.append(problem)
            problem = []
        else:
            problem.append(row)
    if len(problem) > 0:
        problems.append(problem)

    out = 0
    for problem in problems:
        nums = []
        for i, row in enumerate(problem):
            if i == 0:
                s = row[:-1].strip()
            else:
                s = row.strip()
            nums.append(int(s))
        if problem[0][-1] == '+':
            out += sum(nums)
        else:
            prod = 1
            for num in nums:
                prod *= num
            out += prod
    return out



if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=4277556)
    get_results("P1", part1, read_lines, "input.txt", expected=5060053676136)

    get_results("P2 Example", part2, read_lines_literal, "example.txt", expected=3263827)
    get_results("P2", part2, read_lines_literal, "input.txt", expected=9695042567249)