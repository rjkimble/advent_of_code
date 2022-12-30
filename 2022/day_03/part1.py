#!/usr/bin/env python
"""Solves part 1 of the day 3 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from string import ascii_lowercase, ascii_uppercase


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def splitsack(sack):
    """Returns a tuple containing the two halves of a sack's contents."""
    l = len(sack)
    return (sack[:(l//2)], sack[(l//2):])


def common(compartments):
    """Returns the element common to the two compartments."""
    return ''.join(set(compartments[0]).intersection(compartments[1]))


def main():
    # Compute the priority of each letter using a dictionary:
    priority = dict([(letter, 1 + (ascii_lowercase + ascii_uppercase).index(
        letter)) for letter in ascii_lowercase + ascii_uppercase])
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = args.input.read()
    # Populate rucksacks:
    rucksacks = [splitsack(sack) for sack in data.splitlines()]
    # Compute the answer:
    answer = sum([priority[letter] for letter in [common(sack) for sack in rucksacks]])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
