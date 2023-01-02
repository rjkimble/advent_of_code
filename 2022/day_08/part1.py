#!/usr/bin/env python
"""Solves part 1 of the day 8 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Create a list of lists of tree heights as ints:
    trees = [[int(t) for t in data[i]] for i in range(len(data))]
    # Scan the rows and columns and build "arrays" (lists of lists)
    # to compute visibility:
    from_left = []
    for i in range(len(trees)):
        from_left_row = []
        for j in range(len(trees[i])):
            if j:
                from_left_row.append(max(from_left_row[-1], trees[i][j]))
            else:
                from_left_row.append(trees[i][0])
        from_left.append(from_left_row)
    from_right = []
    for i in range(len(trees)):
        from_right_row = []
        for j in range(len(trees[i])):
            if j:
                from_right_row.append(max(from_right_row[-1], trees[i][len(trees[i]) - 1 - j]))
            else:
                from_right_row.append(trees[i][len(trees[i]) -1 - j])
        from_right.append(list(reversed(from_right_row)))
    from_top = []
    for i in range(len(trees)):
        if i:
            from_top_row = []
            for j in range(len(trees[i])):
                from_top_row.append(max(from_top[i - 1][j], trees[i][j]))
            from_top.append(from_top_row)
        else:
            from_top.append(trees[0])
    from_bottom = []
    for i in range(len(trees)):
        if i:
            from_bottom_row = []
            for j in range(len(trees[i])):
                from_bottom_row.append(max(from_bottom[i - 1][j], trees[len(trees) -1 - i][j]))
            from_bottom.append(from_bottom_row)
        else:
            from_bottom.append(trees[-1])
    from_bottom = list(reversed(from_bottom))
    # Compute the answer using the above arrays:
    # Start by counting all the boundary trees:
    visible_count = 2 * (len(trees) - 1 + len(trees[0]) - 1)
    # Now scan the rows and columns in both directions:
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            if (trees[i][j] > from_left[i][j - 1] or trees[i][j] > from_right[i][j + 1]
                or trees[i][j] > from_top[i - 1][j] or trees[i][j] > from_bottom[i + 1][j]):
                visible_count += 1
    # Print the answer:
    print(visible_count)
    return


if '__main__' == __name__:
    main()
