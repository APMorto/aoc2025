import math

from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List

# Its probably easiest to just check all the smaller numbers.
# We need to check up until at least the 2-repetition id
# If our n-repetition has some existing smaller repetition inside of it, that is tough.
# We only end up finding 951 total ids for part 2, so if we can efficiently go through them, it,s free.

# our biggest value is 7_272_795_557
# So we need to iterate through at least 1 million values.
#

# What if we used CUDA? :devious_grin: 🏳️‍⚧️

def num_digits(n: int):
    return math.floor(math.log10(n)) + 1

# Using this we see there is no region overlap.
def check_interval_overlap(intervals):
    intervals.sort()
    print(intervals)
    n = len(intervals)
    for i, (l, r) in enumerate(intervals):
        for j in range(i+1, n):
            if intervals[j][0] <= r:
                print(f"Intervals {intervals[i]} and {intervals[j]} overlap.")


def part1(line):
    ranges = []
    for s in line.split(","):
        l, r = s.split("-")
        l, r = int(l), int(r)
        ranges.append((l, r))
    highest = max(r for l, r in ranges)
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

def part2(line):
    ranges = []
    for s in line.split(","):
        l, r = s.split("-")
        l, r = int(l), int(r)
        ranges.append((l, r))
    ranges.sort()   # Non-overlapping.
    #print("ranges", ranges)
    #check_interval_overlap(ranges)
    highest = max(r for l, r in ranges)
    highest_digits = num_digits(highest)

    out = 0
    seen = set()

    # for base_id in range(1, 10 ** (highest_digits // 2)):
    #     base_digits = num_digits(base_id)
    #     # print("base_id", base_id)
    #     # print("base_digits", base_digits)
    #     base_pow = 10 ** base_digits
    #     # print("base_pow", base_pow)
    #     cur = base_id
    #     while cur < highest:
    #         for l, r in ranges:
    #             if l <= cur <= r and cur not in seen:
    #                 seen.add(cur)
    #                 out += cur
    #         cur = cur * base_pow + base_id
    #     if base_id * base_pow + base_id > highest:
    #         break
    # return out

    for repetitions in range(2, highest_digits+1):
        baseLen = 1
        while baseLen * repetitions <= highest_digits:
            basePow = 10 ** baseLen
            for base_id in range(10 ** (baseLen-1), 10 ** baseLen):
                cur = base_id
                for _ in range(repetitions-1):
                    cur = cur * basePow + base_id

                for l, r in ranges:
                    if l <= cur <= r and cur not in seen:
                        seen.add(cur)
                        out += cur

            baseLen += 1

    # for id in range(1, highest):
    #     sid = str(id)
    #     for amt in range(2, 100):
    #         sxid = sid * amt
    #         xid = int(sxid)
    #         if xid > highest:
    #             break
    #
    #         for l, r in ranges:
    #             # ranges are sorted, so if this region is too big, they ALL will be.
    #             # if xid < l:   This makes it slower....
    #             #     break
    #             if l <= xid <= r and xid not in seen:
    #                 seen.add(xid)
    #                 out += xid
    #
    #     if amt == 2:    # Ugly way to do this, just with sloppy loop leftover, but it works.
    #         break

    #print("len(seen)", len(seen))
    return out


if __name__ == '__main__':
    get_results("P1 Example", part1, read_line, "example.txt", expected=1227775554)
    get_results("P1", part1, read_line, "input.txt", expected=31000881061)

    get_results("P2 Example", part2, read_line, "example.txt", expected=4174379265)
    get_results("P2", part2, read_line, "input.txt", expected=46769308485)