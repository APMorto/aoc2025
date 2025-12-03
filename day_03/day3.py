from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List

def max_joltage(line):
    n = len(line)
    best = -1
    for i in range(n):
        for j in range(i):
            best = max(best, int(line[j] + line[i]))
    return best


def part1(lines):
    return sum(max_joltage(line) for line in lines)


def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=357)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")