#!/usr/bin/env python
"""Solves part 1 of the day 13 puzzle of the 2022 Advent of Code challenge."""

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


def compare(left, right):
    if type(left) == type(0) and type(right) == type(0):
        if left < right:
            return -1
        elif left > right:
            return 1

    if type(left) == type(0) and type(right) == type([]):
        return compare([left], right)
    
    if type(left) == type([]) and type(right) == type(0):
        return compare(left, [right])
    
    if type(left) == type([]) and type(right) == type([]):
        if left == right:
            return 0
        for i in range(len(left)):
            if i >= len(right):
                return 1
            res = compare(left[i], right[i])
            if res:
                return res
        if len(left) < len(right):
            return -1


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().split('\n\n')
    # Read the data into Python objects using loads from the json module:
    data = [list(map(loads, x.splitlines())) for x in data]
    # Print the answer:
    print(sum([i + 1 for i, pair in enumerate(data) if compare(*pair) < 1]))
    return


if '__main__' == __name__:
    main()
