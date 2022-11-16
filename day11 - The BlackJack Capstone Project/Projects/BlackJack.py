import random
#################### Blackjack Project ####################
# Difficulty Normal 😃: Use all hints below to complete the project.
# Difficulty Hard 😅: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😢: Only use Hints 1 & 2 to complete the project.

################ Our Blackjack House Rules ################
# The deck is unlimited in size
# There are no Jokers
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
suits_symbols = ['♠', '♦', '♥', '♣'];
# The cards in the list have equal probability of being drawn.
# Cards are not remove from the deck as they are drawn.
# The computer is the dealer.

close_card = [
    '┌─────────┐', 
    '│░░░░░░░░░│', 
    '│░░░░░░░░░│', 
    '│░░░░░░░░░│', 
    '│░░░░░░░░░│', 
    '│░░░░░░░░░│', 
    '│░░░░░░░░░│', 
    '│░░░░░░░░░│', 
    '└─────────┘'
];

card = """
┌──────────┐
│{}       │
│          │
│          │
│    {}    │
│          │
│          │
│       {}│
└──────────┘
""";

playing = True;

while playing:
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower();
    
    if wanna_play[0] == 'n':
        break;
    
    user_card = {
        # symbol
        suits_symbols[int(random.random() * len(suits_symbols))]:
             # index to card
             int(random.random() * len(cards)),
        # symbol
        suits_symbols[int(random.random() * len(suits_symbols))]:
             # index to card
             int(random.random() * len(cards)),
    
    }
    
    user_card_1 = ''.join([card.f])    


