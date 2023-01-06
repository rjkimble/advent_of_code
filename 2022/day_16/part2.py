#!/usr/bin/env python
"""Solves part 2 of the day 16 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, defaultdict, permutations, re_compile
from part1 import pressure_relief, compute_distances


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
    # Compute the maximum pressure relief for an elephant, considering path 
    # lengths up to one half the number of worth opening valves. Record the
    # maximum relief values for each set of valves considered:
    elephant_contributions = defaultdict(int)
    elephant_best_paths = defaultdict(tuple)
    max_pressure_relief = 0
    best_path = []
    perm_ct = 0
    for path in permutations(wo_ordered, len(wo_ordered) // 2):
        elephant_key = frozenset(path)
        current_pos = 'AA'
        current_time = 4
        current_relief = 0
        for new_pos in path:
            current_time += all_pairs_distances[(current_pos, new_pos)] + 1
            if 30 <= current_time:
                break
            current_pos = new_pos
            current_relief += pressure_relief(current_pos, current_time, valves)
            if current_relief > elephant_contributions[elephant_key]:
                elephant_contributions[elephant_key] = current_relief
                elephant_best_paths[elephant_key] = list(path)
    # Now compute the maximum relief using the remaining worth opening valves.
    # The number of valves we'll consider is either the same as that of the
    # elephants, or one more if there is an odd number of such valves:
    max_pressure_relief = 0
    best_path = []
    elephant_best_key = frozenset()
    for path in permutations(wo_ordered, len(wo_ordered) - (len(wo_ordered) // 2)):
        current_pos = 'AA'
        current_time = 4
        elephant_key = frozenset(worth_opening.difference(path))
        elephant_relief = elephant_contributions[elephant_key]
        current_relief = elephant_relief
        for new_pos in path:
            current_time += all_pairs_distances[(current_pos, new_pos)] + 1
            if 30 <= current_time:
                break
            current_pos = new_pos
            current_relief += pressure_relief(current_pos, current_time, valves)
            if current_relief > max_pressure_relief:
                max_pressure_relief = current_relief
                best_path = list(path)
                elephant_best_key = elephant_key
                #print(current_relief, '=', elephant_relief, '+', current_relief - elephant_relief)
    # Print the answer:
    print(max_pressure_relief)
    return


if '__main__' == __name__:
    main()
