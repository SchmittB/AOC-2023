import numpy as np


def calculate_load(platform):
    total_load = 0
    rows, cols = len(platform), len(platform[0])

    for row in range(rows):
        for col in range(cols):
            if platform[row][col] == 'O':
                total_load += (rows - row)
            elif platform[row][col] == '#':
                continue  # Cube-shaped rocks don't contribute to load

    return total_load


def tilt(rocks):
    for j, l in enumerate(rocks):
        for i, r in enumerate(l):
            if r == 'O':
                ihere = i
                while True:
                    inext = ihere - 1
                    if inext < 0:
                        break
                    if rocks[j][inext] == '.':
                        rocks[j][inext] = 'O'
                        rocks[j][ihere] = '.'
                        ihere = inext
                    else:
                        break


def tilt_platform(platform):
    vertical_platform = list(zip(*platform))

    array_of_columns = [np.array(t) for t in vertical_platform]
    tilt(array_of_columns)
    original_platform = list(zip(*array_of_columns))
    return original_platform


file = 'day14/example.txt'
file = 'day14/input.txt'
f = open(file)
platform = f.read().strip().splitlines()

# Tilt the platform north
platform = tilt_platform(platform)

# Calculate the total load on the north support beams
total_load = calculate_load(platform)

print("part 1:", total_load)
