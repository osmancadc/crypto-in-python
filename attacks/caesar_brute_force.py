
BASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def brute_force(text):
    for key in range(1, len(BASE)):
        decrypted_option=''

        for letter in text:
            if not letter in BASE:
                decrypted_option+=' '
                continue
            position = BASE.find(letter)
            position = (position-key) % len(BASE)
            decrypted_option+=BASE[position]

        print(f'Key: {key}: {decrypted_option}')



if __name__ == '__main__':
    print("------------ Caesar's brute force ------------\n")
   
    plain = input(f'Enter the text to be decrypted: ')
    
    brute_force(plain.upper())
    