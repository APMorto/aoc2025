from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def part1(line):
    print("lines", line)
    ranges = []
    for s in line.split(","):
        l, r = s.split("-")
        l, r = int(l), int(r)
        ranges.append((l, r))
    highest = max(r for l, r in ranges)
    print(len(ranges))
    print("ranges", ranges)
    out = 0
    for id in range(1, highest):
        sid = str(id)
        s2id = sid + sid
        id2 = int(s2id)
        if id2 > highest:
            break
        for l, r in ranges:
            if l <= id2 <= r:
                out += id2
    return out

def part2(lines):
    print("lines", lines)
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_line, "example.txt", expected=1227775554)
    get_results("P1", part1, read_line, "input.txt")

    get_results("P2 Example", part2, read_line, "example.txt")
    get_results("P2", part2, read_line, "input.txt")