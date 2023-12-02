total_1star = 0
f = open("day2/input.txt", "r")
for line in f:
    end_index = line.find(':')
    Id = int(line[5:end_index])  #game Id
    substring = line[end_index + 1:].strip('\n')
    # recreate sets per game
    sets = substring.split(';')
    # Initialize variables to store the counts
    red_count = green_count = blue_count = 0

    possible = True
    # Loop through matches and assign values to variables
    for color in sets:
        if color.find('green') > -1:
            green_count = int(color[color.index('green') -
                                    3:color.index('green')])
        if color.find('red') > -1:
            red_count = int(color[color.index('red') - 3:color.index('red')])
        if color.find('blue') > -1:
            blue_count = int(color[color.index('blue') -
                                   3:color.index('blue')])
        if (red_count > 12 or green_count > 13 or blue_count > 14):
            possible = False

    if (possible):
        total_1star = total_1star + Id

total_2star = 0
# f = open("day2/example.txt", "r")
f = open("day2/input.txt", "r")
for line in f:
    end_index = line.find(':')
    Id = int(line[5:end_index])  #game Id
    substring = line[end_index + 1:].strip('\n')
    # recreate sets per game
    sets = substring.split(';')
    # Initialize variables to store the counts
    red_count = green_count = blue_count = 0
    min_red_count = min_green_count = min_blue_count = 0

    possible = True
    # Loop through matches and assign values to variables
    for color in sets:
        #increment min green balls
        if color.find('green') > -1:
            green_count = int(color[color.index('green') -
                                    3:color.index('green')])
            if (min_green_count < green_count):
                min_green_count = green_count
        #increment min red balls
        if color.find('red') > -1:
            red_count = int(color[color.index('red') - 3:color.index('red')])
            if (min_red_count < red_count):
                min_red_count = red_count
        #increment min blue balls
        if color.find('blue') > -1:
            blue_count = int(color[color.index('blue') -
                                   3:color.index('blue')])
            if (min_blue_count < blue_count):
                min_blue_count = blue_count

    total_2star = total_2star + (min_blue_count * min_green_count *
                                 min_red_count)

print(f"star 1: total {total_1star}")
print(f"star 2: total {total_2star}")
