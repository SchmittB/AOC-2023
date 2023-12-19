def accept(item, name = 'in'):
    if name == 'R':
        return False
    if name == 'A':
        return True
    rules, fallback = workflow[name]
    for r in rules:
        if r[1] == '<': 
            if item[r[0]] < r[2]:
                return accept(item, r[3])
        else:
            if item[r[0]] > r[2]:
                return accept(item, r[3])
    return accept(item, fallback)

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflow[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, min(n - 1, hi))
            F = (max(n, lo), hi)
        else:
            T = (max(n + 1, lo), hi)
            F = (lo, min(n, hi))
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)
            
    return total

file = 'day19/example.txt'
file = 'day19/input.txt'
f = open(file, 'r', newline='')
block1, block2 = f.read().strip().split('\r\n\r\n')

workflow = {}
total = 0

for i in block1.splitlines():
    name, rest = i[:-1].split('{')
    rules = rest.split(',')
    workflow[name] = ([], rules.pop())
    for rule in rules:
        key, target = rule.split(':')
        spec, cmp, nb = key[0], key[1], int(key[2:])
        workflow[name][0].append((spec, cmp, nb,target))

for j in block2.splitlines():
    specs = j[1:-1].split(",")
    item = {}
    for s in specs:
        char, n = s.split('=')
        item[char] = int(n)
    if accept(item):
        total += sum(item.values())
    
print(total)
# PART 2
print(count({key: (1, 4000) for key in "xmas"}))
