#!/usr/bin/env python
"""Solves part 2 of the day 18 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, adjacent_cubes
from collections import defaultdict


def compute_distances(source, air_cubes, neighbors):
    """Computes the distances of all air cubes from the source air cube."""
    dist={source:0}
    dfinal = defaultdict(set)
    remaining = set([air_cube for air_cube in air_cubes])
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
                    distances_found = True
        dnext += 1
    return dist


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Read the cubes:
    cubes = set([tuple(map(int, line.split(','))) for line in data])
    # Compute the x, y, and z ranges of the cubes -- we place a buffer of 1
    # around all the cubes in order to have a starting point for computing
    # the unreachable spaces inside the cube complex:
    xrange = min([x for x, y, z in cubes]) - 1, 2 + max([x for x, y, z in cubes])
    yrange = min([y for x, y, z in cubes]) - 1, 2 + max([y for x, y, z in cubes])
    zrange = min([z for x, y, z in cubes]) - 1, 2 + max([z for x, y, z in cubes])
    # Generate the set of "air cubes" enclosed by the ranges above:
    air_cubes = set()
    for x in range(*xrange):
        for y in range(*yrange):
            for z in range(*zrange):
                if (x, y, z) not in cubes:
                    air_cubes.add((x, y, z))
    # Compute the air cube neighbors (air cubes adjacent to an aircube):
    neighbors = defaultdict(set)
    for air_cube in air_cubes:
        for adj_cube in adjacent_cubes(air_cube):
            if adj_cube in air_cubes:
                neighbors[air_cube].add(adj_cube)
                neighbors[adj_cube].add(air_cube)
    # Compute the distance to each air cube reachable from the one with least
    # coordinates in each dimenstion:
    distances = compute_distances((xrange[0], yrange[0], zrange[0]), air_cubes, 
        neighbors)
    # Compute the area of the free sides reachable from the outside:
    free_sides = 0
    cubes_plus_trapped = cubes.union([cube for cube in air_cubes if cube not in 
        distances])
    for cube in cubes_plus_trapped:
        for adj in adjacent_cubes(cube):
            if adj in cubes_plus_trapped:
                continue
            free_sides += 1
    # Print the answer:
    print(free_sides)
    return


if '__main__' == __name__:
    main()
