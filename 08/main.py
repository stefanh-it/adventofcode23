import sys
import os
import p1
import p2

if sys.argv[1] == '1' and sys.argv[2] == 'test':
    file_path = os.path.join(os.path.dirname(__file__), 'test.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        test_data = f.read()
        solution = p1.main(test_data)
        print(f" Part1 Test Solution: {solution}")
if sys.argv[1] == '1' and sys.argv[2] == 'input':
    file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        input_data = f.read()
        solution = p1.main(input_data)
        print(f" Part1 Solution: {solution}")

if sys.argv[1] == '2' and sys.argv[2] == 'test':
    file_path = os.path.join(os.path.dirname(__file__), 'test.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        test_data = f.read()
        solution = p2.main(test_data)
        print(f" Part2 Test Solution: {solution}")
if sys.argv[1] == '2' and sys.argv[2] == 'input':
    file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        input_data = f.read()
        solution = p2.main(input_data)
        print(f" Part1 Solution: {solution}")
