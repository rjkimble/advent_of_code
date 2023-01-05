#!/usr/bin/env python
"""Solves part 1 of the day 15 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict
from re import compile as re_compile


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    parser.add_argument('y', metavar='Y', type=int,
        help='Target y value.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data."""
    return infp.read()


def read_closest(data):
    """Reads the closest beacon data."""
    closest_re = re_compile(r'Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)')
    closest = [list(map(int, closest_re.match(line).groups())) for line in data]
    return closest


def taxicab_dist(pos1, pos2):
    """Computes the taxicab distance between two positions."""
    return abs(int(pos1[0]) - int(pos2[0])) + abs(int(pos1[1]) - int(pos2[1]))


def compute_forbidden_interval(sensor, y, dist_to_closest_beacon):
    """
    Computes the interval on the given line where no beacon can exist because
    beacons there would violate the closest beacon distance for that sensor.
    """
    sx, _ = sensor
    dclosest = dist_to_closest_beacon[sensor]
    tcd = taxicab_dist(sensor, (sx, y))
    if tcd <= dclosest:
        interval = (sx - dclosest + tcd, sx + dclosest - tcd)
        return interval
    return ()


def combine_intervals(intervals):
    """
    Combines the intervals into the smallest set of non overlapping intervals.
    """
    combined = []
    for interval in sorted(intervals):
        if not interval:
            continue
        if not combined:
            combined.append(interval)
            continue
        last = combined[-1]
        if last[1] < interval[0]:
            combined.append(interval)
        else:
            combined[-1] = (min(last[0], interval[0]), max(last[1], interval[1]))
    return combined


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Read and parse the closest beacon data:
    closest = read_closest(data)
    closest_beacon = {(a, b):(c, d) for a, b, c, d in closest}
    beacons = set([closest_beacon[sensor] for sensor in closest_beacon])
    dist_to_closest_beacon = defaultdict(int)
    for xs, ys, xb, yb in closest:
        sensor = (xs, ys)
        dist_to_closest_beacon[sensor] = taxicab_dist(sensor, (xb, yb))
    intervals = [compute_forbidden_interval(sensor, args.y, dist_to_closest_beacon)
        for sensor in closest_beacon]
    combined = combine_intervals(intervals)
    total_interval_size = 0
    for interval in combined:
        total_interval_size += 1 + interval[1] - interval[0]
    # Adjust for beacons:
    for beacon in beacons:
        bx, by = beacon
        for interval in combined:
            if by == args.y:
                for interval in combined:
                    if interval[0] <= by <= interval[1]:
                        total_interval_size -= 1
    # Print the answer:
    print(total_interval_size)
    return


if '__main__' == __name__:
    main()
