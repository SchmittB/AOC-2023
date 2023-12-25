import random
from collections import defaultdict


#statistically, we traverse graph at random a 1000 times and top 3 bottlneck will be our wire to cut
def random_graph_search(graph):
    nodes = list(graph.keys())
    edge_count = defaultdict(int)
    for _ in range(1000):
        seen = set()
        start, dest = random.choices(nodes, k=2)
        q = [(start, [start])]
        while q:
            n, path = q.pop(0)
            if n == dest:
                for a, b in zip(path[:-1], path[1:]):
                    edge_count[(min(a, b), max(a, b))] += 1
                break
            seen.add(n)
            q.extend((c, path + [c]) for c in graph[n] if c not in seen)
    to_remove = sorted(edge_count.items(), key=lambda x: x[1],
                       reverse=True)[:3]
    return to_remove


def remove_edges_and_count(graph, edges_to_remove):
    for a, _ in edges_to_remove:
        one, two = [*a]
        graph[one].remove(two)
        graph[two].remove(one)
    seen, q = set(), [random.choice(list(graph.keys()))]
    while q:
        n = q.pop()
        seen.add(n)
        q.extend(c for c in graph[n] if c not in seen)
    return (len(graph) - len(seen)) * len(seen)


file = 'day25/example.txt'
file = 'day25/input.txt'
f = open(file, 'r', newline='')
blocks = f.read().splitlines()

components = defaultdict(list)

for block in blocks:
    name, conn = block.split(': ')[0], block.split(': ')[1]
    for i in conn.split(' '):
        components[name].append(i)
        components[i].append(name)

single = [i for i in components if len(components[i]) == 1]
print(components)

node_to_remove = random_graph_search(components)
total = remove_edges_and_count(components, node_to_remove)
print(total)
