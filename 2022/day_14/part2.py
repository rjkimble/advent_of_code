#!/usr/bin/env python
"""Solves part 2 of the day 14 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, sign, get_rocks


def drop_sand2(sand_start, rocks, filled):
    falling = True
    sandx, sandy = sand_start
    path = []
    while falling:
        if (sandx, sandy + 1) in rocks.union(filled):
            if (sandx - 1, sandy + 1) in rocks.union(filled):
                if (sandx + 1, sandy + 1) in rocks.union(filled):
                    filled.add((sandx, sandy))
                    falling = False
                else:
                    sandx += 1
                    sandy += 1
            else:
                sandx -= 1
                sandy += 1
        else:
            sandy += 1
        if falling:
            path.append((sandx, sandy))
    return path


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Compute the rocks map:
    rocks = set()
    for path in data:
        segment_ends = [tuple(map(int, segment_end.split(','))) for segment_end in path.split(' -> ')]
        for start, finish in zip(segment_ends[:-1], segment_ends[1:]):
            rocks.update([rock for rock in get_rocks(start, finish)])
    # Find the level of the bottom rocks:
    bottom = max([rock[1] for rock in rocks]) + 2
    # Now add an "infinite" floor along the bottom:
    floor = set([(i, bottom) for i in range(1001)])
    # Drop the rocks:
    dropped = 0
    filled = set()
    path = [(500, 0)]
    # Drop sand until the path is blocked:
    while path:
        path.extend(drop_sand2(path[-1], rocks.union(floor), filled))
        if path[-1] in filled:
            path.pop()
    # Print the answer:
    print(len(filled))
    return


if '__main__' == __name__:
    main()
