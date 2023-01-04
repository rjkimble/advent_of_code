#!/usr/bin/env python
"""Solves part 1 of the day 14 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from json import loads


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def sign(x):
    """Computes the sign of x."""
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0


def get_rocks(start, finish):
    """Returns the list of rock positions given the start and finish."""
    xs, ys = start
    xf, yf = finish
    if xs == xf:
        return [(xs, y) for y in range(ys, yf + sign(yf - ys), sign(yf - ys))]
    else:
        return [(x, ys) for x in range(xs, xf + sign(xf - xs), sign(xf - xs))]


def drop_sand(rocks, filled, bottom):
    falling = True
    sandx, sandy = 500, 0
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
        if 173 < sandy:
            falling = False


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
    bottom = max([rock[1] for rock in rocks])
    # Drop the rocks:
    dropped = 0
    filled = set()
    # Drop sand until more sand has been dropped than filled
    while dropped <= len(filled):
        drop_sand(rocks, filled, bottom)
        dropped += 1
    # Print the answer:
    print(len(filled))
    return


if '__main__' == __name__:
    main()
