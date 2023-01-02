#!/usr/bin/env python
"""Solves part 2 of the day 4 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, reader, section_range


def overlaps(sr1, sr2):
    """Returns a boolean indicating whether or not the two ranges overlap."""
    l1, r1 = sr1
    l2, r2 = sr2
    return not (r1 < l2 or r2 < l1)


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = args.input
    # Populate assignments:
    assignments = list(reader(data))
    # Compute the answer:
    answer = len([x for x in [overlaps(*(map(section_range, row))) for row in assignments] if x])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
