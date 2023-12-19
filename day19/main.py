from itertools import groupby

file = 'day19/input.txt'
file = 'day19/example.txt'
f = open(file, 'r', newline='')
board = f.read().strip().splitlines()

# Group by the empty string
grouped_lists = [
    list(group) for key, group in groupby(board, lambda x: x == '')
]
workflow = grouped_lists[0]
parts = grouped_lists[-1]

for i in board:
    print(i)
