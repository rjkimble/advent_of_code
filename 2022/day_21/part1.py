#!/usr/bin/env python
"""Solves part 1 of the day 21 puzzle of the 2022 Advent of Code challenge."""

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


def evaluate(a, op, b):
    if '*' == op:
        return a * b
    elif '+' == op:
        return a + b
    elif '-' == op:
        return a - b
    else:
        if a % b:
            return a / b
        return a // b

    
def value(monkey, monkey_expressions):
    expr = monkey_expressions[monkey]
    if 1 == len(expr):
        if expr[0].isnumeric():
            return int(expr[0])
    else:
        m1, op, m2 = expr
        return evaluate(value(m1, monkey_expressions), op, value(m2, 
            monkey_expressions))


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    monkey_expressions = dict([[monkey, expr.split()] for monkey, expr in [
        line.split(':') for line in data]])
    # Print the answer:
    print(value('root', monkey_expressions))
    return


if '__main__' == __name__:
    main()
