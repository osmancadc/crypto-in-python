import pyperclip

BASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar(text, key, is_encrypt):
    encrypted_text = ''
    for letter in text:
        if letter == ' ':
            encrypted_text+=' '
            continue
        if letter in BASE:
            position = BASE.find(letter)

            if is_encrypt:
                position = (position+key)%26
            else:
                position = (position-key)%26
        
        encrypted_text+=BASE[position]    
    return encrypted_text



if __name__ == '__main__':
    print("------------ Caesar's Cipher ------------")
    print("1. Encrypt text")
    print("2. Decrypt text")
    selection = int(input('What do you want to do? '))
    is_encrypt = selection == 1 
    plain = input(f'Enter the text to be {'encrypted' if is_encrypt else 'decrypted'}: ')
    key = int(input(f'Enter the {'encryption' if is_encrypt else 'decryption'} key (between 1 and 25): '))
    encrypted_text = caesar(plain.upper(), key, is_encrypt)
    print('The encrypted text is: ',encrypted_text)
    pyperclip.copy(encrypted_text)