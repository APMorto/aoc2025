from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


# sum of all 8 connected are < 4

def part1(lines):
    grid = lines
    h = len(lines)
    w = len(lines[0])

    sums = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '.': continue
            for rr in (r-1, r, r+1):
                for cc in (c-1, c, c+1):
                    if 0 <= rr < h and 0 <= cc < w:
                        sums[rr][cc] += 1
    out = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] == '@' and sums[r][c] - 1 < 4:
                out += 1
    return out


def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=13)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")