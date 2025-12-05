from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def part1(lines_groups):
    print(lines_groups)
    ranges = []
    for line in lines_groups[0]:
        l, r = line.split("-")
        l, r = int(l), int(r)
        ranges.append((l, r))

    out = 0
    for id in lines_groups[1]:
        id = int(id.strip())
        valid = False
        for l, r in ranges:
            if l <= id <= r:
                valid = True
                continue
        if valid: out += 1
    return out


def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_line_blocks, "example.txt", expected=3)
    get_results("P1", part1, read_line_blocks, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt")
    get_results("P2", part2, read_lines, "input.txt")