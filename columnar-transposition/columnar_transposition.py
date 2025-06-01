import pyperclip, math

BASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def process_text(text):
    """
    Prepares the input text for encryption by converting it to uppercase
    and removing any characters not present in the defined BASE character set.
    This ensures only allowed characters are processed.

    Args:
        text (str): The input string to be processed.

    Returns:
        str: The processed uppercase string containing only characters from BASE.
    """
    processed_text = ''

    for letter in text.upper():
        if letter in BASE:
            processed_text+=letter
            
    return processed_text

def transpose_text(text, key):
    """
    Encrypts the input text using a columnar transposition cipher with the given key.
    Characters are written into a conceptual grid of 'key' columns and then
    read column by column to produce the transposed ciphertext.

    Args:
        text (str): The text to be transposed.
        key (int): The number of columns to use in the transposition grid.
                   This determines the transposition pattern.

    Returns:
        str: The ciphertext resulting from the columnar transposition.
    """
    transposed = [''] * key

    for i in range (key):
        position = i

        while position < len(text):
            transposed[i] += text[position]

            position += key

    return ''.join(transposed)

def group_text(text):
    """
    Groups the input text into blocks of a predefined size (GROUP).
    Spaces are inserted after every 'GROUP' characters to enhance readability
    of the ciphertext.

    Args:
        text (str): The text to be grouped.

    Returns:
        str: The text with spaces inserted after every GROUP characters.
    """
    GROUP = 5  # Define the group size as a constant for clarity

    grouped_text = ''

    for i in range(len(text)):
        grouped_text += text[i]

        if (i+1) % GROUP == 0:
            grouped_text+=' '

    return grouped_text

def encrypt(text, key):
    """
    Encrypts the given text using a combination of processing, transposition,
    and grouping steps.

    Args:
        text (str): The original plaintext to be encrypted.
        key (int): The key used for the transposition cipher.

    Returns:
        str: The final encrypted ciphertext.
    """
    text = process_text(text)

    transposed_text = transpose_text(text, key)

    return group_text(transposed_text)

def decrypt(encrypted_text, key):
    encrypted_text = process_text(encrypted_text)

    num_cols = math.ceil(len(encrypted_text)/key)
    empty_rows = (num_cols * key) - len(encrypted_text)

    plain_text = [''] * num_cols

    col = 0
    row = 0
    for letter in encrypted_text:
        plain_text[col] += letter
        col+=1

        if (col == num_cols) or (col == num_cols - 1 and row >= key - empty_rows):
            col = 0
            row += 1

    return ''.join(plain_text)


if __name__ == "__main__":
    text = input('Enter text to be encrypted: ')
    key = int(input('Enter the secret key: '))

    encrypted_text = encrypt(text, key)

    print(f'Ecnrypted text: {encrypted_text}')
    pyperclip.copy(encrypt)


