import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r' ) as file:
    text_lines = file.read().splitlines()

game = {
        "red": 0,
        "blue": 0,
        "green": 0
        }

pattern = r'[\d] \w+'
for line in text_lines:
    matches = []
    matches = re.findall(pattern, line)
    cubes_per_match = []
    for match in matches:
        # Extract the color and the amount of cubes
        cube_amount, cube_color = match.split(' ')
        # cubes per match
        cubes_per_match.append({cube_color: int(cube_amount)})
        # merge duplicate keys and sum the values
    print(cubes_per_match)
     
