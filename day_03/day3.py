from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


# Select 12/100.

def max_joltage(line):
    n = len(line)
    best = -1
    for i in range(n):
        for j in range(i):
            best = max(best, int(line[j] + line[i]))
    return best


def part1(lines):
    return sum(max_joltage(line) for line in lines)

def max_joltage_12(line, remaining):
    if remaining == 0:
        return ""
    joltages = [int(c) for c in line]
    n = len(joltages)

    # Start with the leftmost largest possible character.
    biggest = joltages[0]
    for i in range(n - remaining+1):
        biggest = max(biggest, joltages[i])

    for i in range(n):
        if joltages[i] == biggest:
            sub = max_joltage_12(line[i+1:], remaining - 1)
            return str(biggest) + sub


def part2(lines):
    return sum(int(max_joltage_12(line, 12)) for line in lines)


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=357)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=3121910778619)
    get_results("P2", part2, read_lines, "input.txt")