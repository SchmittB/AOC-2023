
class Module:
    def __init__(self, type, name, outputs):
        self.type = type
        self.name = name
        self.outputs = outputs

        if type == '%':
            self.memory = 'off'
        else:
            self.memory = {}



file = 'day20/input.txt'
file = 'day20/example.txt'
f = open(file, 'r', newline='')
block = f.read().splitlines()

modules = {}

for i in block:
    outputs = i.split(' -> ')[1].split(", ")
    types = i.split(' -> ')[0]
    if types == 'broadcaster':
        modules[name] = Module(type, 'broadcaster', outputs)
    else:
        type,name = types[0], types[1:]
        modules[name] = Module(type, name, outputs)