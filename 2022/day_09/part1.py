#!/usr/bin/env python
"""Solves both parts of the day 9 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    parser.add_argument('knots_count', metavar='KNOTS_COUNT', type=int,
        help='Number of knots to simulate.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def sign(x):
    """Returns -1 if x is negative, 1 if x is positive, 0 if x is 0."""
    if 0 < x:
        return 1
    elif 0 > x:
        return -1
    return 0


def move_head(d, s, knots, knot_tracks):
    """Moves the head the number of steps in the designated direction."""
    for i in range(s):
        if d == 'U':
            knots[0][1] += 1
        elif d == 'D':
            knots[0][1] -= 1
        elif d == 'R':
            knots[0][0] += 1
        elif d == 'L':
            knots[0][0] -= 1
        knot_tracks[0].add(tuple(knots[0]))
        for k in range(1, len(knots)):
            follow(k, knots, knot_tracks)


def follow(k, knots, knot_tracks):
    """
    Moves the indicated knot (k>0) in accordance with the rules for following
    the knot ahead of it in the chain.
    """
    offset = [knots[k - 1][0] - knots[k][0], knots[k - 1][1] - knots[k][1]]
    absoffset = list(map(abs, offset))
    if 1 >= max(absoffset):
        # No move warranted.
        return
    # Compute the correction to the current position and adjust the position:
    correction = list(map(sign, offset))
    knots[k][0] += correction[0]
    knots[k][1] += correction[1]
    # Record it:
    knot_tracks[k].add(tuple(knots[k]))


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Read the list of moves:
    moves = [(d, int(s)) for d, s in [line.split() for line in data]]
    # Perform the moves:
    knots = [[0, 0] for i in range(args.knots_count)]
    knot_tracks = [set([tuple(knot)]) for knot in knots]
    for d, s in moves:
        move_head(d, s, knots, knot_tracks)
    # Print the answer:
    print(len(knot_tracks[-1]))
    return


if '__main__' == __name__:
    main()
