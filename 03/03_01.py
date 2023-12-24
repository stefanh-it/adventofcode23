import os
import re
from itertools import zip_longest

file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    text_lines = file.read().splitlines()
    
# symbols = {}
# for char in file.read():
#    if char

def get_coordinates(text_lines) -> list:
    coordinates = []    # [char, -> Index from character in input matrix
                        #   [top_left, top, top_right,  -> Previous line left > right
                        #   left, char, right  --> current line left > right
                        #   bottom_left, bottom, bottom_right]] --> Next line
    previous_line = []
    next_line = []
    matrices = []
    for rowIndex, text_line in enumerate(text_lines):
        line_string = None
        #Check if index is greater than 0
        if rowIndex > 0:
            previous_line = text_lines[rowIndex-1]
        #Check if index is smaller than length of text_lines
        if rowIndex < len(text_lines)-1:
            next_line = text_lines[rowIndex+1]
        if rowIndex == 0:
            previous_line = None
        if rowIndex == len(text_lines)-1:
            next_line = None

        for colIndex, char in enumerate(text_line):
            matrix = []
            y_coord = text_lines.index(text_line)+1
            coordinate = [char, [colIndex, y_coord]]
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
                if colIndex == 0:
                    left_char = ""
                    bottom_left_char = ""
                    right_char = text_line[colIndex+1]
                    bottom_right_char = next_line[colIndex+1]
                    bottom_char = next_line[colIndex]
                # Check if character is last character in line in first line
                elif colIndex == len(text_line)-1:
                    left_char = text_line[colIndex-1]
                    bottom_left_char = next_line[colIndex-1]
                    right_char = ""
                    bottom_right_char = ""
                    bottom_char = next_line[colIndex]
                # Check if any character in in between
                elif colIndex > 0 and colIndex < len(text_line)-1:
                    left_char = text_line[colIndex-1]
                    bottom_left_char = next_line[colIndex-1]
                    right_char = text_line[colIndex+1]
                    bottom_right_char = next_line[colIndex+1]
                    bottom_char = next_line[colIndex]
            elif next_line is None:
                bottom_char = ""
                bottom_left_char = ""
                bottom_right_char = ""
                # Check if character is first character in line in last line
                if colIndex == 0:
                    left_char = ""
                    top_left_char = ""
                    right_char = text_line[colIndex+1]
                    top_right_char = previous_line[colIndex+1]
                    top_char = previous_line[colIndex]
                # Check if character is last character in line in last line
                elif colIndex == len(text_line)-1:
                    left_char = text_line[colIndex-1]
                    top_left_char = previous_line[colIndex-1]
                    right_char = ""
                    top_right_char = ""
                    top_char = previous_line[colIndex]
                elif colIndex > 0 and colIndex < len(text_line)-1:
                    left_char = text_line[colIndex-1]
                    top_left_char = previous_line[colIndex-1]
                    right_char = text_line[colIndex+1]
                    top_right_char = previous_line[colIndex+1]
                    top_char = previous_line[colIndex]
            # Check if character is not in first or last line
            elif next_line and previous_line:
                bottom_char = next_line[colIndex]
                top_char = previous_line[colIndex]
                # Check if character is first in line
                if colIndex == 0:
                    left_char = ""
                    top_left_char = ""
                    bottom_left_char = ""
                    right_char = text_line[colIndex+1]
                    top_right_char = previous_line[colIndex+1]
                    bottom_right_char = next_line[colIndex+1]
                # Check if character is last in line
                elif colIndex == len(text_line)-1:
                    left_char = text_line[colIndex-1]
                    top_left_char = previous_line[colIndex-1]
                    bottom_left_char = next_line[colIndex-1]
                    right_char = ""
                    top_right_char = ""
                    bottom_right_char = ""
                # Check if character is in between
                elif colIndex > 0 and colIndex < len(text_line)-1:
                    left_char = text_line[colIndex-1]
                    top_left_char = previous_line[colIndex-1]
                    bottom_left_char = next_line[colIndex-1]
                    right_char = text_line[colIndex+1]
                    top_right_char = previous_line[colIndex+1]
                    bottom_right_char = next_line[colIndex+1]
            matrix = [char,
                              [top_left_char, top_char, top_right_char,
                               left_char, char, right_char,
                               bottom_left_char, bottom_char, bottom_right_char],
                               (rowIndex, colIndex)]
            matrices.append(matrix)
        #return previous_line, text_line, next_line
    #print(f"Matrices: {matrices}")

    return matrices

