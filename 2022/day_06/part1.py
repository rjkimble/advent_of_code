#!/usr/bin/env python
"""Solves part 1 of the day 6 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(data):
    """Reads the data"""
    return data.read()


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input)
    # Compute the answer:
    answer = [len(set(data[i:i+4])) for i in range(len(data) - 3)].index(4) + 4
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
