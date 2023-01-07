#!/usr/bin/env python
"""Solves part 1 of the day 18 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def adjacent_cubes(cube):
    """
    Computes the coordinates of the six cubes adjacent to the cube in question.
    """
    a, b, c = cube
    return [(a + 1, b, c), (a - 1, b, c), (a, b + 1, c), (a, b - 1, c), 
        (a, b, c + 1), (a, b, c - 1)]


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Read the cubes:
    cubes = set([tuple(map(int, line.split(','))) for line in data])
    # Compute the area of the free sides:
    free_sides = 0
    for cube in cubes:
        for adj in adjacent_cubes(cube):
            if adj in cubes:
                continue
            free_sides += 1
    # Print the answer:
    print(free_sides)
    return


if '__main__' == __name__:
    main()
