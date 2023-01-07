#!/usr/bin/env python
"""Solves part 2 of the day 21 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, evaluate, value


def sign(x):
    """Returns the "sign" of x."""
    if 0 < x:
        return 1
    elif 0 > x:
        return -1
    return 0


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    monkey_expressions = dict([[monkey, expr.split()] for monkey, expr in [
        line.split(':') for line in data]])
    monkey_expressions['root'][1] = '-'
    v0 = value('root', monkey_expressions)
    h0 = 1
    for _ in range(100):
        h1 = 10 * value('humn', monkey_expressions)
        monkey_expressions['humn'] = [str(h1)]
        v1 = value('root', monkey_expressions)
        if sign(v0) != sign(v1):
            break
    # Find the answer:
    while value('root', monkey_expressions):
        monkey_expressions['humn'] = [str(h0)]
        v0 = value('root', monkey_expressions)
        monkey_expressions['humn'] = [str(h1)]
        v1 = value('root', monkey_expressions)
        answer = (h0 + h1) // 2
        monkey_expressions['humn'] = [str(answer)]
        v2 = value('root', monkey_expressions)
        if sign(v2) == sign(v0):
            h0 = answer
        elif sign(v2) == sign(v1):
            h1 = answer
        else:
            break
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
