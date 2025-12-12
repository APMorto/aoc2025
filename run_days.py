import os
import sys

from util.timer import get_results
from parser.parser import read_grid, read_list_grid, read_line, read_line_blocks, read_lines, read_lines_literal

import template.template
import day_01_secret_entrance.secret_entrance as    day_01
import day_02_gift_shop.gift_shop as                day_02
import day_03_lobby.joltages as                     day_03
import day_04_printing_department.forklift_grid as  day_04
import day_05_cafeteria.ranges as                   day_05
import day_06_trash_compactor.transpose_math as     day_06
import day_07_laboratories.light_splitting as       day_07
import day_08_playground.ihatedthisbccantread as    day_08
import day_09_movie_theater.shape as                day_09

import day_11_reactor.cable_paths as                day_11
import day_12_christmas_tree_farm.fake_puzzle as    day_12

day_information = {
# # DAY: (p1, p2, input_fn, [input_fn2], "dir")
    #0: (template.template.part1, template.template.part2, read_lines, read_line_blocks, "template"),
    1: (day_01.part1, day_01.part2, read_lines, "day_01_secret_entrance"),
    2: (day_02.part1, day_02.part2, read_line, "day_02_gift_shop"),
    3: (day_03.part1, day_03.part2, read_lines, "day_03_lobby"),
    4: (day_04.part1, day_04.part2, read_lines, read_list_grid, "day_04_printing_department"),
    5: (day_05.part1, day_05.part2, read_line_blocks, "day_05_cafeteria"),
    6: (day_06.part1, day_06.part2, read_lines, read_lines_literal, "day_06_trash_compactor"),
    7: (day_07.part1, day_07.part2, read_lines, "day_07_laboratories"),
    8: (day_08.part1, day_08.part2, read_lines, "day_08_playground"),
    9: (day_09.part1, day_09.part2, read_lines, "day_09_movie_theater"),

    11: (day_11.part1, day_11.part2, read_lines, "day_11_reactor"),
    12: (day_12.part1_heuristic, None, read_line_blocks, "day_12_christmas_tree_farm"),
}


if __name__ == "__main__":
    print(sys.version, sys.argv, '\n')
    p1_results, p2_results = [], []
    p1_times, p2_times = [], []
    p1_parse_times, p2_parse_times = [], []

    days = sorted(day_information.keys())
    for day in days:
        # Get day info
        t = day_information[day]
        if len(t) == 4:
            p1, p2, parse, folder = t
            parse1 = parse2 = parse
        elif len(t) == 5:
            p1, p2, parse1, parse2, folder = t
        else:
            raise Exception("Expected 4 or 5 elements in day, not " + str(len(t)))

        file = os.path.join(folder, "input.txt")
        if p1 is p2:
            (res1, res2), time_b, parse_time_b = get_results(f"Day {day} P1&P1", p1, parse1, file, dense=True)
            # Uniformly distribute for now.
            time1 = time2 = time_b / 2
            parse_time1 = parse_time2 = parse_time_b / 2
        else:
            res1, time1, parse_time1 = get_results(f"Day {day} P1", p1, parse1, file, dense=True)
            res2, time2, parse_time2 = get_results(f"Day {day} P2", p2, parse2, file, dense=True)
        print()

        p1_results.append(res1)
        p2_results.append(res2)

        p1_times.append(time1)
        p2_times.append(time2)

        p1_parse_times.append(parse_time1)
        p2_parse_times.append(parse_time2)

    print()

    # Get total times.
    total_p1_time, total_p2_time, total_p1_parse_time, total_p2_parse_time = map(sum, (p1_times, p2_times, p1_parse_times, p2_parse_times))
    total_time = sum((total_p1_time, total_p2_time, total_p1_parse_time, total_p2_parse_time))
    total_times = list(map(sum, zip(p1_times, p2_times, p1_parse_times, p2_parse_times)))

    # Header.
    print("Total Time (All Days):", total_time, "(s)")
    print(f"Total part 1 (All Days): {total_p1_time:.3f}s | {total_p1_time / total_time: 3.1%}")
    print(f"Total part 2 (All Days): {total_p2_time:.3f}s | {total_p2_time / total_time: 3.1%}")
    print(f"Total parsing (P1&2): {total_p1_parse_time+total_p2_parse_time:.3f}s | {(total_p1_parse_time+total_p2_parse_time) / total_time: 3.1%}")
    print()

    # Print the days.
    for i in range(len(days)):
        day = days[i]
        day_str = str(day) if day >= 10 else f"0{day}"
        print(f"Day {day :2}: {total_times[i] :1.3f}s | {total_times[i] / total_time: 3.1%}")
