#!/usr/bin/env python
"""Solves part 1 of the day 5 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(data):
    """Reads the data and splits it into components essential to solving the puzzle"""
    # Split input into two parts -- stacks and moves:
    stacks_input, moves_input = data.read().split('\n\n')
    stacks_lines = stacks_input.splitlines()
    stacks_count = max([int(n) for n in stacks_lines[-1].split()])
    #print(stacks_count)
    # Read the stacks:
    stacks = defaultdict(list)
    for line_no, line in enumerate(reversed(stacks_lines[:-1])):
        #print(line)
        for stack_no in range(stacks_count):
            crate_entry = line[stack_no * 4:(1 + stack_no) * 4]
            if crate_entry[0] == '[' and crate_entry[2] == ']':
                stacks[stack_no + 1].append(crate_entry[1])
    #print(stacks)
    moves = moves_input.splitlines()
    return stacks, moves


def move(crate_count, from_stack, to_stack):
    """Moves the requested number of crates from one stack to another."""
    # Perform the move, one stack at a time:
    for i in range(crate_count):
        to_stack.append(from_stack.pop())
        
        
def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = args.input
    # Read the data:
    stacks, moves = read_data(data)
    # Move the crates as indicated by the input:
    for move_line in moves:
        crate_count = int(move_line.split()[1])
        from_stack = stacks[int(move_line.split()[3])]
        to_stack = stacks[int(move_line.split()[5])]
        move(crate_count, from_stack, to_stack)
    # Compute the answer:
    answer = ''.join([stacks[i][-1] for i in range(1, 1 + len(stacks))])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
