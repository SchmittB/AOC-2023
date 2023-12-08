import math

f = open('day8/input.txt')
lines = f.read().strip().splitlines()

pattern = lines[0]
node = {}
#fill node dict
for i in lines[2:]:
    node[i[0:3]] = i[7:-1]

# part 1
counter = 0
position = 'AAA'
found = False
while found == False:
    for char in pattern:
        if char == 'R':
            next = node[position][5:]
        else:
            next = node[position][0:3]
        counter += 1
        position = next
        if position == 'ZZZ':
            found = True

print(f"star 1: total {counter}")

#part 2
positions = []
for i in lines[2:]:
    if i[2] == 'A':
        positions.append(i[0:3])  #starting position

counter = 0
found = [False for _ in positions]
while any(item == False for item in found):
    for char in pattern:
        if char == 'R':
            next = [node[position][5:] for position in positions]
        else:
            next = [node[position][0:3] for position in positions]
        counter += 1
        positions = next
        for i, position in enumerate(positions):
            if position.endswith('Z'):
                found[i] = counter

# PPCM de found
result_part2 = math.lcm(*found)

print(f"star 2: total {result_part2}")
