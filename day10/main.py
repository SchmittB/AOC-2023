import random

import matplotlib.path as mpath


#part 1
def tup(x, y):
    return (board[x][y], x, y)


def symbol(x, y):
    if x > len(board) - 1 or y > len(board[x]) - 1:  # cas en dehors du board
        return '.'
    return (board[x][y])


def get_next_pos(pos):
    x = pos[1]
    y = pos[2]

    #for S starting position
    if pos[0] == 'S':
        # Create a list of conditions
        conditions = [(x, y + 1, '-J7'), (x, y - 1, '-FL'), (x + 1, y, '|LJ'),
                      (x - 1, y, '|F7')]

        # Shuffle the list randomly
        random.shuffle(conditions)

        for c in conditions:  #randomly check if next position
            if symbol(c[0], c[1]) in c[2] and tup(c[0], c[1]) not in loop:
                return tup(c[0], c[1])

        # if symbol(x, y + 1) in '-J7' and tup(x, y + 1) not in loop:
        #     return tup(x, y + 1)
        # if symbol(x, y - 1) in '-FL' and tup(x, y - 1) not in loop:
        #     return tup(x, y - 1)
        # if symbol(x + 1, y) in '|LJ' and tup(x + 1, y) not in loop:
        #     return tup(x + 1, y)
        # if symbol(x - 1, y) in '|F7' and tup(x - 1, y) not in loop:
        #     return tup(x - 1, y)

    last_x = loop[-2][1]
    last_y = loop[-2][2]
    delta_x = x - last_x
    delta_y = y - last_y

    if pos[0] == '-':
        return tup(x, y + delta_y)
    if pos[0] == '|':
        return tup(x + delta_x, y)
    if pos[0] == 'J':
        return tup(x - delta_y, y - delta_x)
    if pos[0] == '7':
        return tup(x + delta_y, y + delta_x)
    if pos[0] == 'F':
        return tup(x - delta_y, y - delta_x)
    if pos[0] == 'L':
        return tup(x + delta_y, y + delta_x)


# file = 'day10/example.txt'
file = 'day10/input.txt'
board = list(open(file))
sum_part2 = 0
found = False
loop = []

pipes = {(board[r][c], r, c)
         for r in range(len(board))
         for c in range(len(board[0]) - 1) if board[r][c] not in '.'}

starting_pos = [tup for tup in pipes if tup[0] == 'S'][0]

print(starting_pos)
loop.append(starting_pos)

while not found:
    loop.append(get_next_pos(loop[-1]))

    if loop[-1][0] == 'S':
        found = True

star1 = len(loop) // 2
print(f"star 1: total {star1}")

# part 2
polygon_vertices = [(t[1], t[2]) for t in loop]
area = mpath.Path(polygon_vertices)

board_point = {(r, c)
               for r in range(len(board))
               for c in range(len(board[0]) - 1)
               if (r, c) not in polygon_vertices}

for i in board_point:
    if area.contains_point(i):
        sum_part2 += 1

print(f"star 2: total {sum_part2}")
