#!/usr/bin/env python
"""Solves part 2 of the day 5 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, defaultdict


def move2(crate_count, from_stack, to_stack):
    """
    Moves the requested number of crates from one stack to another.
    The dummy stack is a simple mechanism designed to reverse the order of the
    crates in order to comply with the demands of part 2.
    """
    dummy = []
    for i in range(crate_count):
        dummy.append(from_stack.pop())
    for i in range(crate_count):
        to_stack.append(dummy.pop())


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
        move2(crate_count, from_stack, to_stack)
    # Compute the answer:
    answer = ''.join([stacks[i][-1] for i in range(1, 1 + len(stacks))])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
