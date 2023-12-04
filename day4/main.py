import re
from collections import defaultdict

original_scratchcard = defaultdict(int)
copy_scartchcard = defaultdict(int)

total_1star = 0
# board = list(open('day4/example.txt'))
board = list(open('day4/input.txt'))
for line in board:
    end_index = line.find(':')
    Id = int(line[5:end_index])  #game Id

    substring = line[end_index + 2:].strip('\n')
    array = substring.split('|')
    winning_numbers = set(re.findall(r'\d+', array[0]))
    my_numbers = set(re.findall(r'\d+', array[1]))
    my_winning_numbers = my_numbers & winning_numbers
    len_winning = len(my_winning_numbers)
    if (my_winning_numbers):
        total_1star = total_1star + 2**(len_winning - 1)

    # part 2
    original_scratchcard[Id] = 1
    for i in range(1, len_winning + 1):
        copy_scartchcard[Id + i] = copy_scartchcard[
            Id + i] + 1 + copy_scartchcard[Id]  # add number of original + copy

total_2star = sum(original_scratchcard.values()) + sum(
    copy_scartchcard.values())

print(f"star 1: total {total_1star}")
print(f"star 2: total {total_2star}")
