#!/usr/bin/env python
"""Solves part 2 of the day 17 puzzle of the 2022 Advent of Code challenge."""

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


def create_rock(pattern_number, height):
    return set([(x, y + height) for (x, y) in rock_patterns[pattern_number % 5]])


def move_rock(rock, direction):
    if direction == '<':
        return set([(x - 1, y) for (x, y) in rock])
    elif direction == '>':
        return set([(x + 1, y) for (x, y) in rock])
    elif direction == 'v':
        return set([(x, y - 1) for (x, y) in rock])
    else:
        raise ValueError('Invalid direction: ' + str(direction))


def drop_rock(pattern_number, height, data):
    global current_move_index
    global current_height
    global current_structure
    moves = []
    rock = create_rock(pattern_number, height)
    # Extend left and right walls as necessary:
    for x, y in rock:
        current_structure.add((-1, y))
        current_structure.add((7, y))
    dropping = True
    while dropping:
        current_move = data[current_move_index % len(data)]
        moves.append(current_move)
        current_move_index += 1
        test_rock = move_rock(rock, current_move)
        if test_rock.isdisjoint(current_structure):
            rock = test_rock
        test_rock = move_rock(rock, 'v')
        if test_rock.isdisjoint(current_structure):
            rock = test_rock
        else:
            dropping = False
    current_structure.update(rock)
    current_height = max(current_height, max([y for (x, y) in rock]))


# Creating a global variable holding the 5 rock shapes:
rock_shapes = '''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''.strip().split('\n\n')


# Create a variable to hold the rock shapes in a more useful structure:
rock_patterns = []
for rock_shape in rock_shapes:
    rock_pattern = set()
    lines = rock_shape.splitlines()
    for row, line in enumerate(reversed(lines)):
        for col, char in enumerate(line):
            if char == '#':
                rock_pattern.add((col + 2, row))
    rock_patterns.append(rock_pattern)
pattern_heights = [max([1 + y for (x,y) in pattern]) for pattern in rock_patterns]


def main():
    global current_height
    global current_move_index
    global current_structure
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip()
    # Create the starting structure for the narrow chamber:
    starting_structure = set()
    for i in range(-1, 8):
        starting_structure.add((i, -1))
    for i in range(0, 4):
        starting_structure.add((-1, i))
        starting_structure.add((7, i))
    # Initialize necessary variables:
    current_height = -1
    current_structure = set(starting_structure)
    current_move_index = 0
    current_pattern = 0
    # Drop the rocks:
    current_heights = [-1]
    for _ in range(1000000):
        drop_rock(current_pattern, current_height + 4, data)
        current_heights.append(current_height)
        current_pattern += 1
    # We've dropped one million rocks and recorded the heights after each drop.
    # Now we need to do a little analysis to see how many iterations are
    # involved in repeating the incremental differences pattern:
    def diff(a, b):
        return b - a
    diffs = list(map(diff, current_heights[:-1], current_heights[1:]))
    # Take a snapshot of the last 20 diffs:
    diffs_snap = list(diffs[-20:])
    # Now iterate back through the last 100000 diffs to see how often this
    # snapshot pattern repeats itself:
    repeats = []
    for i in range(100000):
        if diffs[1000000 - 20 - i:1000000 - i] == diffs_snap:
            repeats.append(i)
    # Generate the diffs of the repeats:
    repeats_diffs = list(map(diff, repeats[:-1], repeats[1:]))
    if 1 == len(set(repeats_diffs)):
        repeat_interval = list(set(repeats_diffs))[0]
    #print(repeat_interval)
    height_interval = current_heights[100000] - current_heights[100000 - repeat_interval]
    #print(height_interval)
    final_residue = 1000000000000 % repeat_interval
    current_residue = 1000000 % repeat_interval
    nearby_move = 1000000 + final_residue - current_residue
    if 1000000 < nearby_move:
        nearby_move -= repeat_interval
    #print(nearby_move)
    nearby_height = current_heights[nearby_move]
    final_height = nearby_height + height_interval * ((1000000000000 - nearby_move) // repeat_interval)
    # Print the answer:
    print(final_height + 1)
    return


if '__main__' == __name__:
    main()
