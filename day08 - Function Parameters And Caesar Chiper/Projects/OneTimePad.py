def oneTimePad(plaintext:str, key:str, decryption = False):
    a = [];

    if decryption:
        plaintext = plaintext.split('-');
        print(plaintext);
    # the key and plaintext should in the same length
    if (len(plaintext) % len(key)):
        print("The key and the plaintext must be the same length.");
        return '';

    for n in range(len(plaintext)):
        # xor each of the plaintext using the key
        if decryption:
            a.append(chr(int(plaintext[n]) ^ ord(key[n])));
        else:
            a.append(str(ord(plaintext[n]) ^ ord(key[n])));
    
    return a;

def main():
    text = input("Input the plaintext: ");
    key = input("Input the key: ");
    decryption = input("(D)ecryption or (E)ncryption: ").lower();

    # Decryption
    if 'd' in decryption:
        print(f"Decrypted: {''.join(oneTimePad(text, key, True))}");
    else:
        print(f"Encrypted: {'-'.join(oneTimePad(text, key))}");


if __name__ == "__main__":
    main();