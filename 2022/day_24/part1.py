#!/usr/bin/env python
"""Solves part 1 of the day 24 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


def gcd(m, n):
    """Returns the greatest common divisor of m and n."""
    if not m:
        return n
    if not n:
        return m
    if m < n:
        return gcd(m, n % m)
    return gcd(m % n, n)


def lcm(m, n):
    """Returns the least common multiple of m and n."""
    if not m or not n:
        return 0
    return m * n // gcd(m, n)


def blizzard_pos_by_round(round, starting_blizzard_pos, blizzard_dir, valley_row_range, valley_col_range):
    starting_row = starting_blizzard_pos[0]
    starting_col = starting_blizzard_pos[1]
    valley_width = valley_col_range[-1] - valley_col_range[0] + 1
    valley_height = valley_row_range[-1] - valley_row_range[0] + 1
    if blizzard_dir == '^':
        blizzard_row = (starting_row - 1 - round) % valley_height + 1
        return (blizzard_row, starting_col)
    if blizzard_dir == 'v':
        blizzard_row = (starting_row - 1 + round) % valley_height + 1
        return (blizzard_row, starting_col)
    if blizzard_dir == '<':
        blizzard_col = (starting_col - 1 - round) % valley_width + 1
        return (starting_row, blizzard_col)
    if blizzard_dir == '>':
        blizzard_col = (starting_col - 1 + round) % valley_width + 1
        return (starting_row, blizzard_col)


def find_shortest(source, target, vertices, neighbors):
    dist={source:0}
    dfinal = defaultdict(set)
    remaining = set([vertex for vertex in vertices])
    remaining.remove(source)
    dfinal[0].add(source)
    dnext = 1
    distances_found = True
    while distances_found:
        distances_found = False
        for v in dfinal[dnext - 1]:
            for n in neighbors[v]:
                if n in remaining:
                    dfinal[dnext].add(n)
                    dist[n] = dnext
                    remaining.remove(n)
                    if target == n[0]:
                        # print('Target', target, 'found after round', n[1])
                        return n[1]
                    distances_found = True
        dnext += 1
    return -1


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input)

    lines = data.strip().splitlines()
    row_count = len(lines)
    col_count = len(lines[0])
    map = {}
    for r in range(row_count):
        for c in range(col_count):
            map[(r, c)] = lines[r][c]

    valley_row_range = range(1, len(lines) - 1)
    valley_col_range = range(1, len(lines[0]) - 1)
    valley_width = valley_col_range[-1] - valley_col_range[0] + 1
    valley_height = valley_row_range[-1] - valley_row_range[0] + 1

    blizzard_starting_positions = set()
    for r in valley_row_range:
        for c in valley_col_range:
            pos = (r, c)
            if map[pos] in '<^>v':
                blizzard_starting_positions.add((pos, map[pos]))

    blizzard_maps = defaultdict(set)
    for round in range(lcm(valley_height, valley_width)):
        for blizzard_pos, blizzard_dir in blizzard_starting_positions:
            blizzard_maps[round].add(blizzard_pos_by_round(round, blizzard_pos, blizzard_dir, valley_row_range, valley_col_range))

    free_space_maps = defaultdict(set)
    valley_map = {(0, 1), (row_count - 1, col_count - 2)}
    for r in valley_row_range:
        for c in valley_col_range:
            valley_map.add((r, c))
    for round in blizzard_maps:
        free_space_maps[round] = valley_map.difference(blizzard_maps[round])

    adjacents = defaultdict(set)
    for pos in valley_map:
        adjacents[pos].add(pos)
        r, c = pos
        adjacents[pos].update(valley_map.intersection([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]))

    vertices = set()
    edges = set()
    neighbors = defaultdict(set)
    backneighbors = defaultdict(set)
    for round in range(1400):
        vertices.update([(pos, round) for pos in free_space_maps[round % lcm(valley_height, valley_width)]])
    for round in range(1399):
        for pos in free_space_maps[round % lcm(valley_height, valley_width)]:
            for adj in adjacents[pos]:
                if adj in free_space_maps[(round + 1) % lcm(valley_height, valley_width)]:
                    edges.add(((pos, round), (adj, round + 1)))
                    neighbors[(pos, round)].add((adj, round + 1))
                    backneighbors[(adj, round)].add((pos, round + 1))

    answer = find_shortest(((0, 1), 0), (row_count - 1, col_count - 2), vertices, neighbors)

  # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
