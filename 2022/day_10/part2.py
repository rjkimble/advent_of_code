#!/usr/bin/env python
"""Solves part 2 of the day 10 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Process the instructions:
    x = [1]
    for line in data:
        if 'noop' == line.strip():
            x.append(x[-1])
        if line.startswith('addx'):
            value = int(line.split()[1])
            x.append(x[-1])
            x.append(x[-1] + value)
    # Create a blank display array:
    pixels = []
    for i in range(6):
        pixels.append([' '] * 40)
    # Populate the display:
    for i in range(240):
        sprite_mid = x[i]
        sprite_range = [sprite_mid - 1, sprite_mid, sprite_mid + 1]
        row = (i - 1) // 40
        if i % 40 in sprite_range:
            pixels[row][i % 40] = '#'
        else:
            pixels[row][i % 40] = '.'
    # Compute the answer:
    answer = '\n'.join([''.join(pixels[row]) for row in range(6)])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
