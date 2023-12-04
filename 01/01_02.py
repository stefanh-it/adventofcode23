import os
import re

def get_first_and_last_digit(line):
    string_replace_dict = {
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

    # Iterate over each line
    pattern = r'(?=(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d))'
    matches = re.findall(pattern, line)

    digits = []
    for match_tuple in matches:
        match = next(item for item in match_tuple if item)
        digit = string_replace_dict.get(match, match)
        digits.append(digit)
    first_digit = digits[0]
    last_digit = digits[-1]

    return first_digit, last_digit


file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(file_path, 'r',) as file:
    text_lines = file.read().splitlines()

total_sum = 0
for line in text_lines:
    first_digit, last_digit = get_first_and_last_digit(line)
    calibration_value = int(first_digit + last_digit)
    total_sum += calibration_value

print(f'sum = {total_sum}')
