#!/usr/bin/env python
"""Solves part 1 of the day 12 puzzle of the 2022 Advent of Code challenge."""

from argparse import ArgumentParser
from collections import defaultdict
from string import ascii_lowercase


def get_args():
    """Reads the arguments from the command line."""
    parser = ArgumentParser()
    parser.add_argument('input', metavar='INPUT', type=open,
        help='File containing the puzzle input.')
    return parser.parse_args()


def read_data(infp):
    """Reads the data"""
    return infp.read()


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
                neighbors[(row + 1, col)].add((row, col))
            if 1 >= V[(row + 1, col)] - V[(row, col)]:
                neighbors[(row, col)].add((row + 1, col))
    # For edges between columns:
    for row in range(len(data)):
        for col in range(len(data[row]) - 1):
            if 1 >= abs(V[(row, col)] - V[(row, col + 1)]):
                neighbors[(row, col + 1)].add((row, col))
            if 1 >= abs(V[(row, col + 1)] - V[(row, col)]):
                neighbors[(row, col)].add((row, col + 1))
    # Compute the shortest distances from the source (S) until the distance to 
    # E is found:
    dist = {S:0}
    # Create a dictionary to hold the sets of vertices of a given distance:
    dfinal = defaultdict(set)
    dfinal[0].add(S)
    # Create a set to hold the vertices for which we have already found the
    # shortest distance:
    finished = set()
    finished.add(S)
    # Create a set to hold the vertices for which we still have to compute the
    # distance from S:
    remaining = set([v for v in V])
    remaining.remove(S)
    # Initialize the next distance to consider:
    dnext = 1
    distances_found = True
    while distances_found:
        distances_found = False
        for v in dfinal[dnext - 1]:
            for n in neighbors[v]:
                if n in remaining:
                    dfinal[dnext].add(n)
                    dist[n] = dnext
                    remaining.remove(n)
                    distances_found = True
        dnext += 1
    # Print the answer:
    print(dist[E])
    return


if '__main__' == __name__:
    main()
