import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r' ) as file:
    text_lines = file.read().splitlines()
cubesets = []
cubes = []
game = []
games = []

for text_line in text_lines:
    #print(text_line)
    cubesets = text_line.split(';')
    #print(cubesets)
    game_data = []
    for cubeset in cubesets:
        #print(cubeset)
        cubeset_data = {}
        pairs = re.findall(r'(\d+) (red|green|blue)', cubeset)
        for number, color in pairs:
            cubeset_data[color] = int(number)
        game_data.append(cubeset_data)
    games.append(game_data)
    
#print(f"{games}")
def evaluate_game(game):
    red_cubes = []
    blue_cubes = []
    green_cubes = []

    for cubeset in game:
        if "red" in cubeset:
            red_cubes.append(cubeset["red"])
        if "green" in cubeset:
            green_cubes.append(cubeset["green"])
        if "blue" in cubeset:
            blue_cubes.append(cubeset["blue"])
    return red_cubes, green_cubes, blue_cubes

failed_game_index = []
successful_game_index = []
total_sum = 0

# Search for the lowest number of cubes in each color and check if it is 1
def evaluate_lowest_cubes(red_cubes, green_cubes, blue_cubes):
    if len(red_cubes) == 1:
        min_red_cubes = red_cubes[0]
    else:
        min_red_cubes = max(red_cubes)
    if len(green_cubes) == 1:
        min_green_cubes = green_cubes[0]
    else:
        min_green_cubes = max(green_cubes)
    if len(blue_cubes) == 1:
        min_blue_cubes = blue_cubes[0]
    else:
        min_blue_cubes = max(blue_cubes)
    return min_red_cubes, min_green_cubes, min_blue_cubes


for game in games:
    product = 0
    red_cubes, green_cubes, blue_cubes = evaluate_game(game)
    print(f"Red: {red_cubes}, Green: {green_cubes}, Blue: {blue_cubes}")
    min_red_cubes, min_green_cubes, min_blue_cubes = evaluate_lowest_cubes(red_cubes, green_cubes, blue_cubes)
    print(f"Min Red: {min_red_cubes}, Min Green: {min_green_cubes}, Min Blue: {min_blue_cubes}")

    product = min_red_cubes * min_blue_cubes * min_green_cubes
    total_sum += product

print(total_sum)
