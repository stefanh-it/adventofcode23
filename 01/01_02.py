import os
import re
import sys

# Open input file


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
    print(f"Matches are {matches}")
    
    digits = []
    for match_tuple in matches:
        match = next(item for item in match_tuple if item)
        digit = string_replace_dict.get(match, match)
        digits.append(digit)
    print(f"{digits}")
    first_digit = digits[0]
    last_digit = digits[-1]

    #print(f'first_digit: {first_digit} - last_digit: {last_digit}')
    return first_digit, last_digit


#    digits = re.findall(pattern, line)
#    print(digits)
        # first_digit = digits[0]
        # last_digit = digits[-1]
        #print(f'first_digit: {first_digit} - last_digit: {last_digit}')

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(file_path, 'r',) as file:
    text_lines = file.read().splitlines()

total_sum = 0
for line in text_lines:
    first_digit, last_digit = get_first_and_last_digit(line)
    print(f'first_digit: {first_digit} - last_digit: {last_digit}')
    calibration_value = int(first_digit + last_digit)
    print(f'calibration_value: {calibration_value}')
    print(type(calibration_value))
    total_sum += calibration_value
    

print(f'sum = {total_sum}')
