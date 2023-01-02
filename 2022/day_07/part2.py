#!/usr/bin/env python
"""Solves part 2 of the day 7 puzzle of the 2022 Advent of Code challenge."""


from part1 import defaultdict, join, get_args, read_data, listdirs


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
    # Compute the amount of unused space:
    unused = 70000000 - dirsizes['/']
    # Find the sizes of the candidate directories (don't need the actual paths):
    candidates = [dirsizes[d] for d in dirsizes if dirsizes[d] >= 30000000 - unused]
    # Compute the answer:
    answer = min(candidates)
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
