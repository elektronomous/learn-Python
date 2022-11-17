import random
print('''
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
''');
# Step 2

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
 
chosen_word = random.choice(word_list);

blank_spaces = [underscore for underscore in ('_' * len(chosen_word))];
print(chosen_word);


# TODO 1 -- Create a variable called 'lives' to keep track of the number of lives left.
#           Set 'lives' to equal 6.
# TODO 2 -- If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
#           If 'lives' goes down to 0 then the game should stop and it should print "You lost."
# TODO 3 -- print the ASCII art from 'stages' that corresponds to the current number of 'lives'
#           the user has remaining.

end_of_game = False;
lives = 6;

while not end_of_game:
    guess = input("Guess a letter: ");

    if len(guess) > 1:
        guess = guess[0];

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            blank_spaces[index] = guess;
            
                
    print(blank_spaces);

    if "_" not in blank_spaces:
            end_of_game = True;