def evaluate_games(matrices):
    buffer = [] # num<n>[] Digit Buffer that stores the number until the check is complete
    digits = [] # num<1-3>[] Collected digits that are validated
    numbers = [] # num<1-3>[] Pieced together 

    for _, matrix in enumerate(matrices):
        character = str(matrix[0])
        set = matrix[1]
        validators = ['#', '*', '+', '$', '=', '/', '@', '-', '&'] # TODO: Find symbols with regEx instead (don't froget to exclude \.)
        
        # Validate `character`
        # - 
        if character.isdigit():  
            if len(digits) > 0:
                digits.append(character)
            else:
                buffer.append(character) # Add digits to buffer
                 # Check if Any of the chars around are valid
                if buffer and (any(x in set for x in validators) is True):
                    digits.extend(buffer) # Write buffer into valids
                    buffer.clear()
        elif digits: 
            numbers.append(int("".join(digits)))
            digits.clear()
        else:
            buffer.clear()
        
            
    #print(f"Valid Number: {numbers}")
    return numbers
# .....482
# ....+...
def evaluate_gear_ratios (matrices, text_lines):
    gear_ratios = []
    # Length of a line TODO: Change when required

    maxcolumns = 140

    for rowIndex, text_line in enumerate(text_lines):
        #Check if index is greater than 0
        if rowIndex > 0:
            previous_line = text_lines[rowIndex-1]
        #Check if index is smaller than length of text_lines
        if rowIndex < len(text_lines)-1:
            next_line = text_lines[rowIndex+1]
        if rowIndex == 0:
            previous_line = None
        if rowIndex == len(text_lines)-1:
            next_line = None

        gears = re.finditer(r'\*', str(text_line))
        # Filter out empty gears / invalid lines
        # Generator Expression
        gen_gears = (gear for gear in gears if bool(gears))
        for gear in gen_gears:

            digits_previous = re.finditer(r'(\d+)', str(previous_line))
            digits_line = re.finditer(r'(\d+)', str(text_line))
            digits_next = re.finditer(r'(\d+)', str(next_line))
            gear_colIndex = gear.start()
            # print(f"gear_colIndex {gear_colIndex}")
            # Calculate matrix from the entire list with index from matrix 
            gear_matrix = matrices[(rowIndex*maxcolumns)+(gear_colIndex)]
            gear_matrix_set = gear_matrix[1]
            gear_matrix_coords = gear_matrix[2]

            # Upper Row: Match of digits_previous may be in range of 
            # starting or ending at colIndex -1,
            # starting or ending at colIndex,
            # starting or ending at colIndex +1 or ending at colIndex-1
            # Check if set[0:2] and within the range of a match in digits_previous
            # Only do this if the buffer is no longer than 2


            buffer = []
            for digit in digits_previous:
                # Check if the digit is across all positions above
                if gear_colIndex in range(digit.start(), digit.end()): #and \
                    # gear_colIndex-1 in range(digit.span()) and \
                    # gear_colIndex+1 in range(digit.span()):
                    buffer.append(digit.group())
                elif gear_colIndex-1 == digit.end()-1:
                    buffer.append(digit.group())
                elif gear_colIndex+1 == digit.start():
                    buffer.append(digit.group())
            for digit in digits_line:
                if gear_colIndex == digit.end():
                    buffer.append(digit.group())
                    # print(digit.group())
                if gear_colIndex+1 == digit.start():
                    # print(digit.group())
                    buffer.append(digit.group())
            for digit in digits_next:
                if gear_colIndex in range(digit.start(), digit.end()):
                    buffer.append(digit.group())
                elif gear_colIndex-1 == digit.end()-1:
                    buffer.append(digit.group())
                elif gear_colIndex+1 == digit.start():
                    buffer.append(digit.group())
            # print(f"buffer {buffer}")
            if len(buffer) == 2:
                gear_ratios.append(int(buffer[0]) * int(buffer[1]))
    return gear_ratios


matrices = (list(get_coordinates(text_lines)))
solution1 = sum(evaluate_games(matrices))
print(solution1)
solution2 = sum(evaluate_gear_ratios(matrices, text_lines))
print(solution2)
