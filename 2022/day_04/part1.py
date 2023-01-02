#!/usr/bin/env python
"""Solves part 1 of the day 4 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from csv import reader


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def section_range(s):
    """Reads the input row and returns two tuples representing the section ranges."""
    return tuple(map(int, s.split('-')))


def contains(sr1, sr2):
    """Returns a boolean indicating whether one of the ranges fully contains the other."""
    l1, r1 = sr1
    l2, r2 = sr2
    return ((l1 <= l2 and r1 >= r2) or (l1 >= l2 and r1 <= r2))


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = args.input
    # Populate assignments:
    assignments = list(reader(data))
    # Compute the answer:
    answer = len([x for x in [contains(*(map(section_range, row))) for row in assignments] if x])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
