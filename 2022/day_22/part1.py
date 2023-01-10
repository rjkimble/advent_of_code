#!/usr/bin/env python
"""Solves part 1 of the day 22 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict
from re import compile as re_compile


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def new_dir(cur_dir, turn):
    if turn == '-':
        return cur_dir
    elif turn == 'L':
        return '^<v>^'['^<v>^'.index(cur_dir) + 1]
    elif turn == 'R':
        return '^>v<^'['^>v<^'.index(cur_dir) + 1]
    else:
        raise ValueError('Unknown turn: ' + str(turn))


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input)
    map, path = data.split('\n\n')
    map = map.splitlines()
    re_path = re_compile(r'\d+[LR]')
    path_parts = list(re_path.findall(path))
    all_parts = list(path_parts)
    path_parts = [(int(part[:-1]), part[-1]) for part in path_parts]
    path_parts.append((int(path[len(''.join(all_parts)):]), '-'))
    rows = defaultdict(dict)
    cols = defaultdict(dict)
    positions = {}
    for row, line in enumerate(map):
        for col, char in enumerate(line):
            if ' ' != char:
                rows[row][col] = char
                cols[col][row] = char
                positions[(row, col)] = char
    row_ranges = defaultdict(set)
    col_ranges = defaultdict(set)
    for row in rows:
        for col in rows[row]:
            row_ranges[row].add(col)
    for col in cols:
        for row in cols[col]:
            col_ranges[col].add(row)
    row_boundaries = {}
    for row in rows:
        row_boundaries[row] = (min(row_ranges[row]), max(row_ranges[row]))
    col_boundaries = {}
    for col in cols:
        col_boundaries[col] = (min(col_ranges[col]), max(col_ranges[col]))
    next = {}
    # Scan rows and compute next for both left and right:
    for row in rows:
        for col in row_ranges[row]:
            if positions[(row, col)] == '#':
                continue
            # Compute for rightward moves:
            next_col = col + 1
            if next_col > row_boundaries[row][-1]:
                next_col = row_boundaries[row][0]
            if positions[(row, next_col)] == '.':
                next[((row, col), '>')] = ((row, next_col), '>')
            else:
                next[((row, col), '>')] = ((row, col), '>')
            # Compute for leftward moves:
            next_col = col - 1
            if next_col < row_boundaries[row][0]:
                next_col = row_boundaries[row][1]
            if positions[(row, next_col)] == '.':
                next[((row, col), '<')] = ((row, next_col), '<')
            else:
                next[((row, col), '<')] = ((row, col), '<')
    # Scan columns and compute next for both up and down:
    for col in cols:
        for row in col_ranges[col]:
            if positions[(row, col)] == '#':
                continue
            # Compute for downward moves:
            next_row = row + 1
            if next_row > col_boundaries[col][-1]:
                next_row = col_boundaries[col][0]
            if positions[(next_row, col)] == '.':
                next[((row, col), 'v')] = ((next_row, col), 'v')
            else:
                next[((row, col), 'v')] = ((row, col), 'v')
            # Compute for upward moves:
            next_row = row - 1
            if next_row < col_boundaries[col][0]:
                next_row = col_boundaries[col][1]
            if positions[(next_row, col)] == '.':
                next[((row, col), '^')] = ((next_row, col), '^')
            else:
                next[((row, col), '^')] = ((row, col), '^')
    pos = (0, row_boundaries[0][0])
    current_dir = '>'
    for move_count, turn in path_parts:
        for i in range(move_count):
            pos, current_dir = next[(pos, current_dir)]
        current_dir = new_dir(current_dir, turn)
    # Print the answer:
    print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + '>v<^'.index(current_dir))
    return


if '__main__' == __name__:
    main()
