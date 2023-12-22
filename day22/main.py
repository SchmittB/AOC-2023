from collections import deque

file = 'day22/example.txt'
file = 'day22/input.txt'
f = open(file, 'r', newline='')
blocks = f.read().splitlines()

blocks = [
    list(map(int,
             block.replace('~', ',').split(','))) for block in blocks
]

# print(blocks)

# sort by height (z index)
blocks.sort(key=lambda bricks: bricks[2])

# print(blocks)


# intersect of 2 bricks a and b on the x and y axis
# return bool if intersect
def intersect(a, b):
    #X
    bool_x = max(a[0], b[0]) <= min(a[3], b[3])
    #Y
    bool_y = max(a[1], b[1]) <= min(a[4], b[4])
    return bool_x and bool_y


# O(n2) complexity
for i, brick in enumerate(blocks):
    min_z = 1
    for brick_2 in blocks[:i]:
        if intersect(brick, brick_2):
            min_z = max(min_z, brick_2[5] + 1)
    brick[5] -= brick[2] - min_z
    brick[2] = min_z

blocks.sort(key=lambda bricks: bricks[2])
# print(blocks)

#brick support everything else
k_support_v = {i: set() for i in range(len(blocks))}
#everything else support brick
v_support_k = {i: set() for i in range(len(blocks))}

for j, upper in enumerate(blocks):
    for i, lower in enumerate(blocks[:j]):
        if intersect(lower, upper) and upper[2] == lower[5] + 1:
            k_support_v[i].add(j)
            v_support_k[j].add(i)

total = 0

for i in range(len(blocks)):
    if all(len(v_support_k[j]) >= 2 for j in k_support_v[i]):
        total += 1

print('part1', total)

#part 2
#BFS
total = 0
for i in range(len(blocks)):
    q = deque(j for j in k_support_v[i] if len(v_support_k[j]) == 1)
    falling = set(q)
    falling.add(i)

    while q:
        j = q.popleft()
        for k in k_support_v[j] - falling:
            if v_support_k[k] <= falling:
                q.append(k)
                falling.add(k)

    total += len(falling) - 1

print('part2', total)
