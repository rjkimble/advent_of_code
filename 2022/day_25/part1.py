#!/usr/bin/env python
"""Solves part 1 of the day 25 puzzle of the 2022 Advent of Code challenge."""

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


def hot_air_to_dec(s):
    """Converts number from hot air format to decimal."""
    if not s or s =='0':
        return 0
    d = '=-012'.index(s[-1]) - 2
    return d + 5 * hot_air_to_dec(s[:-1])


def dec_to_hot_air(n):
    """Converts number from decimal to hot air format."""
    s0 = '=-012'[(n + 2) % 5]
    m = n - hot_air_to_dec(s0)
    if m:
        return dec_to_hot_air(m // 5) + s0
    return s0


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Compute the rocks map:
    print(dec_to_hot_air(sum([hot_air_to_dec(line) for line in data])))
    return


if '__main__' == __name__:
    main()
