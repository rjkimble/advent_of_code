#!/usr/bin/env python
"""Solves part 2 of the day 3 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, splitsack, common, ascii_lowercase, ascii_uppercase


def badge(group):
    sacks = [set(''.join(sack)) for sack in group]
    return ''.join(sacks[0].intersection(sacks[1]).intersection(sacks[2]))


def main():
    # Compute the priority of each letter using a dictionary:
    priority = dict([(letter, 1 + (ascii_lowercase + ascii_uppercase).index(
        letter)) for letter in ascii_lowercase + ascii_uppercase])
    # Reuse get_args from part 1:
    args = get_args()
    # Read the input file:
    data = args.input.read()
    # Populate rucksacks:
    rucksacks = [splitsack(sack) for sack in data.splitlines()]
    # Partition into groups:
    group_indices = list(range(0, len(rucksacks), 3))
    groups = [rucksacks[i:i+3] for i in group_indices]
    # Compute the score using the groups:
    answer = sum([priority[badge(group)] for group in groups])
    # Print it:
    print(answer)
    return


if '__main__' == __name__:
    main()
