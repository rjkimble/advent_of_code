#!/usr/bin/env python
"""Solves part 1 of the day 18 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import deque


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    orig = [(int(x), i) for i, x in enumerate(data)]
    # Put the data into a deque:
    dq = deque(orig)
    # Rearrange according to the puzzle rules:
    for n2m, j in orig:
        i = dq.index((n2m, j))
        dq.rotate(-i)
        dq.popleft()
        dq.rotate(-n2m)
        dq.appendleft((n2m, j))
    # Compute the answer:
    i0 = list(dq).index(orig[[x for x, y in orig].index(0)])
    answer = sum([x for x, y in [list(dq)[(i0 + 1000) % len(data)], 
        list(dq)[(i0 + 2000) % len(data)], list(dq)[(i0 + 3000) % len(data)]]])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
