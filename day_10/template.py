import math
from collections import deque

from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List

def solve_bfs(line):
    tokens = line.split()
    goal_str = tokens[0]
    goal_str = goal_str[1:-1]
    button_strs = tokens[1:-1]

    N = len(goal_str)
    goal_int = 0
    for i, c in enumerate(goal_str):
        if c == '#':
            goal_int |= 1 << i
    # print("goal:", goal_int)
    button_xors = []
    for button_str in button_strs:
        indices = [int(num) for num in button_str[1:-1].split(',')]
        button_xor = 0
        for i in indices:
            button_xor |= 1 << i
        button_xors.append(button_xor)

    queue = deque()
    queue.append((0, 0))
    seen = set()
    seen.add(0)

    while queue:
        cur, dist = queue.popleft()
        if cur == goal_int:
            return dist
        for xor in button_xors:
            new = cur ^ xor
            if new not in seen:
                queue.append((new, dist+1))
                seen.add(new)

    return -math.inf


def part1(lines):
    out = 0
    for line in lines:
        out += solve_bfs(line)
    return out


def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=7)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")