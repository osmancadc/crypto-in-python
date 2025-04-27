import pyperclip

PLAIN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
CIPHER = "ZYXWVUTSRQPONMLKJIHGFEDCBA "

def atbash(text):
    encrypted_text = ''
    for letter in text:
        if letter in PLAIN:
            i = PLAIN.find(letter)
            encrypted_text += CIPHER[i]
    return encrypted_text


if __name__ == "__main__":
    text = input('Enter text to be encrypted: ')    
    encrypted_text= atbash(text.upper())
    print('Encrypted text: ', encrypted_text)
    pyperclip.copy(encrypted_text)


