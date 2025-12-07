from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def start_pos(grid):
    w = len(grid[0])
    h = len(grid)
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start = (r, c)
                return start
    return None

def filter_blank_grid_lines(grid):
    w = len(grid[0])
    blank_line = '.' * w
    return [line for line in grid if line != blank_line]

def part1(grid):
    grid = filter_blank_grid_lines(grid)    # Slightly faster.
    w = len(grid[0])
    h = len(grid)
    start = start_pos(grid)
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


def part2(grid):
    grid = filter_blank_grid_lines(grid)    # Slightly faster.
    w = len(grid[0])
    h = len(grid)
    start = start_pos(grid)
    assert start is not None
    sr, sc = start

    dp = [[0] * w for _ in range(h)]
    dp[sr][sc] = 1

    for r in range(1, h):
        for c in range(w):
            if grid[r][c] == '^':
                dp[r][c-1] += dp[r-1][c]
                dp[r][c+1] += dp[r-1][c]
            else:
                dp[r][c] += dp[r-1][c]
    return sum(dp[-1])


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=21)
    get_results("P1", part1, read_lines, "input.txt", expected=1570, repetitions=1000)

    get_results("P2 Example", part2, read_lines, "example.txt", expected=40)
    get_results("P2", part2, read_lines, "input.txt", expected=15118009521693, repetitions=100)