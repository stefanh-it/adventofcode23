import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'input_ari.txt')
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

for game in games:
    red_cubes, green_cubes, blue_cubes = evaluate_game(game)
    if max(red_cubes) > 12 or max(green_cubes) > 13 or max(blue_cubes) > 14:
        #print("Invalid game")
        failed_game_index.append(games.index(game)+1)
    else:
        #print("Valid game")
        successful_game_index.append(games.index(game)+1)

print(f"failed game index: {failed_game_index}")
print(f"successful game index: {successful_game_index}")
print(sum(successful_game_index))



    
    #print(f"Red: {red_cubes}, Green: {green_cubes}, Blue: {blue_cubes}")

    # if "red" in game:
    #     red_cubes += game.get("red")
    # if "Green" in game:
    #     green_cubes += game["Green"]
    # if "Blue" in game:
    #     blue_cubes += game["Blue"]
    # print(f"Red: {red_cubes}, Green: {green_cubes}, Blue: {blue_cubes}")


        # add cubes to game as a nested dict within cubeset
        #game[cubeset] = cubes
#print(game)


# game = {
#         "red": 0,
#         "blue": 0,
#         "green": 0
#         }

# cubesets = []
# def extract_sets(cubesets):
#     game_sets = {}
#     for cubeset in cubesets:
#         game_sets = re.findall(r'(\d+) (red|green|red)', cubeset)
#         print(game_sets)
#
# for line in text_lines:
#     splitted_lines = line.split(';')
#     cubesets.append(splitted_lines)
#     extract_sets(cubesets)
#
# print(cubesets)




# pattern = r'[\d] '
# for line in text_lines:
#     matches = []
#     matches = re.findall(pattern, line)
#     cubes_per_match = []
#     for match in matches:
#         # Extract the color and the amount of cubes
#         cube_amount, cube_color = match.split(' ')
#         # cubes per match
#         cubes_per_match.append({cube_color: int(cube_amount)})
#         # merge duplicate keys and sum the values
#     print(cubes_per_match)
     
