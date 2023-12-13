ps = list(map(str.split, open('day13/input.txt').read().split('\n\n')))


def f(p):
    for i in range(len(p)):
        if sum(c != d for l, m in zip(p[i - 1::-1], p[i:])
               for c, d in zip(l, m)) == s:
            return i
    else:
        return 0


for s in 0, 1:
    print(sum(100 * f(p) + f([*zip(*p)]) for p in ps))
