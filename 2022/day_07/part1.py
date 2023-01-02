#!/usr/bin/env python
"""Solves part 1 of the day 7 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict
from os.path import join


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def listdirs(current_branch):
    """Generates a list of all the directories contained in the current branch."""
    for i in range(len(current_branch)):
        # The replace converts Windows paths to Unix/Linux paths:
        yield join(*current_branch[:1 + i]).replace('\\', '/')


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input)
    # Create a dictionary to hold the directory sizes:
    dirsizes = defaultdict(int)
    # Create a variable to hold the current branch:
    current_branch = []
    # Read the lines:
    for line in data.splitlines():
        line = line.strip()
        if line.startswith('$ cd'):
            # Keep track of the location of the current branch:
            if line == '$ cd ..':
                current_branch.pop()
            elif line.startswith('$ cd /'):
                current_branch = ['/']
            else:
                current_branch.append(line[len('$ cd '):].strip())
        elif line.split()[0].isnumeric():
            # This line represents a file entry. Add its size to every directory
            # on the current branch:
            size = int(line.split()[0])
            for d in listdirs(current_branch):
                dirsizes[d] += size
    # Compute the answer:
    answer = sum([dirsizes[d] for d in dirsizes if dirsizes[d] <= 100000])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
