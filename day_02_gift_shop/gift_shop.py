from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List

# Its probably easiest to just check all the smaller numbers.
# We need to check up until at least the 2-repetition id
# If our n-repetition has some existing smaller repetition inside of it, that is tough.
# We only end up finding 951 total ids for part 2, so if we can efficiently go through them, it,s free.



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
    highest = max(r for l, r in ranges)
    out = 0
    seen = set()
    for id in range(1, highest):
        sid = str(id)
        for amt in range(2, 100):
            sxid = sid * amt
            xid = int(sxid)
            if xid > highest:
                break

            for l, r in ranges:
                if l <= xid <= r:
                    if xid not in seen:
                        seen.add(xid)
                        out += xid

        s2id = sid + sid
        id2 = int(s2id)
        if id2 > highest:
            break
    print("len(seen)", len(seen))
    return out


if __name__ == '__main__':
    get_results("P1 Example", part1, read_line, "example.txt", expected=1227775554)
    get_results("P1", part1, read_line, "input.txt", expected=31000881061)

    get_results("P2 Example", part2, read_line, "example.txt", expected=4174379265)
    get_results("P2", part2, read_line, "input.txt", expected=46769308485)