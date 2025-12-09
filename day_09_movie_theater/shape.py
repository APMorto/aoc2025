import math
from collections import defaultdict

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
            best = max(best, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
    return best


def part2(lines):
    points = []
    for line in lines:
        x, y = line.split(',')
        x, y = int(x), int(y)
        points.append((x, y))
    n = len(points)

    # For bounds checking, we may use a compressed problem.
    uniqueX = sorted(set(x for x, y in points))
    uniqueY = sorted(set(y for x, y in points))
    xMap = {x: i for i, x in enumerate(uniqueX)}
    yMap = {y: i for i, y in enumerate(uniqueY)}

    def compressionMap(p):
        r, c = p
        return xMap[r], yMap[c]

    # Under the assumption that the shape is concave, we may simply check the rays going in from the outside.
    fromLeft = defaultdict(lambda: math.inf)
    fromRight = defaultdict(lambda: -math.inf)
    fromTop = defaultdict(lambda: math.inf)
    fromBottom = defaultdict(lambda: -math.inf)

    def updateBounds(r, c):
        fromLeft[r] = min(fromLeft[r], c)
        fromRight[r] = max(fromRight[r], c)
        fromTop[c] = min(fromTop[c], r)
        fromBottom[c] = max(fromBottom[c], r)

    prevR, prevC = points[-1]
    for p in points:
        r, c = compressionMap(p)
        if prevR == r:
            for cc in range(min(c, prevC), max(c, prevC) + 1):
                updateBounds(r, cc)
        else:
            for rr in range(min(r, prevR), max(r, prevR) + 1):
                updateBounds(rr, c)
        prevR, prevC = r, c

    best = 0
    for i in range(n):
        for j in range(i):
            x1, y1 = points[i]
            x2, y2 = points[j]
            r1, c1 = compressionMap(points[i])
            r2, c2 = compressionMap(points[j])
            rmin, rmax = min(r1, r2), max(r1, r2)
            cmin, cmax = min(c1, c2), max(c1, c2)

            valid = True
            # Check that there are no points inside (non-border), as this would invalidate it.
            # xmin, xmax = min(x1, x2), max(x1, x2)
            # ymin, ymax = min(y1, y2), max(y1, y2)
            # for k in range(n):
            #     if k != i and k != j:
            #         x3, y3 = points[k]
            #         if (xmin < x3 < xmax and ymin < y3 < ymax):
            #             valid = False
            #             break
            # if not valid: continue

            # Check that from outside we can't see pas the boundary of the square
            # ; or check that the rectangle lies within the 'convex' shape
            for cc in range(cmin, cmax + 1):
                if fromTop[cc] > rmin:
                    valid = False
                    break
                if fromBottom[cc] < rmax:
                    valid = False
                    break
            for rr in range(rmin, rmax + 1):
                if fromLeft[rr] > cmin:
                    valid = False
                    break
                if fromRight[rr] < cmax:
                    valid = False
                    break

            if valid:
                best = max(best, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
    return best


if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=50)
    get_results("P1", part1, read_lines, "input.txt", expected=4748985168)

    get_results("P2 Example", part2, read_lines, "example.txt", expected=24)
    get_results("P2", part2, read_lines, "input.txt", expected=1550760868)