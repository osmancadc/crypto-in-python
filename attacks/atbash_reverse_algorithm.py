
BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def reverse_algorithm(text):
    decrypted_text = ''
    for letter in text:
        if not letter in BASE:
            decrypted_text+=' '
            continue
       
        position = BASE.find(letter)+1 

        position = len(BASE)-position

        decrypted_text += BASE[position]
    print(f'Decrypted text: {decrypted_text}')


if __name__ == '__main__':
    print("------------ Athbash reverse algoritm ------------\n")
   
    plain = input(f'Enter the text to be decrypted: ')
    
    reverse_algorithm(plain.upper())
