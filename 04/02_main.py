import os
import re
import sys

file_path = os.path.join(os.path.dirname(__file__), 'input_small.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    cards = f.read().splitlines()

card_scores = []
def get_score(card):

    digits = re.findall(r'(\d+)', card)
    # winning_numbers = digits[1:11]
    # game_numbers = digits[11:]

    winning_numbers = digits[1:6]
    game_numbers = digits[6:]
    # print(winning_numbers, game_numbers)
    score = 0

    duplicates = set(winning_numbers).intersection(game_numbers)
    if len(duplicates) == 1:
        score = 1
        return card_score, duplicates
    if len(duplicates) >= 2:
        score = 2**(len(duplicates)-1)
        return score, duplicates
    return None, None

for card in cards:
    card_score = 0
    card_score, card_duplicates = get_score(card)
    card_scores.append(card_score)
    card_number = cards.index(card)+1
    print(f" Card No: {card_number}, duplicates: {card_duplicates}, card_score: {card_score}")
    if card_duplicates:
        print(range(len(card_duplicates)))
        for i in range(len(card_duplicates)):
            card_scores.append(get_score(cards[card_number+i]))
    # amount of duplicates
    # if card_score > 0:
    #     for i in len(card_duplicates):
    #         card_scores.append(get_score(cards[card_number+i+1]))
    print(card_scores)

#print(sum(card_scores))

# print(f"Score {card_scores}")

