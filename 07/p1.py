"""Solve Day 7/Part 1 AdventOfCode."""


def get_hand_type(hands: list, bids: list) -> list:
    """Return lists of hands sorted by type."""
    fives = []
    fours = []
    full_houses = []
    triplets = []
    two_pairs = []
    pairs = []
    high_cards = []
    
    for i, hand in enumerate(hands):
        # print(list(hand))
        gameid = [i, hand, bids[i]]

        # Case 1 - Five of a kind
        if all(suit == hand[0] for suit in hand) is True:
            # print(f'Five of a kind: {gameid}')
            fives.append(gameid)
        
        # Case 2 - Four of a kind
        elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
            # print(f'Four of a kind: {gameid}')
            fours.append(gameid)

        elif len(set(hand)) >= 2:
            # Case 3 - Full House
            if len(set(hand)) == 2:
                # print(f'Full House: {gameid}')
                full_houses.append(gameid)
            # Case 4 - Three of a kind
            elif len(set(hand)) == 3 and any(hand.count(suit) == 3 for suit in hand):
                # print(f'Three of a kind: {gameid}')
                triplets.append(gameid)
            # Case 5 - Two pairs
            elif len(set(hand)) == 3 and any(hand.count(suit) == 2 for suit in hand):
                # print(f'Two pairs: {gameid}')
                two_pairs.append(gameid)
            # Case 6 - One pair
            elif len(set(hand)) == 4:
                # print(f'One pair: {gameid}')
                pairs.append(gameid)
            else:
                # print(f'High card: {gameid}')
                high_cards.append(gameid)
            # print(f'Triplet: {gameid}')
            #if len(set(hand))
        #print(set(hand))
         
    card_types = [fives, fours, full_houses, triplets, two_pairs, pairs, high_cards]
    return card_types


def rank_cards(card_types: list) -> list:
    """Function to rank the cards based on the power of the card position."""
    def calculate_suit_power(suit):
        if suit == 'T':
            return 10
        elif suit == 'J':
            return 11
        elif suit == 'Q':
            return 12
        elif suit == 'K':
            return 13
        elif suit == 'A':
            return 14
        else:
            return int(suit)
        
    fives, fours, full_houses, triplets, two_pairs, pairs, high_cards = card_types
        
    for i, cards in enumerate(card_types):
        print(cards)
        converted_suits = []
        for suit in cards[i]:
            print(suit)
            converted_suit = calculate_suit_power(suit)
            converted_suits.append(converted_suit)
        card.append(converted_suits)
            

    return card_types

def main(input):
    input = input.splitlines()
    hands = []
    bids = []
    for game in input:
        hand = game.split(' ')[0]
        bid = game.split(' ')[1]
        # print(hand)
        hands.append(hand)
        bids.append(bid)
    solution = rank_cards(get_hand_type(hands, bids))
    # print(hands, bids)
    return solution, None
