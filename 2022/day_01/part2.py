#!/usr/bin/env python
"""Solves part 2 of the day 1 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args


def main():
    # Reuse get_args from part 1:
    args = get_args()
    # Read the input file:
    data = args.input.read()
    # Split into individual calorie lists:
    cal = data.split('\n\n')
    # Compute individual calorie entries as lists of integers:
    cal2 = [list(map(int, row.split())) for row in cal]
    # Sum each list to compute calorie totals:
    cal3 = [sum(row) for row in cal2]
    # Sort cal3 into descending order:
    cal3.sort(reverse=True)
    # Sum the three largest entries:
    answer = sum(cal3[:3])
    # Print it:
    print(answer)
    return


if '__main__' == __name__:
    main()
