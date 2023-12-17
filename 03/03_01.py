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
            character_game = []
            char = j
            y_coord = text_lines.index(text_line)+1
            coordinate = [char, [i, y_coord]]
            coordinates.append(coordinate)
            top_char = ""
            top_right_char = ""
            top_left_char = ""
            bottom_char = ""
            bottom_right_char = ""
            bottom_left_char = ""
            left_char = ""
            right_char = ""
            # Check if character is in first line
            if previous_line is None:
                top_char = ""
                top_right_char = ""
                top_left_char = ""
                # Check if character is first character in line in first line
                if i == 0:
                    left_char = ""
                    bottom_left_char = ""
                    right_char = text_line[i+1]
                    bottom_right_char = next_line[i+1]
                    bottom_char = next_line[i]
                # Check if character is last character in line in first line
                elif i == len(text_line)-1:
                    left_char = text_line[i-1]
                    bottom_left_char = next_line[i-1]
                    right_char = ""
                    bottom_right_char = ""
                    bottom_char = next_line[i]
                # Check if any character in in between
                elif i > 0 and i < len(text_line)-1:
                    left_char = text_line[i-1]
                    bottom_left_char = next_line[i-1]
                    right_char = text_line[i+1]
                    bottom_right_char = next_line[i+1]
                    bottom_char = next_line[i]
            elif next_line is None:
                bottom_char = ""
                bottom_left_char = ""
                bottom_right_char = ""
                # Check if character is first character in line in last line
                if i == 0:
                    left_char = ""
                    top_left_char = ""
                    right_char = text_line[i+1]
                    top_right_char = previous_line[i+1]
                    top_char = previous_line[i]
                # Check if character is last character in line in last line
                elif i == len(text_line)-1:
                    left_char = text_line[i-1]
                    top_left_char = previous_line[i-1]
                    right_char = ""
                    top_right_char = ""
                    top_char = previous_line[i]
                elif i > 0 and i < len(text_line)-1:
                    left_char = text_line[i-1]
                    top_left_char = previous_line[i-1]
                    right_char = text_line[i+1]
                    top_right_char = previous_line[i+1]
                    top_char = previous_line[i]
            # Check if character is not in first or last line
            elif next_line and previous_line:
                bottom_char = next_line[i]
                top_char = previous_line[i]
                # Check if character is first in line
                if i == 0:
                    left_char = ""
                    top_left_char = ""
                    bottom_left_char = ""
                    right_char = text_line[i+1]
                    top_right_char = previous_line[i+1]
                    bottom_right_char = next_line[i+1]
                # Check if character is last in line
                elif i == len(text_line)-1:
                    left_char = text_line[i-1]
                    top_left_char = previous_line[i-1]
                    bottom_left_char = next_line[i-1]
                    right_char = ""
                    top_right_char = ""
                    bottom_right_char = ""
                # Check if character is in between
                elif i > 0 and i < len(text_line)-1:
                    left_char = text_line[i-1]
                    top_left_char = previous_line[i-1]
                    bottom_left_char = next_line[i-1]
                    right_char = text_line[i+1]
                    top_right_char = previous_line[i+1]
                    bottom_right_char = next_line[i+1]
            character_game = [char,
                              [right_char, top_right_char, bottom_right_char,
                               bottom_char, bottom_left_char, left_char,
                               top_left_char, top_char]]
            character_games.append(character_game)
        #return previous_line, text_line, next_line
    print(f"character_games: {character_games}")

    return coordinates, character_games

