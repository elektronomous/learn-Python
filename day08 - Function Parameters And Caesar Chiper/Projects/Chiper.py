alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
nAlphabet = len(alphabet);

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower();
text = input("Type your message:\n");
shift = int(input("Type the shift number:\n"));

# TODO - 1 - Create a function called 'encrypt' that takes the 'text' and 
#            'shift' as input.
             # TODO - 2 - Inside the 'encrypt' function, shift each letter of the 'text'
             #            forwards in the alphabet of the shift amount and print the encrypted text
             # e.g
             # plain_text = "hello"
             # shift = 5
             # chiper_text = "mjqqt"
             # print output: the encoded text is "mjqqt"

# TODO - 3 - Call the encrypt function and pass in the user inputs. you should be able
#            to test the code and encrypt a message

def encrypt(text, shift):
    if shift:
        charPositions = [alphabet.index(char) for char in text];
        shiftPositions = [shift + charPositions[n] for n in range(len(charPositions))];
        chiperText = ''.join()
    else:
        return text; 

encrypt(text, shift);