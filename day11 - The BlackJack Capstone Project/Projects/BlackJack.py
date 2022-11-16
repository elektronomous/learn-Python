import random
import os
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
suit_symbols = ['♠', '♦', '♥', '♣'];
# The cards in the list have equal probability of being drawn.
# Cards are not remove from the deck as they are drawn.
# The computer is the dealer.

close_card = """┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘"""
open_card = """┌──────────┐
│{}       │
│          │
│          │
│    {}    │
│          │
│          │
│       {}│
└──────────┘""";

def get_card_symbol(index:int):
    suit_symbol_cards = {
        0: "A",
        10: "J",
        11: "Q",
        12: "K"
    };

    if index in suit_symbol_cards:
        return suit_symbol_cards[index];
    else:
        return f"{cards[index]}";

def draw_card(card:dict, computer_card:bool = False):
    card_picture = "";
    result_card = [];
    for n in range(len(card)):
        
        if computer_card:
            result_card.append(close_card.split("\n"));
            computer_card = False;
        else:
            [index,suit] = card[n];
            result_card.append(open_card.format(''.join([f"{get_card_symbol(index)}{suit}"]).ljust(3),
            suit.ljust(2), 
            ''.join([f"{get_card_symbol(index)}{suit}"]).ljust(3)).split("\n"));

    for n in range(len(result_card[0])):
        for i in range(len(result_card)):
            card_picture += result_card[i][n] + " ";
        card_picture += "\n";
    
    print(card_picture);

def count_score(card:dict):
    total = 0;
    for n in range(len(card)):
        [index,suit] = card[n];

        if not index:           # if the card was ACE
            if (total + index) < 21:
                total += cards[index];
            else:
                total += 1;
        elif index > 9:           # if the card was JACK or QUEEN or KING
            total += 10;
        else:
            total += cards[index];
    return total;




playing = user_decision = computer_decision = True;

while playing:
    user_score = computer_score = 0;

    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()[0];
    
    if wanna_play[0] == 'n':
        break;

    user_card = {};
    computer_card = {};

    # USER
    # generate two index random numbers for cards
    user_index_card = [random.randint(0,len(cards)-1), random.randint(0,len(cards)-1)];
    # generate two index random numbers for suit_symbols
    user_index_suit = [random.randint(0,len(suit_symbols)-1),random.randint(0,len(suit_symbols)-1)];

    print(user_index_card);

    # COMPUTER
    # generate two index random numbers for cards
    computer_index_card = [random.randint(0,len(cards)-1), random.randint(0,len(cards)-1)];
    # generate two index random numbers for suit_symbols
    computer_index_suit = [random.randint(0,len(suit_symbols)-1),random.randint(0,len(suit_symbols)-1)];

    # initialize the user_card & computer_card
    for n in range(len(user_index_card)):
        user_card[n] = [user_index_card[n], suit_symbols[user_index_suit[n]]];
        computer_card[n] = [computer_index_card[n], suit_symbols[user_index_suit[n]]];
    
    # draw the card
    print("Your card: ");
    draw_card(user_card);
    # and show the score
    print(f"Current Score: {count_score(user_card)}");

    # draw the card
    print("Computer card: ");
    draw_card(computer_card, True);
    # print(f"Current Score: {count_score(computer_card)}");
    

    while user_decision:
        player_choice = input("Type (H)it to take another card\nType (S)tand to stop\n").upper()[0];

        if player_choice == 'H':
            # add card to user_card
            n += 1;
            user_card[n] = [random.randint(0,len(cards)-1), suit_symbols[random.randint(0,len(suit_symbols)-1)]];


            # clear the screen first
            # os.system('clear');
            # print("Your card: ");
            # draw_card(user_card);
            # print("Computer Card: ");
            # draw_card(computer_card);

            print(user_card);
            draw_card(user_card);
        else:
            break;
             




