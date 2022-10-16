import random

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

hangman = [HANGMANPICS[n] for n in range(len(HANGMANPICS)-1,-1,-1)];
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
      ''')

# Step 1

#Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# TODO - 1 - Randombly choose a word from the word_list and assign it
#            to a variable called chosen_word.
# TODO - 2 - Ask the user to guess a letter and assign their asnwer to
#            a variable called guess. Make guess lowercase
# TODO - 3 - Check if the letter the user guessed(guess) is one of the
#            letters in the chosen_word.

chosen_word = random.choice(word_list);
print(chosen_word);
    
# Step 2

# TODO - 1 - Create an empty List called display. For each letter in the
#            chosen_word, add a "_" to 'display'. So if the chosen_word
#            was "Apple", 'display' should be ["_","_","_","_","_"] with 5
#            "_" representing each letter to guess.
# TODO - 2 - Loop through each position in the chosen_word; if the letter at
#            that position matches 'guess' then reveal the letter in the 'display'
#            at that position. e.g. if the user guess "p" and the chosen word was
#            "Apple", the display should be ["_","p","p","_","_"].
# TODO - 3 - Print 'display' and you should see the guessed letter in the correct position
#            every other letter replace with "_".

# Step 3

# TODO - 1 - Use a while loop to let the user guess again. The loop should only stop once
#            the user has guessed all the letters in the chosen_word and 'display' has no more
#            blanks. then you can tell the user they've won.


display = ["_"] * len(chosen_word);
print(display);
guessing = True;
lives = 6;

while guessing:
    guess = input("Guess the word: ");
    if not guess:
        guessing = False;

    
    if guess in display:
        print("You've already guess the letter");  
    elif guess in chosen_word:    
        for n in range(len(chosen_word)):
            if guess == chosen_word[n]:
                display[n] = guess;
                print(''.join(display));
    else:
        print(hangman[lives]);
        lives -= 1;
    
    if lives < 0:
        print("You lost!");
        guessing = False;
    elif "_" not in display:
        print("You Win!");
        guessing = False; 
