from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def part1(grid):
    start = None
    w = len(grid[0])
    h = len(grid)
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start = (r, c)
    assert start is not None
    sr, sc = start

    rowPos = set()
    rowPos.add(sc)
    splits = 0

    def split(cols, r):
        nonlocal splits
        newSet = set()
        for c in cols:
            if grid[r][c] == '^':
                splits += 1
                newSet.add(c-1)
                newSet.add(c+1)
            else:
                newSet.add(c)
        return newSet

    for r in range(h):
        curSet = split(rowPos, r)
        rowPos = curSet
    return splits
    return len(rowPos)





def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=21)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")