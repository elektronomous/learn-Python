import random
# Step 2
word_list = ["ardvark", "baboon", "camel"];
chosen_word = random.choice(word_list);

blank_spaces = [underscore for underscore in ('_' * len(chosen_word))];
print(chosen_word);


# TODO 1 -- Use a while loop to let the user guess again. The loop should only stop
#           once the user has guessed all the letters in the chosen_word and 'display'
#           has no more blanks("_")

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
