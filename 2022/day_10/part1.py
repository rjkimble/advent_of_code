#!/usr/bin/env python
"""Solves part 1 of the day 10 puzzle of the 2022 Advent of Code challenge."""

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


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Process the instructions:
    x = [1]
    for line in data:
        if 'noop' == line.strip():
            x.append(x[-1])
        if line.startswith('addx'):
            value = int(line.split()[1])
            x.append(x[-1])
            x.append(x[-1] + value)
    # Compute the answer:
    answer = sum([i * x[i - 1] for i in range(20, len(x), 40)])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
