import re

total_1star = 0
parts = {}
board = list(open('day3/input.txt'))
# position of all symbols
symbols = {(r, c)
           for r in range(140)
           for c in range(140) if board[r][c] not in '01234566789.'}

# print(chars)

for r, row in enumerate(board):
    for m in re.finditer(r'\d+', row):  # all numbers in board
        # area close to number (include diagonals)
        number_area = {(r + s, c + d)
                       for s in (-1, 0, 1)
                       for d in (-1, 0, 1)
                       for c in range(*m.span())}
        for intersection in symbols & number_area:  # intersection of 2 sets
            total_1star = total_1star + int(m[0])
            # create parts dict from symbol
            if intersection in parts:
                parts[intersection].append(int(m[0]))
            else:
                parts[intersection] = [int(m[0])]

total_2star = sum(p[0] * p[1] for p in parts.values() if len(p) == 2)
print(f"star 1: total {total_1star}")
print(f"star 2: total {total_2star}")
