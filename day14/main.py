import numpy as np


def find_pattern(values):
    n = len(values)
    longest_pattern = []
    for pattern_length in range(1, n // 2 + 1):
        for i in range(n - 2 * pattern_length + 1):
            pattern = values[i:i + pattern_length]
            if values[i:i + pattern_length] == values[i + pattern_length:i +
                                                      2 * pattern_length]:
                if len(pattern) > len(longest_pattern):
                    longest_pattern = pattern

    return longest_pattern


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


def tilt_platform(platform, direction):
    if direction == 'north':
        vertical_platform = list(zip(*platform))

        array_of_columns = [np.array(t) for t in vertical_platform]
        tilt(array_of_columns)
        platform = list(zip(*array_of_columns))
    if direction == 'south':
        vertical_platform = list(zip(*platform))

        array_of_columns = [np.array(t)[::-1] for t in vertical_platform]
        tilt(array_of_columns)
        platform = list(zip(*array_of_columns))
        platform = platform[::-1]
    if direction == 'east':
        platform = [np.array(t)[::-1] for t in platform]
        tilt(platform)
        platform = [t[::-1] for t in platform]
    if direction == 'west':
        platform = [np.array(t) for t in platform]
        tilt(platform)
    return platform


file = 'day14/example.txt'
file = 'day14/input.txt'
f = open(file)
platform = f.read().strip().splitlines()
platform2 = platform.copy()

# Tilt the platform north
direction = 'north'
platform = tilt_platform(platform, direction)

# Calculate the total load on the north support beams
total_load = calculate_load(platform)

print("part 1:", total_load)

#part 2
loads = []
for i in range(1000):
    platform2 = tilt_platform(platform2, 'north')
    platform2 = tilt_platform(platform2, 'west')
    platform2 = tilt_platform(platform2, 'south')
    platform2 = tilt_platform(platform2, 'east')
    loads.append(calculate_load(platform2))

pattern = find_pattern(loads)
print("part 2:", loads[1_000_000_000 % len(pattern) - 1])
