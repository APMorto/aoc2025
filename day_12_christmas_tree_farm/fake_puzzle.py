from itertools import chain

from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List

def rotate90(shape):
    vflipped = shape[::-1]
    tranposed = list(zip(*vflipped))
    return tranposed

def tupleMap(shape):
    return tuple(tuple(row) for row in shape)

def rotateAndFlipShape(shape):
    vflipped = shape[::-1]
    out = set()
    for start in shape, vflipped:
        cur = tupleMap(start)
        for _ in range(4):
            out.add(cur)
            cur = tupleMap(rotate90(cur))
    return list(out)



def part1(line_blocks):
    shapesStrs, regionStrs = line_blocks[:-1], line_blocks[-1]

    shapes = []
    shapeAreas = []
    for shape_str in shapesStrs:
        label = shape_str[0]
        shape_grid_str = shape_str[1:]
        shape = [[int(c == '#') for c in row] for row in shape_grid_str]
        shapes.append(shape)
        shapeAreas.append(sum(chain(*shape)))
    #print(shapeAreas)

    shapePermutations = []
    for shape in shapes:
        shapePermutations.append(rotateAndFlipShape(shape))
        #print(shapePermutations[-1])

    out = 0
    for region_str in regionStrs:
        shape, amt_str = region_str.split(':')
        w, h = shape.split('x')
        w = int(w)
        h = int(h)
        amts = [int(amt_str) for amt_str in amt_str.strip().split()]

        #print(amts)
        areaRequired = sum(amt * area for amt, area in zip(amts, shapeAreas))
        if areaRequired > w * h:
            #print("skipping due to too much area")
            continue
        else:
            out += 1

        grid = [[False] * w for _ in range(h)]
        def place(r, c, shape):
            for rr in range(r, r+3):
                for cc in range(c, c+3):
                    ro = rr - r
                    co = cc - c
                    if shape[ro][co] and not ((0 <= rr < h and 0 <= cc < w) and not grid[rr][cc]):
                        return False

            # We can place.
            for rr in range(r, r+3):
                for cc in range(c, c+3):
                    ro = rr - r
                    co = cc - c
                    if shape[ro][co]:
                        grid[rr][cc] = shape[ro][co]
            return True

        def unplace(r, c, shape):
            for rr in range(r, r+3):
                for cc in range(c, c+3):
                    ro = rr - r
                    co = cc - c
                    if shape[ro][co]:
                        shape[ro][co] = False



    return out

def part1_heuristic(line_blocks):
    shapesStrs, regionStrs = line_blocks[:-1], line_blocks[-1]
    shapeAreas = []
    for shape_str in shapesStrs:
        shape_grid_str = shape_str[1:]
        shape = [[int(c == '#') for c in row] for row in shape_grid_str]
        shapeAreas.append(sum(chain(*shape)))

    out = 0
    for region_str in regionStrs:
        shape, amt_str = region_str.split(':')
        w, h = shape.split('x')
        w = int(w)
        h = int(h)
        amts = [int(amt_str) for amt_str in amt_str.strip().split()]

        areaRequired = sum(amt * area for amt, area in zip(amts, shapeAreas))
        if areaRequired <= w * h:
            out += 1
    return out


def part2(lines):
    pass


if __name__ == '__main__':
    get_results("P1 Example", part1, read_line_blocks, "example.txt", expected=2)
    get_results("P1", part1, read_line_blocks, "input.txt", expected=567)

    get_results("P1 Heuristic only Example", part1_heuristic, read_line_blocks, "example.txt", expected=2)
    get_results("P1 Heuristic only", part1_heuristic, read_line_blocks, "input.txt", expected=567)

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")