import sys
from dataclasses import dataclass

sys.setrecursionlimit(1_000_000)


@dataclass
class board_point:
    x: int
    y: int
    symbol: str
    energy: bool = False


def get_symbol(x, y):
    filtered_objects = [obj for obj in grid if obj.x == x and obj.y == y]
    return filtered_objects[0].symbol


def energize(p, grid):
    filtered_objects = [obj for obj in grid if obj.x == p[0] and obj.y == p[1]]
    filtered_objects[0].energy = True


def nb_energize(grid):
    filtered_objects = [obj for obj in grid if obj.energy == True]
    return len(filtered_objects)


def next_step(start_pos, dir, grid):
    global visited
    while (start_pos, dir) not in visited:
        if dir == 'R':
            p = (start_pos[0], start_pos[1] + 1)
        if dir == 'L':
            p = (start_pos[0], start_pos[1] - 1)
        if dir == 'N':
            p = (start_pos[0] - 1, start_pos[1])
        if dir == 'S':
            p = (start_pos[0] + 1, start_pos[1])

        visited.append((start_pos, dir))

        if p[0] < 0 or p[0] > len(
                board[0]) - 1 or p[1] < 0 or p[1] > len(board) - 1:
            return

        energize(p, grid)

        next_symbol = get_symbol(p[0], p[1])

        if next_symbol == '.':
            next_step(p, dir, grid)
        if next_symbol == '/':
            new_dir = 'N' if dir in 'R' else 'S' if dir in 'L' else 'R' if dir in 'N' else 'L' if dir in 'S' else ''
            next_step(p, new_dir, grid)
        if next_symbol == '\\':
            new_dir = 'S' if dir in 'R' else 'N' if dir in 'L' else 'L' if dir in 'N' else 'R' if dir in 'S' else ''
            next_step(p, new_dir, grid)
        if next_symbol == '-':
            if dir in ['R', 'L']:
                next_step(p, dir, grid)
            else:
                next_step(p, 'R', grid)
                next_step(p, 'L', grid)
        if next_symbol == '|':
            if dir in ['N', 'S']:
                next_step(p, dir, grid)
            else:
                next_step(p, 'N', grid)
                next_step(p, 'S', grid)


file = 'day16/example.txt'
file = 'day16/input.txt'
f = open(file, 'r', newline='')
board = f.read().strip().splitlines()
sum_part1 = 0
found = False
loop = []

grid = [
    board_point(r, c, board[r][c]) for r in range(len(board))
    for c in range(len(board[0]))
]

print(grid[0])

starting_start_pos = (0, -1)
starting_dir = 'R'

visited = []
next_step(starting_start_pos, starting_dir, grid)
print(nb_energize(grid))
