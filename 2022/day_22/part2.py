#!/usr/bin/env python
"""Solves part 2 of the day 22 puzzle of the 2022 Advent of Code challenge."""


from part1 import get_args, read_data, re_compile, new_dir, defaultdict


def gen_tuples(x):
    return [(int(x[0]), x[1]), (int(x[3]), x[4])]


def flip(dir):
    return '<^>v<^'['<^>v<^'.index(dir) + 2]


def main():
    # Read the command line:
    args = get_args()
    # Read the input file:
    data = read_data(args.input)
    # Import the appropriate extra module:
    if args.input.name == 'input.txt':
        from input import wraps, cells, edge_wraps
    elif args.input.name == 'sample.txt':
        from sample import wraps, cells, edge_wraps

    map2, path2 = data.split('\n\n')
    map2 = map2.splitlines()

    rows = defaultdict(dict)
    cols = defaultdict(dict)
    positions = {}
    for row, line in enumerate(map2):
        for col, char in enumerate(line):
            if ' ' != char:
                rows[row][col] = char
                cols[col][row] = char
                positions[(row, col)] = char

    row_ranges = defaultdict(set)
    col_ranges = defaultdict(set)
    for row in rows:
        for col in rows[row]:
            row_ranges[row].add(col)
    for col in cols:
        for row in cols[col]:
            col_ranges[col].add(row)

    row_boundaries = {}
    for row in rows:
        row_boundaries[row] = (min(row_ranges[row]), max(row_ranges[row]))
    col_boundaries = {}
    for col in cols:
        col_boundaries[col] = (min(col_ranges[col]), max(col_ranges[col]))

    next = {}
    # Scan rows and compute next for both left and right:
    for row in rows:
        for col in row_ranges[row]:
            if positions[(row, col)] == '#':
                continue
            next[((row, col), '>')] = ((row, col), '>')
            next[((row, col), '<')] = ((row, col), '<')
            # Compute for rightward moves:
            next_col = col + 1
            if next_col <= row_boundaries[row][-1]:
                if positions[(row, next_col)] == '.':
                    next[((row, col), '>')] = ((row, next_col), '>')
            # Compute for leftward moves:
            next_col = col - 1
            if next_col >= row_boundaries[row][0]:
                if positions[(row, next_col)] == '.':
                    next[((row, col), '<')] = ((row, next_col), '<')
    # Scan columns and compute next for both up and down:
    for col in cols:
        for row in col_ranges[col]:
            if positions[(row, col)] == '#':
                continue
            next[((row, col), 'v')] = ((row, col), 'v')
            next[((row, col), '^')] = ((row, col), '^')
            # Compute for downward moves:
            next_row = row + 1
            if next_row <= col_boundaries[col][-1]:
                if positions[(next_row, col)] == '.':
                    next[((row, col), 'v')] = ((next_row, col), 'v')
            # Compute for upward moves:
            next_row = row - 1
            if next_row >= col_boundaries[col][0]:
                if positions[(next_row, col)] == '.':
                    next[((row, col), '^')] = ((next_row, col), '^')

    next_edge = dict([gen_tuples(ew) for ew in edge_wraps])
    next_edge.update(dict([list(reversed(gen_tuples(ew))) for ew in edge_wraps]))

    for edge in next_edge:
        target = next_edge[edge]
        edge_cells = cells[edge]
        target_cells = cells[target]
        edge_dir = edge[1]
        target_dir = flip(target[1])
        for i in range(len(edge_cells)):
            pos = edge_cells[i]
            if positions[pos] == '#':
                continue
            target_pos = target_cells[i]
            if positions[target_pos] == '#':
                next[(pos, edge_dir)] = ((pos, edge_dir))
            else:
                next[(pos, edge_dir)] = ((target_pos, target_dir))

    re_path = re_compile(r'\d+[LR]')
    path_parts = list(re_path.findall(path2))
    all_parts = list(path_parts)
    path_parts = [(int(part[:-1]), part[-1]) for part in path_parts]
    path_parts.append((int(path2[len(''.join(all_parts)):]), '-'))

    pos = (0, row_boundaries[0][0])
    current_dir = '>'
    for move_count, turn in path_parts:
        for i in range(move_count):
            pos, current_dir = next[(pos, current_dir)]
        current_dir = new_dir(current_dir, turn)

    final_password = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + '>v<^'.index(current_dir)

    # Print the answer:
    print(final_password)
    return


if '__main__' == __name__:
    main()
