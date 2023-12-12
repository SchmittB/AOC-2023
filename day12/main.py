from functools import cache


@cache
def recurse(s, sizes, num_in_group=0):
    if not s:
        # Is this a solution? Did we handle and close all groups?
        return not sizes and not num_in_group
    num_sols = 0
    # If next letter is a "?", we branch
    possible = [".", "#"] if s[0] == "?" else s[0]
    for c in possible:
        if c == "#":
            # Extend current group
            num_sols += recurse(s[1:], sizes, num_in_group + 1)
        else:
            if num_in_group:
                # If we were in a group that can be closed, close it
                if sizes and sizes[0] == num_in_group:
                    num_sols += recurse(s[1:], sizes[1:])
            else:
                # If we are not in a group, move on to next symbol
                num_sols += recurse(s[1:], sizes)
    return num_sols


# file = 'day12/example.txt'
file = 'day12/input.txt'
board = list(open(file))
sum_part1 = 0
board = [line.strip().split(' ') for line in board]
springs = [line[0] + '.' for line in board]  # +'.' to close input
sizes = [list(map(int, line[1].split(','))) for line in board]

print(board)

for i in range(len(board)):
    nb_arrangement = 0
    nb_arrangement = recurse(springs[i], tuple(sizes[i]))
    sum_part1 += nb_arrangement

print(sum_part1)

#part 2

springs = ['?'.join([s[0]] * 5) + '.' for s in board]  # +'.' to close input
sizes_temp = [','.join([s[1]] * 5) for s in board]
sizes = [list(map(int, line.split(','))) for line in sizes_temp]

sum_part2 = 0

for i in range(len(board)):
    nb_arrangement = 0
    nb_arrangement = recurse(springs[i], tuple(sizes[i]))
    sum_part2 += nb_arrangement

print(sum_part2)
