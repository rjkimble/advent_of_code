#!/usr/bin/env python
"""Solves part 1 of the day 1 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def main():
    args = get_args()
    # Read the input file:
    data = args.input.read()
    # Split into individual calorie lists:
    cal = data.split('\n\n')
    # Compute individual calorie entries as lists of integers:
    cal2 = [list(map(int, row.split())) for row in cal]
    # Sum each list to compute calorie totals:
    cal3 = [sum(row) for row in cal2]
    # Find the maxiumum entry:
    answer = max(cal3)
    # Print it:
    print(answer)
    return


if '__main__' == __name__:
    main()
