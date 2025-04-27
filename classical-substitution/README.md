# Classical Substitution Ciphers in Python

This directory contains implementations of classical substitution ciphers in Python. Substitution ciphers are a method of encryption where units of plaintext are replaced with ciphertext, according to a regular system. The algorithms included here are foundational examples in the history of cryptography.

## Algorithms Included

This folder currently houses the following classical substitution ciphers:

* Atbash Cipher: A simple substitution cipher where each letter is replaced by the letter in the same position in the reversed alphabet.
* Caesar Cipher: A type of substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.

Each algorithm has its own Python implementation file. This README provides an overview of the ciphers included in this directory. For detailed information on a specific cipher, please refer to its individual comments within the Python file.



## About the algorithms

```text
Both the `atbash.py` and `caesar.py` files include a `__main__`
module. This means that if you execute these files directly from 
your terminal using the command `python atbash.py` or `python caesar.py`, 
they will prompt you to enter the text you wish to encrypt via the keyboard. 

This allows for quick testing and experimentation with the ciphers 
without the need to write a separate script to import and use their functions. 

If you prefer to integrate these cipher functions into your own Python projects, 
you can simply import them as modules.
```
### ATBASH Cipher

The Atbash cipher is a very simple substitution cipher that dates back to around **500-600 BCE.** It was originally used for the Hebrew alphabet and is mentioned in several Jewish texts. Its name, "***Atbash***" is actually derived from the Hebrew alphabet itself: the first letter ('Aleph') is replaced by the last ('Tav'), the second ('Bet') by the second to last ('Shin'), and so on. This direct reversal of the alphabet forms the basis of the cipher, making it exceptionally easy to implement but also very weak against cryptanalysis.

This algorithm is uniquely notable for its usage in one of the world's most famous books, the Bible. In **Jeremiah 25:26 ; 51:41**, the cryptogram '***SHESHAC***' is used to substitute the plaintext '***BABEL***'. It's believed that the use of this algorithm in the Bible was likely not intended to conceal information but rather to add an extra layer of mystery or perhaps a stylistic element to the text.

### How to use

The `atbash.py` module provides functions for encrypting text using the Atbash cipher.

#### `atbash(text)`

```python
from atbash import atbash

plaintext = "Hello World"
ciphertext = atbash(plaintext) 

print(f"Plaintext: {plaintext}") # Output Hello World 

print(f"Ciphertext (Atbash): {ciphertext}") # Output SVOOL DLIOW
```

## Caesar Cipher

The Caesar cipher, one of the earliest known and simplest encryption techniques, is attributed to Julius Caesar, who reportedly used it for military communications. It operates by shifting each letter in the plaintext a fixed number of positions down the alphabet. For example, with a shift of 3, 'A' would become 'D', 'B' would become 'E', and so on, wrapping around the alphabet if necessary. Its ease of use and implementation made it historically significant, though its simplicity also renders it quite vulnerable to basic cryptanalytic attacks.

The first documented use of the substitution cipher is in The Gallic Wars by Julius Caesar where he described how he managed to send a message to Cicero, who was besieged and about to surrender. The substitution replaces Greek letters for Latin words, making the message completely unintelligible to the enemy.

### How to use

The `caesar.py` module provides functions for encrypting and decrypting text using the Caesar cipher.

#### `encrypt(text, shift)`

This function encrypts the input `text` by shifting each alphabetic character by the specified `shift` value.

* `text` (str): The plaintext to be encrypted.
* `shift` (int): The number of positions to shift each letter. A positive value shifts to the right, and a negative value shifts to the left.

It preserves the case of the letters. Non-alphabetic characters are left unchanged. The shift value will wrap around the alphabet (e.g., a shift of 27 is the same as a shift of 1 for the English alphabet).

**Example:**

```python
from caesar import caesar

plaintext = "Hello World"
shift_value = 3

ciphertext = caesar(plaintext, shift_value)

print(f"Plaintext: {plaintext}") # Output: Hello World

print(f"Ciphertext: {ciphertext}") # Output: Khoor Zruog
```

## Contributing

If you have improvements or would like to add more classical substitution cipher implementations to this directory, feel free to contribute by following the guidelines outlined in the main repository's README.

## License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE). See the `LICENSE` file in the main repository for more details.