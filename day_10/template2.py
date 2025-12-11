import math
from collections import deque

from day_10.giveup import answer
from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List
import numpy as np

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

def joltage_2(line):
    tokens = line.split()
    goal_str = tokens[0]
    goal_str = goal_str[1:-1]
    button_strs = tokens[1:-1]
    N = len(goal_str)

    joltage_str = tokens[-1]
    joltages = [int(j_str) for j_str in joltage_str[1:-1].split(',')]
    joltage_goal = tuple(joltages)

    button_increments = []
    for button_str in button_strs:
        indices = [int(num) for num in button_str[1:-1].split(',')]
        button = [0] * N
        for i in indices:
            button[i] = 1
        button_increments.append(button)

    # if len(button_increments) > N:
    #     joltage_goal += tuple([0] * (len(button_increments) - N))
    #     N = len(joltage_goal)
    #     for button in button_increments:
    #         while len(button) < N:
    #             button.append(0)
    # while N > len(button_increments):
    #     button_increments.append([0] * N)
    #
    # # buttons define joltages a
    # a = np.zeros((len(button_increments), N), dtype=int)
    # for i, button in enumerate(button_increments):
    #     a[i, :] = button_increments[i]
    # b = np.zeros((len(joltage_goal), 1), dtype=int)
    # for i, joltage in enumerate(joltage_goal):
    #     b[i, 0] = joltage
    #
    # x = np.linalg.solve(a, b)
    # return np.sum(x)

    initial = tuple([0] * N)
    queue = deque()
    queue.append((initial, 0))
    seen = set()
    seen.add(initial)

    while queue:
        cur, dist = queue.popleft()
        if cur == joltage_goal:
            return dist

        remaining = [goal - c for goal, c in zip(joltage_goal, cur)]


        for button_increment in button_increments:
            cur_list = list(cur)

            valid = True
            for i, inc in enumerate(button_increment):
                cur_list[i] += inc
                if cur_list[i] > joltage_goal[i]:
                    valid = False

            if not valid:
                continue
            new = tuple(cur_list)

            remaining = [goal - c for goal, c in zip(joltage_goal, cur)]
            for i in range(N):
                for j in range(N):
                    if i == j: continue
                    valid_buttons = [button for button in button_increments if button[i] == 1 and button[j] == 0]
                    if len(valid_buttons) == 0:
                        valid = False
                        break
                    # if remaining[i] > remaining[j] and not any(button[i] == 1 and button[j] == 0 for button in button_increments):
                    #     if
                    #     valid = False
                    #     break
                if not valid:
                    break
            if not valid: continue


            if new not in seen:
                seen.add(new)
                queue.append((new, dist+1))
    return -1




def part2(lines):
    out = 0
    for i, line in enumerate(lines):
        out += joltage_2(line)
        if i % 10 == 0:
            print(i)
    return out


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=7)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=33)
    get_results("P2", part2, read_lines, "input.txt")
    #get_results("P2", answer, read_lines, "input.txt")
