import os as os
import re as re

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

score = 0

for line in data:
    digits = re.findall(r'(\d+)', line)
    winning_numbers = digits[1:11]
    game_numbers = digits[11:]
    duplicates = set(winning_numbers).intersection(game_numbers)
    if len(duplicates) == 1:
        score += 1
    elif len(duplicates) >= 2:
        score += 2**(len(duplicates)-1)

print(f"Score {score}")
