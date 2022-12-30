#!/usr/bin/env python
"""Solves part 1 of the day 2 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def score(opp, you):
    """Computes the score of a single round."""
    choice = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}
    return choice[you] + 3 * (((1 + choice[you] - choice[opp]) % 3))
    
    
def main():
    args = get_args()
    # Read the input file:
    data = args.input.read()
    # Read the "strategy guide":
    sg = [line.split() for line in data.splitlines()]
    # Compute the total score (the sum of the scores of the indiidual rounds):
    answer = sum([score(*row) for row in sg])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
