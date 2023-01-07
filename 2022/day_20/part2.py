#!/usr/bin/env python
"""Solves part 2 of the day 18 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, deque


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    orig = [(811589153 * int(x), i) for i, x in enumerate(data)]
    # Put the data into a deque:
    dq = deque(orig)
    # Rearrange according to the puzzle rules:
    for _ in range(10):
        for n2m, j in orig:
            i = dq.index((n2m, j))
            dq.rotate(-i)
            dq.popleft()
            dq.rotate(-n2m)
            dq.appendleft((n2m, j))
    # Compute the answer:
    i0 = list(dq).index(orig[[x for x, y in orig].index(0)])
    answer = sum([x for x, y in [list(dq)[(i0 + 1000) % len(data)], 
        list(dq)[(i0 + 2000) % len(data)], list(dq)[(i0 + 3000) % len(data)]]])
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
