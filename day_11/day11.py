from collections import defaultdict
from functools import cache

from util.timer import get_results
from parser.parser import read_lines, read_line, read_grid, read_list_grid, read_line_blocks
from typing import List


def part1(lines):
    g = {}
    for line in lines:
        src, dests = line.split(':')
        dests  = dests.strip().split()
        g[src] = list(dests)

    reversedG = defaultdict(list)
    for src, dests in g.items():
        for dest in dests:
            reversedG[dest].append(src)

    @cache
    def waysTo(dest):
        if dest == 'you':
            return 1
        out = 0
        for src in reversedG[dest]:
            out += waysTo(src)
        return out

    return waysTo('out')


def part2(lines):
    g = {}
    for line in lines:
        src, dests = line.split(':')
        dests  = dests.strip().split()
        g[src] = list(dests)

    reversedG = defaultdict(list)
    for src, dests in g.items():
        for dest in dests:
            reversedG[dest].append(src)

    @cache
    def waysTo(dest):
        if dest == 'svr':
            return 1, 0, 0, 0
        outNeither = 0
        outDac = 0
        outFft = 0
        outBoth = 0
        for src in reversedG[dest]:
            subNeither, subDac, subFft, subBoth = waysTo(src)
            if src == 'dac':
                outDac += subNeither
                outDac += subDac
                outBoth += subFft
                outBoth += subBoth
            elif src == 'fft':
                outFft += subNeither
                outFft += subFft
                outBoth += subBoth
                outBoth += subDac
            else:
                outNeither += subNeither
                outBoth += subBoth
                outDac += subDac
                outFft += subFft

        return outNeither, outDac, outFft, outBoth

    print(waysTo('out'))
    return waysTo('out')[3]



if __name__ == '__main__':
    get_results("P1 Example", part1, read_lines, "example.txt", expected=5)
    get_results("P1", part1, read_lines, "input.txt")

    get_results("P2 Example", part2, read_lines, "example.txt", expected=None)
    get_results("P2", part2, read_lines, "input.txt")