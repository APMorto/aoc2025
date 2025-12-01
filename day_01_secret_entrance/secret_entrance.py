from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def part1(lines):
    # L lower, R higher
    MOD = 100
    # How many rotations until it points to 0?
    cur = 50
    out = 0
    for i, line in enumerate(lines):
        mult = -1 if line[0] == 'L' else 1
        amt = int(line[1:])
        cur = (cur + mult * amt) % MOD
        if cur == 0:
            out += 1
    return out

def part2(lines):
    MOD = 100
    # How many rotations until it points to 0?
    cur = 50
    out = 0
    for i, line in enumerate(lines):
        #print("line", line)
        mult = -1 if line[0] == 'L' else 1
        amt = int(line[1:])
        for _ in range(amt):
            cur = (cur + mult) % MOD
            if cur == 0:
                out += 1
        # new = (cur + mult * amt)
        # if ((mult == 1 and new >= MOD) or (mult == -1 and new <= 0)) and (cur != 0):
        #     #print("incremented")
        #     out += 1
        # out += max(0, amt // MOD - 1)
        #print("cur -> new", cur, new)
        # cur = new % MOD
    return out


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt")
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt")
    get_results("P2", part2, read_lines, "input.txt")