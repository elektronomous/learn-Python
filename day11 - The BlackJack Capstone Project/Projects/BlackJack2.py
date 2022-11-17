# HINT  -   4   -   create a del_card() function that uses the list below to return a 
#                   random card.
# 11 is the ACE.

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
    return random.choice(cards);

# HINT  -   5   -   Deal the user and computer 2 cards each using deal_card()
user_card = [];
computer_card = [];

for _ in range(2):
    user_card.append(deal_card());
    computer_card.append(deal_card());

# HINT  -   6   -   Create a function called calculate_score() that takes a List of cards
#                   as input and return the score.
# HINT  -   7   -   Inside calculate_score() check for a blackjack (ace + 10) and return 0 
#                   instead of the actual score. 0 will represent a blackjack in our game
# HINT  -   8   -   Inside calculate_score() check for an 11 (ace). If the score already over
#                   21, remove the 11 and replace it with a 1. You might need to look up over
#                   append() and remove().

def calculate_score(cards:list):
    """ Take a list of card and return int """
    total_score = sum(cards);

    if 11 in cards and total_score > 21:
        cards[cards.index(11)] = 1;
        total_score = sum(cards);

    if total_score == 21 and len(cards) == 2:
        return 0;
    
    return total_score;
# HINT  -   9   -   Call calculate_score(). If the computer or the user has a blackjack(0) or
#                   if the user's score is over21, then the gamee ends.

playing = True;

while playing:
    user_score = calculate_score(user_card);
    computer_score = calculate_score(computer_card);
    print(f"    Your cards: {user_card}, current score: {user_score}");
    print(f"    Computer's first card: {computer_card[0]}");

# HINT  -   10  -   If the game has not ended, ask the user if they want to draw another card. If
#                   yes, then use the deal_card() function to add another card to the user_cards
#                   list. If no, then the game has ended

    if not user_score or not computer_score or user_score > 21 or computer_score > 21:
        break;
    
    player_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()[0];

    if 'n' in player_decision:
        break;
    # add to the user_card
    user_card.append(deal_card());

# HINT  -   12  -   Once the user is done, it's time to let the computer play. The computer should
#                   keep drawing cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card());
    computer_score = calculate_score(computer_card);

# HINT  -   13  -   Create a function called compare() and pass in the user_score and computer_score.
#                   If the computer and user both have the same score, then it's a draw. If the computer
#                   has a blackjack(0), then the user losses. If the user has blackjack(0), then the user
#                   wins. If the user_score is over 21, then the user losses. If the computer_score is over
#                   21, then the computer loses. If none of the above, then the player with highest score
#                   wins.

def compare(score1:int, score2:int):
    if user_score == computer_score:
        print("Draw!");
    elif not user_score or user_score > computer_score:
        print("You win!");
    elif not computer_score or computer_score > user_score:
        print("You lost!");
    elif user_score > 21:
        print("You went over. you lose");



compare(user_score, computer_score);
