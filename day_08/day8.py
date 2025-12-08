from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List
from util.datastructures import DisJointSets

def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

def part1(lines):
    points = []
    for line in lines:
        x, y, z = line.split(',')
        x, y, z = int(x), int(y), int(z)
        points.append((x, y, z))
    n = len(points)
    print(n)

    distances = [(dist(points[i], points[j]), i, j) for i in range(n) for j in range(n) if i > j]
    distances.sort()
    distances = distances[:1000]

    dsu = DisJointSets(n)

    connections = 0
    for d, i, j in distances:
        if not dsu.connected(i, j):
        #if True:
            dsu.join(i, j)
            connections += 1
            if connections >= 1000-1:
                break

    componentSizes = [dsu.componentSize(root) for root in dsu.componentRoots()]
    componentSizes.sort(reverse=True)
    print(componentSizes)
    return componentSizes[0] * componentSizes[1] * componentSizes[2]




def part2(lines):
    points = []
    for line in lines:
        x, y, z = line.split(',')
        x, y, z = int(x), int(y), int(z)
        points.append((x, y, z))
    n = len(points)
    print(n)

    distances = [(dist(points[i], points[j]), i, j) for i in range(n) for j in range(n) if i != j]
    distances.sort()

    dsu = DisJointSets(n)

    connections = 0
    for d, i, j in distances:
        if not dsu.connected(i, j):
        #if True:
            dsu.join(i, j)
            connections += 1
            if dsu.componentSize(0) == n:
                print(i, j)
                print(points[i], points[j])
                return points[i][0] * points[j][0]
            #if connections >= n-1:
            #    return points[i][0] * points[j][1]

    componentSizes = [dsu.componentSize(root) for root in dsu.componentRoots()]
    componentSizes.sort(reverse=True)
    print(componentSizes)
    #return componentSizes[0] * componentSizes[1] * componentSizes[2]


if __name__ == '__main__':
    #get_results("P1 Example", part1, read_lines, "example.txt", expected=40)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")