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

hi = lo = 0
rm = {}

for press in range(1000):
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

print(lo * hi)
