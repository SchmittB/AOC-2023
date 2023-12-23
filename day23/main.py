file = 'day23/example.txt'
file = 'day23/input.txt'
f = open(file, 'r', newline='')
blocks = f.read().splitlines()

start = (0, blocks[0].index('.'))
end = (len(blocks) - 1, blocks[-1].index('.'))

points = [start, end]

#find crossroad tile because grid has few of them
for i, row in enumerate(blocks):
    for j, ch in enumerate(row):
        if ch == '#':
            continue
        neighbors = 0
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < len(blocks) and 0 <= nj < len(
                    blocks[0]) and blocks[ni][nj] != '#':
                neighbors += 1

        if neighbors >= 3:
            points.append((i, j))

print(points)

dirs = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "#": []
}

#create graph
graph = {pt: {} for pt in points}

#DFS
for sr, sc in points:
    stack = [(0, sr, sc)]
    seen = {(sr, sc)}

    while stack:
        n, r, c = stack.pop()

        if n != 0 and (r, c) in points:
            graph[(sr, sc)][(r, c)] = n
            continue

        for dr, dc in dirs[blocks[r][c]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(blocks) and 0 <= nc < len(
                    blocks[0]) and blocks[nr][nc] != "#" and (nr,
                                                              nc) not in seen:
                stack.append((n + 1, nr, nc))
                seen.add((nr, nc))

#DFS recursively
seen = set()


def dfs(pt):
    if pt == end:
        return 0

    m = -float("inf")

    seen.add(pt)
    for nx in graph[pt]:
        if nx not in seen:
            m = max(m, dfs(nx) + graph[pt][nx])
    seen.remove(pt)

    return m


print(dfs(start))

# PART 2
#create graph
graph = {pt: {} for pt in points}

#DFS
for sr, sc in points:
    stack = [(0, sr, sc)]
    seen = {(sr, sc)}

    while stack:
        n, r, c = stack.pop()

        if n != 0 and (r, c) in points:
            graph[(sr, sc)][(r, c)] = n
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(blocks) and 0 <= nc < len(
                    blocks[0]) and blocks[nr][nc] != "#" and (nr,
                                                              nc) not in seen:
                stack.append((n + 1, nr, nc))
                seen.add((nr, nc))

#DFS recursively
seen = set()

print(dfs(start))
