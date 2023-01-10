#!/usr/bin/env python
"""Code specific to processing sample.txt."""


wraps = {}
wraps[(1, '>')] = (6, '<')
wraps[(6, '>')] = (1, '<')
wraps[(1, '<')] = (3, 'v')
wraps[(3, '^')] = (1, '>')
wraps[(1, '^')] = (2, 'v')
wraps[(2, '^')] = (1, 'v')
wraps[(2, '<')] = (6, '^')
wraps[(6, 'v')] = (2, '>')
wraps[(2, 'v')] = (5, '^')
wraps[(5, 'v')] = (2, '^')
wraps[(3, 'v')] = (5, '>')
wraps[(5, '<')] = (3, '^')
wraps[(4, '>')] = (6, 'v')
wraps[(6, '^')] = (4, '<')


edge_wraps = '''
1>,6>
1<,3^
1^,2^
2<,6v
2v,5v
3v,5<
4>,6^
'''.strip().splitlines()


cells = {}
cells[(1, '>')] = [(row, 11) for row in range(4)]
cells[(6, '>')] = [(row, 15) for row in range(11, 7, -1)]
cells[(1, '<')] = [(row, 8) for row in range(4)]
cells[(3, '^')] = [(4, col) for col in range(4, 8)]
cells[(1, '^')] = [(0, col) for col in range(8, 12)]
cells[(2, '^')] = [(4, col) for col in range(3, -1, -1)]
cells[(2, '<')] = [(row, 0) for row in range(4, 8)]
cells[(6, 'v')] = [(11, col) for col in range(15, 11, -1)]
cells[(2, 'v')] = [(7, col) for col in range(4)]
cells[(5, 'v')] = [(11, col) for col in range(11, 7, -1)]
cells[(3, 'v')] = [(7, col) for col in range(4, 8)]
cells[(5, '<')] = [(row, 8) for row in range(11, 7, -1)]
cells[(4, '>')] = [(row, 11) for row in range(4, 8)]
cells[(6, '^')] = [(8, col) for col in range(15, 11, -1)]


