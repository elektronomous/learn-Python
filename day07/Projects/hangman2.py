import random
# Step 2
word_list = ["ardvark", "baboon", "camel"];
chosen_word = random.choice(word_list);

blank_spaces = [underscore for underscore in ('_' * len(chosen_word))];
print(chosen_word);


# TODO 1 -- Create an empty List called display.
            # For each letter in the chosen_word, add "_" to 'display'.
            # So if the chosen_word was "apple", the display should be
            # ["_", "_", "_", "_", "_"] with 5 "_" representing each
            # letter to guess.
# TODO 2 -- Loop through each position in the chosen word; 
            # if the letter at that position matches 'guess' then
            # reveal that letter in the display at that position.
            # e.g If the user guessed 'p' and the chosen word was
            # 'apple', then display should be ["_", "p", "p", "_", "_"].
# TODO 3 -- Print 'Display' and you should see the guessed letter in the correct
#           correct position and every other letter replace with "_".
            # Hint - Don't worry about getting the user to guess the next letter

end_of_game = False;

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
