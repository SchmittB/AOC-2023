import math
from collections import deque


class Module:

    def __init__(self, type, name, outputs):
        self.type = type
        self.name = name
        self.outputs = outputs

        if type == '%':
            self.memory = 'off'
        else:
            self.memory = {}


file = 'day20/example.txt'
file = 'day20/input.txt'
f = open(file, 'r', newline='')
block = f.read().splitlines()

modules = {}

for i in block:
    outputs = i.split(' -> ')[1].split(", ")
    types = i.split(' -> ')[0]
    if types == 'broadcaster':
        name = type = 'broadcaster'
        modules[name] = Module(type, name, outputs)
    else:
        type, name = types[0], types[1:]
        modules[name] = Module(type, name, outputs)

for m in modules.values():
    if m.type == '&':
        for em in modules.values():
            if m.name in em.outputs:
                m.memory[em.name] = 'low'

modules2 = modules.copy()

hi = lo = 0

for _ in range(1000):
    lo += 1
    q = deque([("broadcaster", x, "low")
               for x in modules['broadcaster'].outputs])

    while q:
        origin, target, pulse = q.popleft()

        if pulse == "low":
            lo += 1
        else:
            hi += 1

        if target not in modules:
            continue

        module = modules[target]

        if module.type == "%":
            if pulse == "low":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "high" if module.memory == "on" else "low"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = "low" if all(
                x == "high" for x in module.memory.values()) else "high"
            for x in module.outputs:
                q.append((module.name, x, outgoing))

print("part1", lo * hi)

press = 0
(feed, ) = [
    name for name, module in modules2.items() if "rx" in module.outputs
]

cycle_lengths = {}
seen = {name: 0 for name, module in modules2.items() if feed in module.outputs}
while True:
    press += 1
    q = deque([("broadcaster", x, "low")
               for x in modules2['broadcaster'].outputs])

    while q:
        origin, target, pulse = q.popleft()

        if target not in modules2:
            continue

        module = modules2[target]

        if module.name == feed and pulse == "high":
            seen[origin] += 1

            if origin not in cycle_lengths:
                cycle_lengths[origin] = press
            else:
                assert press == seen[origin] * cycle_lengths[origin]

            if all(seen.values()):
                x = 1
                for cycle_length in cycle_lengths.values():
                    x = x * cycle_length // math.gcd(x, cycle_length)
                print(x)
                exit(0)

        if module.type == "%":
            if pulse == "low":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "high" if module.memory == "on" else "low"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = "low" if all(
                x == "high" for x in module.memory.values()) else "high"
            for x in module.outputs:
                q.append((module.name, x, outgoing))
