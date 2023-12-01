def replace_words_with_numbers(input_string):
    replacements = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for word, number in replacements.items():
        input_string = input_string.replace(word, word + number + word)

    return input_string


def get_first_and_last_number(input_string):
    input_string = replace_words_with_numbers(input_string)
    # Use regular expression to find all numbers in the string
    numbers = [s for s in [*input_string] if s.isdigit()]

    # Retrieve the first and last numbers
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number


total = 0
f = open("day1/input.txt", "r")
i = 0
for line in f:
    first, last = get_first_and_last_number(line)
    total = total + int(first + last)
    i += 1
# print(i)
print(total)
