import  math

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
    GROUP = 5  # Define the group size as a constant for clarity

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


def read_file_to_string(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().replace('\n', ' ')  # Replace newlines with spaces
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def save_string_to_file(text, file_path, mode='w'):
    try:
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(text)
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

if "__main__":
    text = read_file_to_string('books/war_and_peace_40.txt')
    encrypted = encrypt(text,1467)

    save_string_to_file(encrypted,'encrypted.txt')