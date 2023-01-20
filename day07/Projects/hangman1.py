from random import *
# Step 1
word_list = ["advark", "baboon", "camel"];


# TODO 1 -- Randomly choose a word from the word_list and assign it to a variable
#           called chosen_word.
# TODO 2 -- Ask the user to guess a letter and assign their answer to a variable caleed guess.
#           Make guess lowercase
# TODO 3 -- Check if the letter the user guesses(guess) is one of the letter in the chosen_word.

#chosen_word = word_list[randint(0, len(word_list)-1)];
chosen_word = choice(word_list);

answered_word = '_' * len(chosen_word);

while True:
    print(answered_word);
    
    letterGuess = input("Guess a letter: ").lower();
    if len(letterGuess) > 1:
        letterGuess = letterGuess[0];
    
    if not letterGuess:
        break;
    for letter in chosen_word:
        if(letter == letterGuess):
            print("Right");
        else:
            print("Wrong");
    
        
    
    