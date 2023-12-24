import sympy


class Hailstone:

    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy


file = 'day24/example.txt'
file = 'day24/input.txt'
f = open(file, 'r', newline='')
blocks = f.read().splitlines()

lines = [
    list(map(int,
             block.replace(' @', ',').split(', '))) for block in blocks
]

list = []
#construct list of Hailstone
for l in lines:
    list.append(Hailstone(*l))
total = 0

for i, hs1 in enumerate(list):
    for hs2 in list[:i]:
        #Ax+By=C equation
        a1, b1, c1 = hs1.a, hs1.b, hs1.c
        a2, b2, c2 = hs2.a, hs2.b, hs2.c

        #parallel case
        if a1 * b2 == b1 * a2:
            continue

        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
            if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0
                   for hs in (hs1, hs2)):
                total += 1

print("part1", total)

#PART 2
xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []
for i, l in enumerate(list):
    equations.append((xr - l.sx) * (l.vy - vyr) - (yr - l.sy) * (l.vx - vxr))
    equations.append((yr - l.sy) * (l.vz - vzr) - (zr - l.sz) * (l.vy - vyr))
    if i < 2:
        continue
    answers = [
        soln for soln in sympy.solve(equations)
        if all(x % 1 == 0 for x in soln.values())
    ]
    if len(answers) == 1:
        break

answer = answers[0]

print("answer part 2", answer[xr] + answer[yr] + answer[zr])
print(i)
