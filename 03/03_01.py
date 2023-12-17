import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    text_lines = file.read().splitlines()
    


def get_coordinates(text_lines) -> list:
    coordinates = []    # [char, -> Index from character in input matrix
                        #   [top_left, top, top_right,  -> Previous line left > right
                        #   left, char, right  --> current line left > right
                        #   bottom_left, bottom, bottom_right]] --> Next line
    previous_line = []
    next_line = []
    character_matrices = []
    for colIndex, text_line in enumerate(text_lines):
        line_string = None
        #Check if index is greater than 0
        if colIndex > 0:
            previous_line = text_lines[colIndex-1]
        #Check if index is smaller than length of text_lines
        if colIndex < len(text_lines)-1:
            next_line = text_lines[colIndex+1]
        if colIndex == 0:
            previous_line = None
        if colIndex == len(text_lines)-1:
            next_line = None
        # print(f"previous_line: {previous_line}")
        # print(f"text_line: {text_line}")
        # print(f"next_line: {next_line}")

        segment = [previous_line, text_line, next_line]

        for rowIndex, char in enumerate(text_line):
            character_matrix = []
            y_coord = text_lines.index(text_line)+1
            coordinate = [char, [rowIndex, y_coord]]
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
                if rowIndex == 0:
                    left_char = ""
                    bottom_left_char = ""
                    right_char = text_line[rowIndex+1]
                    bottom_right_char = next_line[rowIndex+1]
                    bottom_char = next_line[rowIndex]
                # Check if character is last character in line in first line
                elif rowIndex == len(text_line)-1:
                    left_char = text_line[rowIndex-1]
                    bottom_left_char = next_line[rowIndex-1]
                    right_char = ""
                    bottom_right_char = ""
                    bottom_char = next_line[rowIndex]
                # Check if any character in in between
                elif rowIndex > 0 and rowIndex < len(text_line)-1:
                    left_char = text_line[rowIndex-1]
                    bottom_left_char = next_line[rowIndex-1]
                    right_char = text_line[rowIndex+1]
                    bottom_right_char = next_line[rowIndex+1]
                    bottom_char = next_line[rowIndex]
            elif next_line is None:
                bottom_char = ""
                bottom_left_char = ""
                bottom_right_char = ""
                # Check if character is first character in line in last line
                if rowIndex == 0:
                    left_char = ""
                    top_left_char = ""
                    right_char = text_line[rowIndex+1]
                    top_right_char = previous_line[rowIndex+1]
                    top_char = previous_line[rowIndex]
                # Check if character is last character in line in last line
                elif rowIndex == len(text_line)-1:
                    left_char = text_line[rowIndex-1]
                    top_left_char = previous_line[rowIndex-1]
                    right_char = ""
                    top_right_char = ""
                    top_char = previous_line[rowIndex]
                elif rowIndex > 0 and rowIndex < len(text_line)-1:
                    left_char = text_line[rowIndex-1]
                    top_left_char = previous_line[rowIndex-1]
                    right_char = text_line[rowIndex+1]
                    top_right_char = previous_line[rowIndex+1]
                    top_char = previous_line[rowIndex]
            # Check if character is not in first or last line
            elif next_line and previous_line:
                bottom_char = next_line[rowIndex]
                top_char = previous_line[rowIndex]
                # Check if character is first in line
                if rowIndex == 0:
                    left_char = ""
                    top_left_char = ""
                    bottom_left_char = ""
                    right_char = text_line[rowIndex+1]
                    top_right_char = previous_line[rowIndex+1]
                    bottom_right_char = next_line[rowIndex+1]
                # Check if character is last in line
                elif rowIndex == len(text_line)-1:
                    left_char = text_line[rowIndex-1]
                    top_left_char = previous_line[rowIndex-1]
                    bottom_left_char = next_line[rowIndex-1]
                    right_char = ""
                    top_right_char = ""
                    bottom_right_char = ""
                # Check if character is in between
                elif rowIndex > 0 and rowIndex < len(text_line)-1:
                    left_char = text_line[rowIndex-1]
                    top_left_char = previous_line[rowIndex-1]
                    bottom_left_char = next_line[rowIndex-1]
                    right_char = text_line[rowIndex+1]
                    top_right_char = previous_line[rowIndex+1]
                    bottom_right_char = next_line[rowIndex+1]
            character_matrix = [char,
                              [top_left_char, top_char, top_right_char,
                               left_char, char, right_char,
                               bottom_left_char, bottom_char, bottom_right_char]]
            character_matrices.append(character_matrix)
        #return previous_line, text_line, next_line
    print(f"character_games: {character_matrices}")

    return character_matrices

def evaluate_games(character_matrices, text_lines):
    valid_numbers = []
    digit = []
    digits = []
    valid_digit = []
    valid_digits = []
    for i, character_matrix in enumerate(character_matrices):
        character = ""
        character = str(character_matrix[0]) # any -> str(any) -> num(str)
        set = character_matrix[1]
        validators = ['#', '*', '+', '$', '=', '/', '@', '-'] # TODO: Find symbols with regEx instead (don't froget to exclude \.)
        
        # Conditions
        # any of the validators in set
        # set[0] = right_char
        # set[5] = left_char
        
        # Check if character is a valid digit
        if character.isdigit() is True \
                and any(x in set for x in validators) is False:
            digit.append(character)
        elif character.isdigit() is True \
                and any(x in set for x in validators) is True:
        # Check if char is a digit and and and an invalid digit 
                    
        # Check if char is a digit, not first in line and part of a valid number
            if valid_digit:
                if character.isdigit() is True \
                        and set[5] == valid_digit[-1]:
                    valid_digit.append(character)
        # Check if char is a valid digit and part of a number
            elif digit:
                if character.isdigit() is True \
                        and set[5] == digit[-1] \
                        and any(x in set for x in validators) is True:
                    valid_digit.append(int(''.join(digit) + str(character)))
                    digit.clear()
            else:
                valid_digit.append(character)
        # Check if char terminates a number
        elif (character.isdigit() is False and \
                set[5].isdigit() is True):
            valid_digits.append(''.join(valid_digit))
            digits.append(''.join(digit))
            digit.clear()
            valid_digit.clear()
        
        # Clear lists if line is complete
        if (i+1) % 10 == 0 and i > 0 and valid_digit is not None and digit is not None:
            valid_digits.append(''.join(valid_digit))
            digits.append(digit)
            digit.clear()
            valid_digit.clear()
        #if (i+1) % 10 == 0 and i > 0 and valid_digit is not None and digit is not None:


    valid_numbers.append(valid_digits)

    print(f"valid_numbers: {valid_numbers}")

    return valid_numbers


character_matrices = (list(get_coordinates(text_lines)))
valid_numbers = evaluate_games(character_matrices, text_lines)
#print(character_games)
#evaluate_coordinates(coordinates)
#print(coordinates)


