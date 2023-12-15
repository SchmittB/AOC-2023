from collections import defaultdict


def hash(string):
    temp = 0
    for c in string:
        temp += ord(c)
        temp = temp * 17
        temp = temp % 256
    return temp


def calculate_focal(hashmap):
    total = 0
    for i in hashmap:
        for j, l in enumerate(hashmap[i]):
            total += (i + 1) * (j + 1) * int(hashmap[i][l])
    return total


file = 'day15/example.txt'
file = 'day15/input.txt'
f = open(file)
seq = f.read().split(',')
# print(seq)
# seq = ['HASH']

total = 0
for s in seq:
    total += hash(s)

print(total)

hashmap: defaultdict[int, dict[str, int]] = defaultdict(dict)
# PART2
for s in seq:
    #DELETE
    if (index := s.find('-')) > -1:
        label = s[0:index]
        box = hash(label)
        hashmap[box].pop(label, None)
    #ADD
    if (index := s.find('=')) > -1:
        label = s[0:index]
        focal = s[-1]
        box = hash(label)
        hashmap[box][label] = focal
print(calculate_focal(hashmap))
