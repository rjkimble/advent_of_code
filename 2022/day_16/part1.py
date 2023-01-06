#!/usr/bin/env python
"""Solves part 1 of the day 16 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict
from itertools import permutations
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


def pressure_relief(valve, current_time, valves):
    """
    Computes the value of the pressure relief for the valve when opened at the
    current time.
    """
    return valves[valve] * (30 - current_time)


def compute_distances(source, valves, tunnels):
    """
    Computes the lengths of the shortest paths to the other valves given the
    supplied tunnels. This is quick enough to be called multiple times.
    """
    dist={source:0}
    dfinal = defaultdict(set)
    remaining = set([valve for valve in valves])
    remaining.remove(source)
    dfinal[0].add(source)
    dnext = 1
    distances_found = True
    while distances_found:
        distances_found = False
        for v in dfinal[dnext - 1]:
            for n in tunnels[v]:
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
    # Parse the input data:
    re_input = re_compile(r'^Valve (?P<valve>[A-Z]+) has flow rate='
        '(?P<flow_rate>\d+); tunnels? leads? to valves? (?P<targets>[A-Z]+(, '
        '[A-Z]+)*)$')
    valves = {}
    tunnels = defaultdict(list)
    for line in data:
        m = re_input.match(line)
        valve = m.group('valve')
        flow_rate = int(m.group('flow_rate'))
        targets = m.group('targets').split(', ')
        valves[valve] = flow_rate
        tunnels[valve].extend(targets)
    # Identify the valves worth opening:
    worth_opening = set([valve for valve in valves if valves[valve]])
    # Compute shortest distances:
    all_pairs_distances = {}
    all_pairs_distances2 = {}
    for valve in valves:
        distances = compute_distances(valve, valves, tunnels)
        all_pairs_distances2[valve] = distances
        for valve2 in distances:
            all_pairs_distances[(valve, valve2)] = distances[valve2]
    wo_ordered = [x[-1] for x in list(sorted([(all_pairs_distances[('AA', wo)], wo) for wo in worth_opening]))]
    worth_opening_distances = {}
    worth_opening_distances2 = defaultdict(dict)
    for w in worth_opening:
        for w2 in worth_opening:
            worth_opening_distances[(w, w2)] = all_pairs_distances[(w, w2)]
    # Compute the maximum pressure relief and a path that achieves that.
    max_pressure_relief = 0
    best_path = []
    perm_ct = 0
    # We'll consider all paths that include up to 8 of the worth opening valves:
    for path in permutations(wo_ordered, min(8, len(wo_ordered))):
        perm_ct += 1
        current_pos = 'AA'
        current_time = 0
        current_relief = 0
        for new_pos in path:
            # Compute the time at which the new valve will be opened:
            current_time += all_pairs_distances[(current_pos, new_pos)] + 1
            if 30 <= current_time:
                break
            current_pos = new_pos
            current_relief += pressure_relief(current_pos, current_time, valves)
            if current_relief > max_pressure_relief:
                max_pressure_relief = current_relief
                best_path = list(path)
                #print(max_pressure_relief, path, perm_ct)
    # Print the answer:
    print(max_pressure_relief)
    return


if '__main__' == __name__:
    main()
