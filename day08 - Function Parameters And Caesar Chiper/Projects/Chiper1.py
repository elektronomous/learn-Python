alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
nAlphabet = len(alphabet);


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
"""
def encrypt(plainText, shiftAmount):
    if shiftAmount:
        charPositions = [alphabet.index(char) for char in plainText];
        shiftPositions = [shiftAmount + charPositions[n] for n in range(len(charPositions))];
        chiperText = ''.join(alphabet[shiftPositions[n] % nAlphabet] for n in range(len(shiftPositions)));

        print(f"The encoded text is \"{chiperText}\"");

        print(chiperText);
    else:
        print(plainText);
"""
# TODO - 1 - Create a different function called 'decrypt' that takes the 'text' and 'shift as inputs
# TODO - 2 - Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet
#            by the shift amount and print the decrypted text.
#            e.g
#            chiper_text = "mjqqt"
#            shift = 5
#            plain_text = "hello"
#            print output: "The decoed text is hello";
# TODO - 3 - Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#            Then call the correct function based on that 'direction' variable. You should be able to test the
#            the code to encrypt *AND* decrypt a message.
"""
def decrypt(plainText, shiftAmount):
    encrypt(plainText=plainText, shiftAmount=shiftAmount);
"""

# TODO - 1 - Combine the encrypt() and decrypt() functions into a single functions called caesar()
#            Commeneting out the encrypt decrypt function
def caesar(plainText, shiftAmount, direct):
    if shiftAmount:
        if direct == 'decode':
            shiftAmount = -shiftAmount;

        charPositions = [alphabet.index(char) for char in plainText];
        shiftPositions = [shiftAmount + charPositions[n] for n in range(len(charPositions))];
        chiperText = ''.join(alphabet[shiftPositions[n] % nAlphabet] for n in range(len(shiftPositions)));
        plainText = chiperText;
    print(f"The encoded text is \"{plainText}\"");

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower();
    text = input("Type your message:\n");
    shift = int(input("Type the shift number:\n"));

    caesar(plainText=text, shiftAmount=shift, direct=direction);


if __name__ == '__main__':
    main();