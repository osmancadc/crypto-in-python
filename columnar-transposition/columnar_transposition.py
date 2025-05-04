import pyperclip

BASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def process_text(text):
    processed_text = ''

    for letter in text.upper():
        if letter in BASE:
            processed_text+=letter
            
    return processed_text

def transpose_text(text, key):
    transposed = [''] * key

    for i in range (key):
        position = i

        while position < len(text):
            transposed[i] += text[position]

            position += key

    return ''.join(transposed)

def group_text(text):
    GROUP = 5

    grouped_text = ''

    for i in range(len(text)):
        grouped_text += text[i]

        if (i+1) % GROUP == 0:
            grouped_text+=' '

    return grouped_text

def encrypt(text, key):
    text = process_text(text)

    transposed_text = transpose_text(text, key)    

    return group_text(transposed_text)


        


if __name__ == "__main__":
    text = input('Enter text to be encrypted: ')
    key = int(input('Enter the secret key: '))

    encrypted_text= encrypt(text, key)

    print('Encrypted text: ', encrypted_text)
    pyperclip.copy(encrypted_text)


