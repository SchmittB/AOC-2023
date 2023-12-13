def is_mirrored(block, sep):
    row_to_check = min(len(block) - sep, sep)
    good = True
    for i in range(row_to_check):
        if block[sep + i] != block[sep - i - 1]:
            good = False
    return good


def fix_smudge(block, index):
    row_to_check = min(len(block) - index, index)
    for i in range(row_to_check):
        string1 = block[index + i]
        string2 = block[index - i - 1]
        common_characters = [(char, index)
                             for index, char in enumerate(string1)
                             if char in string2[index]]

        if len(common_characters) == len(string1) - 1:  #found smudge
            block[index - i - 1] = block[index + i]  #fix smudge
            return block, index
    return block, 0


def equal_or_smudge(block1, block2):
    if block1 == block2:
        return True
    common_characters = [(char, index) for index, char in enumerate(block1)
                         if char in block2[index]]

    if len(common_characters) == len(block1) - 1:  #found smudge
        return True
    return False


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
        if block[i] == block[i + 1] and is_mirrored(block, i + 1):
            horizontal_sep = i + 1

    row_above = horizontal_sep

    #COLUMN
    array_of_columns = list(zip(*block))
    for i in range(0, len(array_of_columns) - 1):
        if array_of_columns[i] == array_of_columns[i + 1] and is_mirrored(
                array_of_columns, i + 1):
            vertical_sep = i + 1

    col_left = vertical_sep

    sum_part1 += row_above * 100 + col_left

print(f"star 1: total {sum_part1}")

sum_part2 = 0
# part 2
for block in blocks:
    horizontal_sep = 0
    vertical_sep = 0
    row_above = 0
    col_left = 0

    #ROW

    for i in range(0, len(block) - 1):
        if equal_or_smudge(block[i], block[i + 1]):
            block, i_fixed = fix_smudge(block, i + 1)
            if i_fixed > 0:
                horizontal_sep = i_fixed
                break

    row_above = horizontal_sep

    #COLUMN
    array_of_columns = list(zip(*block))
    for i in range(0, len(array_of_columns) - 1):
        if equal_or_smudge(array_of_columns[i], array_of_columns[i + 1]):
            array_of_columns, i_fixed = fix_smudge(array_of_columns, i + 1)
            if vertical_sep > 0:
                vertical_sep = i_fixed
                break

    col_left = vertical_sep

    sum_part2 += row_above * 100 + col_left

print(f"star 2: total {sum_part2}")
