import math

# file = 'day11/example.txt'
file = 'day11/input.txt'
board = list(open(file))
sum_part1 = 0

board = [line.strip() for line in board]

# expand galaxies ROW
line_to_insert = []
for i, line in enumerate(board):
    if all(char == '.' for char in line):
        line_to_insert.append(i)

delta = 0
for i in line_to_insert:
    board.insert(i + delta, '.' * len(board[0]))
    delta += 1

# Transpose the array (convert rows to columns) using zip
array_of_columns = list(zip(*board))

# expand galaxies COLUMN
col_to_insert = []
for i, col in enumerate(array_of_columns):
    if all(char == '.' for char in col):
        col_to_insert.append(i)

delta = 0
for i in col_to_insert:
    array_of_columns.insert(i + delta, ['.'] * len(array_of_columns[0]))
    delta += 1

expanded_board = list(zip(*array_of_columns))

# position of galaxy in expanded space
galaxy = [(r, c) for r in range(len(expanded_board))
          for c in range(len(expanded_board[0]))
          if expanded_board[r][c] not in '.']

print(galaxy)


def calculate_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


nb_galaxy = len(galaxy)
for g in range(nb_galaxy):
    for i in range(g + 1, nb_galaxy):
        sum_part1 = sum_part1 + calculate_distance(galaxy[g], galaxy[i])

print(sum_part1)
