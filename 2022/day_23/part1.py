#!/usr/bin/env python
"""Solves part 1 of the day 23 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict, deque


def find_move(pos, elf_pos, dirs):
    """
    Computes the next position to which the elf can move according to the puzzle
    directions.
    """ 
    offset = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    r, c = pos
    dir_neighbors = {}
    dir_neighbors['N'] = set([(r - 1, c - 1), (r - 1, c), (r - 1, c + 1)])
    dir_neighbors['S'] = set([(r + 1, c - 1), (r + 1, c), (r + 1, c + 1)])
    dir_neighbors['W'] = set([(r - 1, c - 1), (r, c - 1), (r + 1, c - 1)])
    dir_neighbors['E'] = set([(r - 1, c + 1), (r, c + 1), (r + 1, c + 1)])
    neighbors = set()
    for dir in dirs:
        neighbors.update(dir_neighbors[dir])
    if not elf_pos.intersection(neighbors):
        return None
    for dir in dirs:
        if not dir_neighbors[dir].intersection(elf_pos):
            off = offset[dir]
            return (pos[0] + off[0], pos[1] + off[1])
    return None


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
    data = read_data(args.input)
    # Compute the starting positions:
    starting_elf_pos = set()
    for row, line in enumerate(data.splitlines()):
        for col, char in enumerate(line):
            if char == '#':
                starting_elf_pos.add((row, col))
    starting_move_dirs = deque('NSWE')

    positions = set(starting_elf_pos)
    dirs = deque(starting_move_dirs)
    for round in range(10):
        potential_moves = {}
        potential_move_counts = defaultdict(int)
        for pos in set(positions):
            move = find_move(pos, set(positions), dirs)
            if move:
                #print(pos, move)
                potential_moves[pos] = move
                potential_move_counts[move] += 1
        for pos in set(positions):
            if pos in potential_moves:
                move = potential_moves[pos]
                if 1 == potential_move_counts[move]:
                    positions.remove(pos)
                    positions.add(move)
        dirs.rotate(-1)

    height = max([pos[0] for pos in positions]) - min([pos[0] for pos in positions]) + 1
    width = max([pos[1] for pos in positions]) - min([pos[1] for pos in positions]) + 1

    # Print the answer:
    print(height * width - len(positions))
    return


if '__main__' == __name__:
    main()
