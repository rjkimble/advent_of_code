#!/usr/bin/env python
"""Code specific to processing input.txt."""


face_ranges = {}
face_ranges[1] = (range(50), range(50, 100))
face_ranges[2] = (range(50), range(100, 150))
face_ranges[3] = (range(50, 100), range(50, 100))
face_ranges[4] = (range(100, 150), range(50))
face_ranges[5] = (range(100, 150), range(50, 100))
face_ranges[6] = (range(150, 200), range(50))


wraps = {}
wraps[(1, '^')] = (6, '>')
wraps[(6, '<')] = (1, 'v')
wraps[(1, '<')] = (4, '>')
wraps[(4, '<')] = (1, '>')
wraps[(2, '^')] = (6, '^')
wraps[(6, 'v')] = (2, 'v')
wraps[(2, '>')] = (5, '<')
wraps[(5, '>')] = (2, '<')
wraps[(2, 'v')] = (3, '<')
wraps[(3, '>')] = (2, '^')
wraps[(3, '<')] = (4, 'v')
wraps[(4, '^')] = (3, '>')
wraps[(5, 'v')] = (6, '<')
wraps[(6, '>')] = (5, '^')


edge_wraps = '''
1^,6<
1<,4<
2^,6v
2>,5>
2v,3>
3<,4^
5v,6>
'''.strip().splitlines()


cells = {}
cells[(1, '^')] = [(0, col) for col in face_ranges[1][1]]
cells[(6, '<')] = [(row, 0) for row in face_ranges[6][0]]
cells[(1, '<')] = [(row, 50) for row in face_ranges[1][0]]
cells[(4, '<')] = [(row, 0) for row in reversed(face_ranges[4][0])]
cells[(2, '^')] = [(0, col) for col in face_ranges[2][1]]
cells[(6, 'v')] = [(199, col) for col in face_ranges[6][1]]
cells[(2, '>')] = [(row, 149) for row in face_ranges[2][0]]
cells[(5, '>')] = [(row, 99) for row in reversed(face_ranges[5][0])]
cells[(2, 'v')] = [(49, col) for col in face_ranges[2][1]]
cells[(3, '>')] = [(row, 99) for row in face_ranges[3][0]]
cells[(3, '<')] = [(row, 50) for row in face_ranges[3][0]]
cells[(4, '^')] = [(100, col) for col in face_ranges[4][1]]
cells[(5, 'v')] = [(149, col) for col in face_ranges[5][1]]
cells[(6, '>')] = [(row, 49) for row in face_ranges[6][0]]


