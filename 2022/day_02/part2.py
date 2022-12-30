#!/usr/bin/env python
"""Solves part 2 of the day 2 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, score


def directed_choice(opp, you):
    """Computes the choice you need to make to achieve the desired outcome"""
    result = {'X':-1, 'Y':0, 'Z':1}[you]
    dchoice = {'A':1, 'B':2, 'C':3}
    return 'XYZ'[(dchoice[opp] + result - 1) % 3]
    
    
def directed_score(opp, you):
    """Computes the round score using the directed strategy"""
    return score(opp, directed_choice(opp, you))


def main():
    # Reuse get_args from part 1:
    args = get_args()
    # Read the input file:
    data = args.input.read()
    # Read the "strategy guide":
    sg = [line.split() for line in data.splitlines()]
    # Compute the score using the directed strategy:
    answer = sum([directed_score(*row) for row in sg])
    # Print it:
    print(answer)
    return


if '__main__' == __name__:
    main()
