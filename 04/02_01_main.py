import os
import re
import sys

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    cards = f.read().splitlines()

def matches(line):
    _, line = line.split(':')
    lhs, rhs = line.split('|')
    return len(set(lhs.split()) & set(rhs.split()))


score_1 = 0

cards_amount = [1]*len(cards)

for c, card in enumerate(cards):
    num_matches = matches(card)
    score_1 += int(2**(num_matches-1))
    #print(cards_amount)
    for i in range(num_matches):
        print(i)
        cards_amount[c+1+i] += cards_amount[c]

print(score_1)

print(sum(cards_amount))


