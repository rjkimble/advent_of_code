#!/usr/bin/env python
"""Solves part 2 of the day 23 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, defaultdict, deque, find_move


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
    round = 0
    move_made = True
    while move_made:
        move_made = False
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
                    move_made = True
        dirs.rotate(-1)
        round += 1

    # Print the answer:
    print(round)
    return


if '__main__' == __name__:
    main()
