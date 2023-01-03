#!/usr/bin/env python
"""Solves part 2 of the day 11 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, times, plus, monkey, create_monkeys


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip()
    # Split the input into monkey descriptions:
    monkeys_text = data.split('\n\n')
    # Create the monkeys:
    monkeys = create_monkeys(monkeys_text)
    # In order to keep the worry levels within reason, we need to change the
    # per the instructions. The only thing that makes sense is to reduce the
    # worry level my taking the residue after dividing by the product (or 
    # least common multiple) of the monkey test values. So the first thing to
    # do is to compute that number (modulo).
    #
    # The key point here is that the idea is to not have to reduce the worry
    # levels. However, they quickly grow to unreasonable sizes. In order to 
    # arrive at the same result, we reduce them by finding the residue as 
    # described above.
    mod = 1
    for monkey_number in monkeys:
        mod *= monkeys[monkey_number].test
    # Run the 10000 rounds per the puzzle instructions:
    for _ in range(10000):
        for monkey_number in monkeys:
            m = monkeys[monkey_number]
            for worry_level in m.worry_levels:
                worry_level = m.new_worry_level(worry_level)
                m.inspection_count += 1
                worry_level = worry_level % mod
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
