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
    

    converted_matches = []
    for match in matches:
        converted_matches = string_replace_dict.get(match, match)
        print(converted_matches)



        #converted_matches = string_replace_dict.get(match, match)
    #print(converted_matches)
    first_digit = 1
    last_digit = 1
    #
    return first_digit, last_digit


#    digits = re.findall(pattern, line)
#    print(digits)
        # first_digit = digits[0]
        # last_digit = digits[-1]
        #print(f'first_digit: {first_digit} - last_digit: {last_digit}')
#    calibration_value = int(first_digit + last_digit)
#    sum += calibration_value

    print(f'sum: {sum}')

print(f'sum: {sum}')
file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r',) as file:
    text_lines = file.read().splitlines()

for line in text_lines:
    first_digit, last_digit = get_first_and_last_digit(line)
    calibration_value = first_digit + last_digit
    

