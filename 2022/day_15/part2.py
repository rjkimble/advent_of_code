#!/usr/bin/env python
"""Solves part 2 of the day 15 puzzle of the 2022 Advent of Code challenge."""


from part1 import defaultdict, ArgumentParser, read_data, read_closest, taxicab_dist
from part1 import compute_forbidden_interval, combine_intervals


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    parser.add_argument('size', metavar='SIZE', type=int,
        help='Target y value.')
    return parser.parse_args()


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Read and parse the closest beacon data:
    closest = read_closest(data)
    closest_beacon = {(a, b):(c, d) for a, b, c, d in closest}
    dist_to_closest_beacon = defaultdict(int)
    for xs, ys, xb, yb in closest:
        sensor = (xs, ys)
        dist_to_closest_beacon[sensor] = taxicab_dist(sensor, (xb, yb))
    # Find the gap:
    for y in range(args.size + 1):
        intervals = list(sorted([compute_forbidden_interval(sensor, y, 
            dist_to_closest_beacon) for sensor in closest_beacon]))
        combined = combine_intervals(intervals)
        if 1 < len(combined):
            beacon_pos = ((combined[0][1] + combined[1][0]) // 2, y)
            break
    # Print the answer:
    print(4000000 * beacon_pos[0] + beacon_pos[1])
    return


if '__main__' == __name__:
    main()
