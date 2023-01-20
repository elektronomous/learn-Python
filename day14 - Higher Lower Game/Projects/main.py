from logo import logo, vs
from game_data import data as game_data
import os
import random

def main():
    on_game = True;
    score = 0;
    debug = False;

    # get game_data length
    nData = len(game_data);
    
    # print the logo first
    print(logo);
    
    while on_game:
        for n in range(nData):
            if n + 2 > nData:
                break;

            # get the data profile
            data = {
                'A': game_data[random.randint(n, nData-1)],
                'B': game_data[random.randint(n, nData-1)]
            };

            # make sure the data isn't same
            if data['A']['name'] is data['B']['name']:
                data['B'] = game_data[random.randint(n, nData - 1)];

            if(debug):
                print(data['A']['follower_count']);
                print(data['B']['follower_count']);

            print(f"Compare A: {data['A']['name']}, {data['A']['description']} from {data['A']['country']}");
            print(vs);
            print(f"Against B: {data['B']['name']}, {data['B']['description']}, from {data['B']['country']}");

            answer = input("Who has more followers? Type 'A' or 'B': ").upper();
            os.system('clear');

            if answer not in 'AB':
                on_game = False;
                break;
            
            answerFollower = data[answer]['follower_count'];
            compareFollower = data['B' if 'B' != answer else 'A']['follower_count'];

            if answerFollower > compareFollower:
                score += 1;
                print(f"You right! Current score: {score}");
            else:
                print(f"Sorry, that's wrong. Final score: {score}");
                on_game = False;
                break;

if __name__ == "__main__":
    main();