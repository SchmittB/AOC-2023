def shoelace_and_perimeter(vertices):
    """
    Calculate the area and external perimeter of a polygon using the Shoelace Formula.

    Parameters:
    - vertices: A list of (x, y) coordinates representing the vertices of the polygon.

    Returns:
    - A tuple containing the area and perimeter of the polygon.
    """
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    # Add the first vertex at the end to complete the loop
    vertices.append(vertices[0])

    # Calculate the area using the Shoelace Formula
    area = 0
    for i in range(n):
        area += (vertices[i][0] * vertices[i + 1][1]) - (vertices[i + 1][0] *
                                                         vertices[i][1])

    # Take the absolute value and divide by 2
    area = abs(area) / 2.0

    # Calculate the external perimeter
    perimeter = 0
    for i in range(n):
        perimeter += ((vertices[i][0] - vertices[i + 1][0])**2 +
                      (vertices[i][1] - vertices[i + 1][1])**2)**0.5

    return area + perimeter // 2 + 1


def next_node(current_node, dir, lines):
    x = current_node[0]
    y = current_node[1]
    if dir == 'U':
        y = y - lines
    if dir == 'D':
        y = y + lines
    if dir == 'R':
        x = x + lines
    if dir == 'L':
        x = x - lines
    return (x, y)


def decode_hexadecimal(hex_code):
    hex_code = hex_code.strip('(#').strip(')')
    if len(hex_code) != 6 or not all(c in '0123456789abcdef'
                                     for c in hex_code):
        raise ValueError(
            "Invalid hexadecimal code. It should be six hexadecimal digits long."
        )

    distance_hex = hex_code[:-1]
    direction_hex = hex_code[-1]

    distance_dec = int(distance_hex, 16)
    direction_dec = int(direction_hex, 16)

    directions = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    direction = directions.get(direction_dec, 'Unknown')

    return distance_dec, direction


file = 'day18/example.txt'
file = 'day18/input.txt'
f = open(file, 'r', newline='')
board = f.read().strip().splitlines()
instruction = [i.split(' ') for i in board]

node = [(0, 0)]

for l in instruction:
    node.append(next_node(node[-1], l[0], int(l[1])))

sum_part1 = shoelace_and_perimeter(node)

print(sum_part1)

#part 2
node = [(0, 0)]

for l in instruction:
    length, dir = decode_hexadecimal(l[2])
    node.append(next_node(node[-1], dir, length))

sum_part2 = shoelace_and_perimeter(node)

print(sum_part2)
