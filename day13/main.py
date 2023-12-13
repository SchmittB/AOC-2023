def Is_mirrored(block, sep):
    row_to_check = min(len(block) - sep, sep)
    good = True
    for i in range(row_to_check):
        if block[sep + i] != block[sep - i - 1]:
            good = False
    return good


# file = 'day13/example.txt'
file = 'day13/input.txt'
f = open(file)
board = f.read().strip().splitlines()
board.append('')
sum_part1 = 0
blocks = []

starting_block = 0
for i, j in enumerate(board):
    if j == '':
        blocks.append(board[starting_block:i])
        starting_block = i + 1

for block in blocks:
    horizontal_sep = 0
    vertical_sep = 0
    row_above = 0
    col_left = 0
    #ROW
    for i in range(0, len(block) - 1):
        if block[i] == block[i + 1] and Is_mirrored(block, i + 1):
            horizontal_sep = i + 1

    row_above = horizontal_sep

    #COLUMN
    array_of_columns = list(zip(*block))
    for i in range(0, len(array_of_columns) - 1):
        if array_of_columns[i] == array_of_columns[i + 1] and Is_mirrored(
                array_of_columns, i + 1):
            vertical_sep = i + 1

    col_left = vertical_sep
    #check horizontal_sep

    sum_part1 += row_above * 100 + col_left

print(f"star 1: total {sum_part1}")
