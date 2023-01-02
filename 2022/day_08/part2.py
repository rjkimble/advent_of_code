#!/usr/bin/env python
"""Solves part 2 of the day 8 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Create a list of lists of tree heights as ints:
    trees = [[int(t) for t in data[i]] for i in range(len(data))]
    # Compute the scenic scores and keep track of the max:
    scenic_score = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            left_score = 0
            for k in range(j - 1, -1, -1):
                left_score += 1
                if trees[i][k] >= trees[i][j]:
                    break
            right_score = 0
            for k in range(j + 1, len(trees[i])):
                right_score += 1
                if trees[i][k] >= trees[i][j]:
                    break
            top_score = 0
            for k in range(i - 1, -1, -1):
                top_score += 1
                if trees[k][j] >= trees[i][j]:
                    break
            bottom_score = 0
            for k in range(i + 1, len(trees)):
                bottom_score += 1
                if trees[k][j] >= trees[i][j]:
                    break
            scenic_score = max(scenic_score, left_score * right_score * top_score * bottom_score)
    # Print the answer:
    print(scenic_score)
    return


if '__main__' == __name__:
    main()
