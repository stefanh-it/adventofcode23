import os
import re


file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r',) as file:
    text_lines = file.read().splitlines()

    pattern = r'([1-9])'
    digits = re.findall(pattern, text_lines)
    print(digits)
    first_digit = digits[0]
    last_digit = digits[-1]
    print(f'first_digit: {first_digit} - last_digit: {last_digit}')
    calibration_value = int(first_digit + last_digit)
    sum += calibration_value

print (f'sum: {sum}')
