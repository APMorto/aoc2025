from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


# Select 12/100.

# 0.14s
def max_joltage(line):
    n = len(line)
    best = -1
    for i in range(n):
        for j in range(i):
            best = max(best, int(line[j] + line[i]))
    return best

# 0.0013s, or 100x faster.
def fast_joltage_p1(line):
    joltages = list(map(int, line)) # Try basic list comprehension -- is it faster?
    biggest = max(joltages[:-1])
    firstPos = joltages.index(biggest)
    second = max(joltages[firstPos+1:])
    return biggest * 10 + second

def part1(lines):
    return sum(fast_joltage_p1(line) for line in lines)

def part1_old(lines):
    return sum(max_joltage(line) for line in lines)

def max_joltage_12(line, remaining):
    if remaining == 0:
        return ""
    joltages = [int(c) for c in line]
    n = len(joltages)

    # Start with the leftmost largest possible character.
    biggest = joltages[0]
    for i in range(n - remaining+1):
        biggest = max(biggest, joltages[i])

    for i in range(n):
        if joltages[i] == biggest:
            sub = max_joltage_12(line[i+1:], remaining - 1)
            return str(biggest) + sub

def fast_joltage_p2(line):
    # 0 is not present in the input. (this doesn't help really, but its cool IG)
    # Maintain a list of counts of each digit to efficiently find the biggest value
    n = len(line)
    N = 12
    joltages = list(map(int, line))
    counts = [0] * 10
    for joltage in joltages[:n-N+1]:
        counts[joltage] += 1

    def find_biggest():
        for d in range(9, 0, -1):
            if counts[d] > 0:
                return d

    out = 0
    curIdx = 0
    for digit in range(1, N+1):
        biggest = find_biggest()
        # if digit == N:                    # We don't actually need to find it on the last iteration.
        #     out = out * 10 + biggest      # Benchmarks weren't clear on this being better.
        #     continue
        while True:
            joltage = joltages[curIdx]
            counts[joltage] -= 1
            curIdx += 1
            if joltage == biggest:
                out = out * 10 + biggest
                if digit < N:
                    counts[joltages[n-(N-digit)]] += 1
                break
    return out

def part2(lines):
    return sum(fast_joltage_p2(line) for line in lines)

def part2_old(lines):
    return sum(int(max_joltage_12(line, 12)) for line in lines)


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=357)
    get_results("P1", part1, read_lines, "input.txt", expected=17403)
    get_results("P1 old", part1_old, read_lines, "input.txt", expected=17403)

    get_results("P2 Example", part2, read_lines, "example.txt", expected=3121910778619)
    get_results("P2", part2, read_lines, "input.txt", expected=173416889848394)
    get_results("P2 old", part2_old, read_lines, "input.txt", expected=173416889848394)