def evaluate_games(character_games, text_lines):
    valid_numbers = []
    digit = []
    digits = []
    valid_digit = []
    valid_digits = []
    for i, character_game in enumerate(character_games):
        character = ""
        character = str(character_game[0])
        set = character_game[1]
        validators = ['#', '\*', '+', '$', '=', '/', '@', '-']
        
        # Conditions
        # any of the validators in set
        # set[0] = right_char
        # set[5] = left_char
        
        # Check if character is a digit
        if character.isdigit() is True \
                and any(x in set for x in validators) is False:
            digit.append(character)
        # Check if char is a digit and and a valid digit 
            if character.isdigit() is True \
                    and any(x in set for x in validators) is True:
                valid_digit.append(character)
            # Check if char is a digit, not first in line and part of a valid number
            if valid_digit:
                if character.isdigit() is True \
                        and (i % 10 != 0) \
                        and set[5] == valid_digit[-1]:
                    valid_digit.append(character)
            # Check if  char is a valid digit and part of a number
            if digit:
                if character.isdigit() is True \
                        and set[5] == digit[-1] \
                        and any(x in set for x in validators) is True:
                    digit.append(character)
                    valid_digit.append(digit)
            # Check if char terminates a number
        if character.isdigit() is False and \
                set[5].isdigit() is True:
            valid_digits.append(valid_digit)
            digits.append(digit)
            digit.clear()
            valid_digit.clear()

        if (i+1) % 10 == 0 and i > 0 and valid_digit is not None and digit is not None:
            valid_digits.append(valid_digit)
            digits.append(digit)
            digit.clear()
            valid_digit.clear()

    valid_numbers.append(valid_digits)
            # #elif character.isdigit() is False and i+1 > 1\
            #         and (set[1] == next(reversed(valid_numbers)) \
            #         or set[1] == next(reversed(numbers))):
            #     valid_numbers.append(valid_number)


            # Check if previous char set[5] is the last value character_games[i-1].character_game[0]
            # if set[5] == character_games[i-1][0] and character.isdigit() is True:
            #     current_valid_number = current_valid_number + str(character)
            #     print(current_valid_number)
            #     break
            #elif character.isdigit() is True and set[5].isdigit() is True
    print(f"valid_numbers: {valid_numbers}")
                # print(f"{text_line}")
        # match_count = 0
        # numbers_in_line = []
        # for match in re.finditer(r'\d+', text_line):
        #     print(f"match: {match}")
        #     if match is None:
        #         numbers_in_line = []
        #     else:
        #         numbers_in_line.append(match)
        #         number_start_position = match.start()
        #         number_end_position = match.end()
            #print(f"{set}")
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
valid_numbers = evaluate_games(character_games, text_lines)
#print(character_games)
#evaluate_coordinates(coordinates)
#print(coordinates)


### Old 

#"""             # Check if character is not first character in line and not in first or last line
#            if i == 0 and None not in (previous_line, next_line):
#                top_char = previous_line[i]
#                bottom_char = next_line[i]
#                left_char = ""
#                top_left_char = ""
#                bottom_left_char = "" 
#                right_char = text_line[i+1]
#                top_right_char = previous_line[i+1]
#                bottom_right_char = next_line[i+1]
#                print(char)
#            # Check is character is last in line
#            elif i == len(text_line)-1 not in (previous_line, next_line):
#                top_char = previous_line[i]
#                bottom_char = next_line[i]
#                left_char = text_line[i-1]
#                top_left_char = previous_line[i-1]
#                bottom_left_char = next_line[i-1]
#                right_char = ""
#                top_right_char = ""
#                bottom_right_char = ""
#            # Check if character is first character in line of the first line
#            elif i == 0 and previous_line is None:
#                top_char = ""
#                bottom_char = next_line[i]
#                left_char = ""
#                top_left_char = ""
#                bottom_left_char = ""
#                right_char = text_line[i+1]
#                top_right_char = ""
#                bottom_right_char = next_line[i+1]
#            # Check if character is last character in line of the first line
#            elif i == len(text_line)-1 and previous_line is None:
#                top_char = ""
#                bottom_char = next_line[i]
#                left_char = text_line[i-1]
#                top_left_char = ""
#                bottom_left_char = next_line[i-1]
#                right_char = ""
#                top_right_char = ""
#                bottom_right_char = ""
#            # Check if character is first character in line of the last line
#            elif i == 0 and next_line is None:
#                top_char = previous_line[i]
#                top_right_char = previous_line[i+1]
#                right_char = text_line[i+1]
#                bottom_right_char = ""
#                bottom_char = ""
#                bottom_left_char = ""
#            # Check if character is last character in line of the last line
#            elif i == len(text_line)-1 and next_line is None:
#                top_char = previous_line[i]
#                top_left_char = previous_line[i-1]
#                left_char = text_line[i-1]
#                bottom_left_char = ""
#                bottom_char = ""
#                bottom_right_char = ""
#            elif i > 0 and i < len(text_line)-1 and None not in (previous_line, next_line):
#                top_char = previous_line[i]
#                bottom_char = next_line[i]
#                left_char = text_line[i-1]
#                top_left_char = previous_line[i-1]
#                bottom_left_char = next_line[i-1]
#                right_char = text_line[i+1]
#                top_right_char = previous_line[i+1]
#                bottom_right_char = next_line[i+1] 
#                """
#