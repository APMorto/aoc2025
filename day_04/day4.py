from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


# sum of all 8 connected are < 4

def part1(lines):
    grid = lines
    grid = [list(line) for line in lines]
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
    remove = []
    removed = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '@' and sums[r][c] - 1 < 4:
                grid[r][c] = '.'
                removed.add((r, c))
                remove.append((r, c))
                out += 1
    while remove:
        r, c = remove.pop()
        for rr in (r-1, r, r+1):
            for cc in (c-1, c, c+1):
                if 0 <= rr < h and 0 <= cc < w:
                    if grid[rr][cc] == '@':
                        sums[rr][cc] -= 1
                        if (rr, cc) not in removed and sums[rr][cc] - 1 < 4:
                            grid[rr][cc] = '.'
                            out += 1
                            removed.add((rr, cc))
                            remove.append((rr, cc))


    return out


def part2(lines):
    return part1(lines)
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=13)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=43)
    get_results("P2", part2, read_lines, "input.txt")