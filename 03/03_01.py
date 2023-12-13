import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    text_lines = file.read().splitlines()
    

def get_coordinates(text_lines):
    y_coords = []
    x_coords = []
    coordinates = []
    previous_line = []
    next_line = []
    character_games = []
    character_game = []
    for index, text_line in enumerate(text_lines):
        line_string = None
        #Check if index is greater than 0
        if index > 0:
            previous_line = text_lines[index-1]
        #Check if index is smaller than length of text_lines
        if index < len(text_lines)-1:
            next_line = text_lines[index+1]
        if index == 0:
            previous_line = None
        if index == len(text_lines)-1:
            next_line = None
        # print(f"previous_line: {previous_line}")
        # print(f"text_line: {text_line}")
        # print(f"next_line: {next_line}")

        for i, j in enumerate(text_line):
            char = j
            y_coord = text_lines.index(text_line)+1
            coordinate = [char, [i, y_coord]]
            coordinates.append(coordinate)
            # Check if character is not first character in line and not in first or last line
            if i == 0 and None not in (previous_line, next_line):
                top_char = previous_line[i]
                bottom_char = next_line[i]
                left_char = None
                top_left_char = None
                bottom_left_char = None
                right_char = text_line[i+1]
                top_right_char = previous_line[i+1]
                bottom_right_char = next_line[i+1]
            # Check is character is last in line
            elif i == len(text_line)-1 and None not in (previous_line, next_line):
                top_char = previous_line[i]
                bottom_char = next_line[i]
                left_char = text_line[i-1]
                top_left_char = previous_line[i-1]
                bottom_left_char = next_line[i-1]
                right_char = None
                top_right_char = None
                bottom_right_char = None
            # Check if character is first character in line of the first line
            elif i == 0 and previous_line is None:
                top_char = None
                bottom_char = next_line[i]
                left_char = None
                top_left_char = None
                bottom_left_char = None
                right_char = text_line[i+1]
                top_right_char = None
                bottom_right_char = next_line[i+1]
            # Check if character is last character in line of the first line
            elif i == len(text_line)-1 and previous_line is None:
                top_char = None
                bottom_char = next_line[i]
                left_char = text_line[i-1]
                top_left_char = None
                bottom_left_char = next_line[i-1]
                right_char = None
                top_right_char = None
                bottom_right_char = None
            # Check if character is first character in line of the last line
            elif i == 0 and next_line is None:
                top_char = previous_line[i]
                top_right_char = previous_line[i+1]
                right_char = text_line[i+1]
                bottom_right_char = None
                bottom_char = None
                bottom_left_char = None
            # Check if character is last character in line of the last line
            elif i == len(text_line)-1 and next_line is None:
                top_char = previous_line[i]
                top_left_char = previous_line[i-1]
                left_char = text_line[i-1]
                bottom_left_char = None
                bottom_char = None
                bottom_right_char = None
            elif i > 0 and i < len(text_line)-1 and None not in (previous_line, next_line):
                top_char = previous_line[i]
                bottom_char = next_line[i]
                left_char = text_line[i-1]
                top_left_char = previous_line[i-1]
                bottom_left_char = next_line[i-1]
                right_char = text_line[i+1]
                top_right_char = previous_line[i+1]
                bottom_right_char = next_line[i+1]
            character_game = [char,
                              [top_char, top_right_char, right_char,
                               bottom_right_char, bottom_char,
                               bottom_left_char, left_char,
                               top_left_char]]
            character_games.append(character_game)
    return coordinates, character_games

def evaluate_games(character_games):
    valid_numbers = []
    for character_game in character_games:
        character = ""
        character = str(character_game[0])
        set = character_game[1]
        #print(f"{set}")
        validators = ['.', '#', '*', '+', '$', '=', '/', '@', '-']
        if character.isdigit() == True: 
            print(f"char {character}, isdigit")
        #print(f"character: {character}, set: {set}")
            # if character == '.':
            #     print(f"dot {character}")
            # elif character in ['#', '*', '+', '$', '=', '/', '@', '-']:
            #     print(f"raute {character}")
            # elif character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            #     print(f"zahl {character}")
            # else:
            #     print(f"else {character}")
    return valid_numbers
# def evaluate_coordinates(coordinates):
#     for coordinate in coordinates:
#         print(coordinate)
            # x_coord = values['x']
            # y_coord = values['y']
            # for x, y in enumerate(char):
            #     print(f"x: {x}, y: {y}")
            
            #nextchar = coordinate{'x':x_coord+1,y_coord]
            #print(next_char)
            #print(f"char: {char} x_coord: {x_coord}, y_coord: {y_coord}")
            # print next char in line by incrementing x_coord
            
            # while char is in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and \
            #         values.get('x') == x_coord 
            # if key == '.':
            #     print(f"dot {key}")
            # elif key in ['#', '*', '+', '$', '=', '/', '@', '-']:
            #     print(f"raute {key}")
            # elif key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            #     print(f"zahl {key}")
            # else:
            #     print(f"else {key}")
    return coordinates

coordinates, character_games = (list(get_coordinates(text_lines)))
valid_numbers = evaluate_games(character_games)
#print(character_games)
#evaluate_coordinates(coordinates)
#print(coordinates)
