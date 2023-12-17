import heapq


class Node:

    def __init__(self, x, y, heat, px, py):
        self.x = x
        self.y = y
        #previous
        self.px = px
        self.py = py
        self.h = heat

    def __lt__(self, other):
        return self.h < other.h


def astar(grid, start, goal, least, most):
    open_set = []
    closed_set = set()

    start_node = Node(*start, 0, 0, 0)
    goal_node = Node(*goal, grid[goal[0]][goal[1]], 0, 0)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        x, y, heat = current_node.x, current_node.y, current_node.h
        px, py = current_node.px, current_node.py

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            return current_node.h

        if (x, y, px, py) in closed_set: continue
        closed_set.add((x, y, px, py))

        #calculate turn only
        for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {(px, py),
                                                            (-px, -py)}:
            a, b, h = x, y, heat
            #most == Number of max moves for crucicles
            for i in range(1, most + 1):
                a, b = a + dx, b + dy
                if -1 < a < len(grid) and -1 < b < len(grid):
                    h += grid[a][b]
                    if i >= least:
                        neighbor_node = Node(a, b, h, dx, dy)
                        heapq.heappush(open_set, neighbor_node)

    return None  # No path found


f = open('day17/example.txt')
f = open('day17/input.txt')
lines = f.read().strip().splitlines()
grid = []
for line in lines:
    grid.append([int(c) for c in line])

start_point = (0, 0)
goal = len(lines) - 1
goal_point = (goal, goal)

path = astar(grid, start_point, goal_point, 1, 3)
if path:
    print("min heat found:", path)
else:
    print("No path found.")

path = astar(grid, start_point, goal_point, 4, 10)
if path:
    print("min heat found part2:", path)
else:
    print("No path found.")
