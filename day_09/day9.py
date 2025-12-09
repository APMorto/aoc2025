from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def part1(lines):
    points = []
    for line in lines:
        x, y = line.split(',')
        x, y = int(x), int(y)
        points.append((x, y))
    n = len(points)

    best = 0
    for i in range(n):
        for j in range(i):
            x1, y1 = points[i]
            x2, y2 = points[j]
            best = max(best, (abs(x1 - x2)+1) * (abs(y1 - y2)+1))
    return best


def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=50)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")