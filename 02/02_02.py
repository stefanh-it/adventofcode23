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

for game in games:
    product = 0
    red_cubes, green_cubes, blue_cubes = evaluate_game(game)
    if any (type(i) is not list for i in evaluate_game(game)):
        i 
    # Try if return of cubes is a list or integer, return either int or min

    #product = lowest_red_cubes * lowest_blue_cubes * lowest_green_cubes
    #print(product)

print(total_sum)
