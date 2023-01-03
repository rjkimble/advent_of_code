#!/usr/bin/env python
"""Solves part 1 of the day 10 puzzle of the 2022 Advent of Code challenge."""

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


def times(a, b):
    """Computes the product of the two arguments."""
    return a * b


def plus(a, b):
    """Computes the sum of the two arguments."""
    return a + b


class monkey:
    """Class for instantiating a monkey instance."""
    def __init__(self, starting, inspect, test, throw_true, throw_false):
        self.worry_levels = list(map(int, starting.split(', ')))
        
        def new_worry_level(old):
            parts = inspect.split()
            if parts[2] == 'old':
                parts[2] = old
            else:
                parts[2] = int(parts[2])
            if '+' == parts[1]:
                return old + parts[2]
            elif '*' == parts[1]:
                return old * parts[2]
        
        self.new_worry_level = new_worry_level

        def throw_to(worry_level):
            if worry_level % test:
                return throw_false
            else:
                return throw_true
        
        self.throw_to = throw_to
        self.inspection_count = 0
        self.test = test


def create_monkeys(monkeys_text):
    """
    Parse the monkey descriptions and use the results to instatiate a monkey
    instance for each description.
    """
    monkeys = {}
    for text in monkeys_text:
        lines = text.splitlines()
        monkey_number = int(lines[0].split(':')[0].split()[-1])
        starting = lines[1].split(':')[-1].strip()
        inspect = lines[2].split('=')[-1].strip()
        test = int(lines[3].split()[-1])
        throw_true = int(lines[4].split()[-1])
        throw_false = int(lines[5].split()[-1])
        monkeys[monkey_number] = monkey(starting, inspect, test, throw_true, throw_false)
    return monkeys


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip()
    # Split the input into monkey descriptions:
    monkeys_text = data.split('\n\n')
    # Create the monkeys:
    monkeys = create_monkeys(monkeys_text)
    # Run the 20 rounds per the puzzle instructions:
    for _ in range(20):
        for monkey_number in monkeys:
            m = monkeys[monkey_number]
            for worry_level in m.worry_levels:
                worry_level = m.new_worry_level(worry_level)
                m.inspection_count += 1
                worry_level = worry_level // 3
                target = m.throw_to(worry_level)
                monkeys[target].worry_levels.append(worry_level)
            m.worry_levels.clear()
    # Compute the answer:
    activities = list(sorted([monkeys[n].inspection_count for n in monkeys]))
    answer = activities[-1] * activities[-2]
    # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
