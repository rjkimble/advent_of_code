#!/usr/bin/env python
"""Solves part 2 of the day 12 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, defaultdict, ascii_lowercase


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input).strip().splitlines()
    # Set up a height array and build a graph:
    height = {}
    for letter in ascii_lowercase:
        height[letter] = ascii_lowercase.index(letter)
    V = {}
    S = (-1, -1)
    E = {-1, -1}
    neighbors = defaultdict(set)
    # Populate the vertices array:
    for row in range(len(data)):
        for col in range(len(data[row])):
            h = data[row][col]
            V[(row, col)] = h
            if h == 'S':
                S = (row, col)
                V[S] = 'a'
            elif h == 'E':
                E = (row, col)
                V[E] = 'z'
            V[(row, col)] = height[V[(row, col)]]
    # Populate the neighbors dictionary:
    # For edges between rows:
    for row in range(len(data) - 1):
        for col in range(len(data[row])):
            if 1 >= V[(row, col)] - V[(row + 1, col)]:
                neighbors[(row, col)].add((row + 1, col))
            if 1 >= V[(row + 1, col)] - V[(row, col)]:
                neighbors[(row + 1, col)].add((row, col))
    # For edges between columns:
    for row in range(len(data)):
        for col in range(len(data[row]) - 1):
            if 1 >= abs(V[(row, col)] - V[(row, col + 1)]):
                neighbors[(row, col)].add((row, col + 1))
            if 1 >= abs(V[(row, col + 1)] - V[(row, col)]):
                neighbors[(row, col + 1)].add((row, col))
    # Compute the shortest distances from E until a vertex of min height is 
    # found:
    dist = {E:0}
    # Create a dictionary to hold the sets of vertices of a given distance:
    dfinal = defaultdict(set)
    dfinal[0].add(E)
    # Create a set to hold the vertices for which we still have to compute the
    # distance from E:
    remaining = set([v for v in V])
    remaining.remove(E)
    # Initialize the next distance to consider:
    dnext = 1
    distances_found = True
    shortest_not_found = True
    answer = 'Not found.'
    while distances_found and shortest_not_found:
        distances_found = False
        for v in dfinal[dnext - 1]:
            for n in neighbors[v]:
                if not V[n]:
                    # We've found a vertex of min height.
                    answer = dnext
                    shortest_not_found = False
                    break
                if shortest_not_found and n in remaining:
                    dfinal[dnext].add(n)
                    dist[n] = dnext
                    remaining.remove(n)
                    distances_found = True
            if shortest_not_found:
                continue
            else:
                break
        dnext += 1
   # Print the answer:
    print(answer)
    return


if '__main__' == __name__:
    main()
