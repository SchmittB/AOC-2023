import re
from collections import defaultdict

#part 1
# f = open('day6/example.txt')
f = open('day6/input.txt')
lines = f.read().strip().splitlines()
Time = re.findall("\d+", lines[0])
Distance = re.findall("\d+", lines[1])
ways = defaultdict(int)

for race in range(0, len(Time)):
    racetime = int(Time[race])
    racedistance = int(Distance[race])
    for i in range(1, racetime):
        distance_travelled = i * (racetime - i)
        if (distance_travelled > racedistance):
            ways[race] = ways[race] + 1

total_1star = ways[0] * ways[1] * ways[2] * ways[3]

#part 2
ways_2 = 0
Time_2 = int(''.join(Time))
Distance_2 = int(''.join(Distance))
for i in range(12_000_00, Time_2):  #greedy search > 12 000 000
    distance_travelled = i * (Time_2 - i)
    if (distance_travelled > Distance_2):
        ways_2 = ways_2 + 1

print(f"star 1: total {total_1star}")
print(f"star 2: total {ways_2}")
