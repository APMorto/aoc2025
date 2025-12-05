from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List
import math


# I just copy/pasted this from my leetcode solution. So it is my code technically.
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()  # sort by interval start (sort implicitly does this, and then breaks ties by second element)
    nonOverlapping = [[-math.inf, -math.inf]]
    for start, end in intervals:
        if start <= nonOverlapping[-1][1]:
            nonOverlapping[-1][1] = max(nonOverlapping[-1][1], end)
        else:
            nonOverlapping.append([start, end])
    return nonOverlapping[1:]


# Standard BF approach
def part1_old(lines_groups):
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

# Merge ranges, followed by tracking the intervals in order.
def part1(lines_groups):
    ranges = []
    for line in lines_groups[0]:
        l, r = line.split("-")
        l, r = int(l), int(r)
        ranges.append((l, r))
    ranges = merge(ranges)  # Sorted.

    out = 0
    ids = list(map(int, lines_groups[1]))
    ids.sort()
    interval_idx = 0
    for id in ids:
        while interval_idx < len(ranges) and ranges[interval_idx][1] < id:
            interval_idx += 1
        if interval_idx >= len(ranges):
            break
        if id >= ranges[interval_idx][0]:
            out += 1
    return out


def part2(lines_groups):
    ranges = []
    for line in lines_groups[0]:
        l, r = line.split("-")
        l, r = int(l), int(r)
        ranges.append((l, r))
    merged = merge(ranges)
    out = 0
    for l, r in merged:
        out += r - l + 1
    return out


if __name__ == '__main__':
    get_results("P1 Example", part1_old, read_line_blocks, "example.txt", expected=3)
    get_results("P1 old", part1_old, read_line_blocks, "input.txt", expected=681)
    get_results("P1_faster Example", part1, read_line_blocks, "example.txt", expected=3)
    get_results("P1_faster", part1, read_line_blocks, "input.txt", expected=681)

    get_results("P2 Example", part2, read_line_blocks, "example.txt", expected=14)
    get_results("P2", part2, read_line_blocks, "input.txt", expected=348820208020395)