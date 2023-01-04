#!/usr/bin/env python
"""Solves part 2 of the day 13 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, loads, compare
from functools import cmp_to_key


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().split('\n\n')
    # Read the data into Python objects using loads from the json module:
    data = [list(map(loads, x.splitlines())) for x in data]
    # Turn the data into a list of packets:
    packets = []
    for pair in data:
        packets.extend(pair)
    # Append the divider packets:
    packets.extend([[[2]], [[6]]])
    # Sort, using the compare function:
    packets.sort(key=cmp_to_key(compare))
    # Print the answer:
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
    return


if '__main__' == __name__:
    main()
