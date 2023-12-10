def get_differences(array_int):
    return [array_int[i + 1] - array_int[i] for i in range(len(array_int) - 1)]


#part 1

# f = open('day9/example.txt')
f = open('day9/input.txt')
lines = f.read().strip().splitlines()
sum_part1 = 0
sum_part2 = 0
differences = []

for line in lines:
    differences = []
    differences.append([int(i) for i in line.split(' ')])  # init top row
    j = 1
    Found = False
    # create tree of history line by line
    while not Found:
        differences.append(get_differences(differences[j - 1]))
        j += 1
        if all(difference == 0 for difference in differences[j - 1]):
            Found = True

    # extrapolate at last position
    for k in range(len(differences) - 2, -1, -1):
        differences[k].append(differences[k][-1] + differences[k + 1][-1])

    extrapolated_value = differences[0][-1]
    sum_part1 = sum_part1 + extrapolated_value

    # extrapolate ar first position (part 2)
    for k in range(len(differences) - 2, -1, -1):
        differences[k].insert(0, differences[k][0] - differences[k + 1][0])

    extrapolated_value = differences[0][0]
    sum_part2 = sum_part2 + extrapolated_value

print(f"star 1: total {sum_part1}")
print(f"star 2: total {sum_part2}")
