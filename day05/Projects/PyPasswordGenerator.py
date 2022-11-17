import string       # import ASCII letters, digits, punctuation
import random

print("Welcome to the PyPassword Generator!");

alphabet = string.ascii_letters;
numeric = string.digits;
symbol = string.punctuation;

nLetters = int(input("How many letters would you like in your password\n"));
nSymbols = int(input("How many symbols would like?\n"));
nNumbers = int(input("How many numbers would you like?\n"));

thePassword = [];

for n in range(0, nLetters):
    thePassword.append(random.choice(alphabet));
for n in range(0, nSymbols):
    thePassword.append(random.choice(symbol));
for n in range(0, nNumbers):
    thePassword.append(random.choice(numeric));

random.shuffle(thePassword);
print(f"Your password: {''.join(thePassword)}")