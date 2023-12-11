def calculate_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def sum_shortest_path(galaxy):
    sum = 0
    nb_galaxy = len(galaxy)
    for g in range(nb_galaxy):
        for i in range(g + 1, nb_galaxy):
            sum = sum + calculate_distance(galaxy[g], galaxy[i])
    return sum


# file = 'day11/example.txt'
file = 'day11/input.txt'
board = list(open(file))
sum_part1 = 0

board = [line.strip() for line in board]
board_part2 = board.copy()

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
sum_part1 = sum_shortest_path(galaxy)
print(sum_part1)

#PART 2
expansion_factor = 1_000_000
# position of galaxy in NON expanded space
galaxy2 = [[r, c] for r in range(len(board_part2))
           for c in range(len(board_part2[0])) if board_part2[r][c] not in '.']

delta = 0
for i in line_to_insert:
    for j in galaxy2:
        if j[0] > i + delta:
            j[0] = j[0] + expansion_factor - 1
    delta += expansion_factor - 1

delta = 0
for i in col_to_insert:
    for j in galaxy2:
        if j[1] > i + delta:
            j[1] = j[1] + expansion_factor - 1
    delta += expansion_factor - 1

sum_part2 = sum_shortest_path(galaxy2)
print(sum_part2)
