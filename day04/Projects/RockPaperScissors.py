import random

rock = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handForm = [paper, scissor, rock];

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"));
computerChoice = random.randint(0,len(handForm)-1);

if userChoice < len(handForm) and computerChoice < len(handForm):
    output = f"{handForm[userChoice]}\nComputer chose:\n{handForm[computerChoice]}";
    
    if computerChoice == 0 and userChoice == 2:
        userChoice = -1;
    elif computerChoice == 2 and userChoice == 0:
        computerChoice = -1;

    if userChoice > computerChoice:
        print(f"{output}\nYou Win!");
    elif computerChoice > userChoice:
        print(f"{output}\nYou lose");
    else:
        print(f"{output}\nDraw");
else:
    print("You lose.");


