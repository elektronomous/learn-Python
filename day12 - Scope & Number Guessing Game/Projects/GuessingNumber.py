import random

logo = """                                                                                                            ,--.                                                           
  ,----..                                                                                                 ,--.'|                       ____                                
 /   /   \                                                   ,--,                                     ,--,:  : |                     ,'  , `.  ,---,                       
|   :     :          ,--,                                  ,--.'|         ,---,                    ,`--.'`|  ' :         ,--,     ,-+-,.' _ |,---.'|               __  ,-. 
.   |  ;. /        ,'_ /|             .--.--.    .--.--.   |  |,      ,-+-. /  |  ,----._,.        |   :  :  | |       ,'_ /|  ,-+-. ;   , |||   | :             ,' ,'/ /| 
.   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '  `--'_     ,--.'|'   | /   /  ' /        :   |   \ | :  .--. |  | : ,--.'|'   |  ||:   : :      ,---.  '  | |' | 
;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./  ,' ,'|   |   |  ,"' ||   :     |        |   : '  '; |,'_ /| :  . ||   |  ,', |  |,:     |,-.  /     \ |  |   ,' 
|   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_    '  | |   |   | /  | ||   | .\  .        '   ' ;.    ;|  ' | |  . .|   | /  | |--' |   : '  | /    /  |'  :  /   
.   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `. |  | :   |   | |  | |.   ; ';  |        |   | | \   ||  | ' |  | ||   : |  | ,    |   |  / :.    ' / ||  | '    
'   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \'  : |__ |   | |  |/ '   .   . |        '   : |  ; .':  | : ;  ; ||   : |  |/     '   : |: |'   ;   /|;  : |    
'   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /|  | '.'||   | |--'   `---`-'| |        |   | '`--'  '  :  `--'   \   | |`-'      |   | '/ :'   |  / ||  , ;    
|   :    /  :  ,      .-./|   :    |'--'.     /'--'.     / ;  :    ;|   |/       .'__/\_: |        '   : |      :  ,      .-./   ;/          |   :    ||   :    | ---'     
 \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'  |  ,   / '---'        |   :    :        ;   |.'       `--`----'   '---'           /    \  /  \   \  /           
  `---`                     `----'                          ---`-'                \   \  /         '---'                                     `-'----'    `----'            
"""

ATTEMPT_EASY = 10;
ATTEMPT_HARD = 5;

def main():
    print(logo);

    level = input("Choose your difficulty, Type 'H' for Hard , 'E' for Easy: ").lower();

    if 'h' in level:
        guessing_attempt = ATTEMPT_HARD;
    else:
        guessing_attempt = ATTEMPT_EASY;
    
    print(f"You have {guessing_attempt} attempts remaining to guess the number")

    the_number = int(random.random() * 100);
    while guessing_attempt:
        guess = int(input("Make a guess: "));

        if not guess % the_number:
            print("You Win!");
            break;
        elif guess > the_number:
            print("It's too high");
        else:
            print("It's too low");
        
        guessing_attempt -= 1;
    
    if not guessing_attempt:
        print("You lost!");

if __name__ == "__main__":
    main();

        