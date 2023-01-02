#!/usr/bin/env python
"""Solves part 2 of the day 5 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data



def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input)
    # Compute the answer:
    answer = [len(set(data[i:i+14])) for i in range(len(data) - 3)].index(14) + 14
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
