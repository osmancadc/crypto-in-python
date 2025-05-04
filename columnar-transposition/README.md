# Columnar Transposition in Python

This directory contains an implementation of the Columnar Transposition cipher in Python. Transposition is another fundamental technique in cryptography; it consists of rearranging the positions of letters within the plaintext according to a specific algorithm known to both the sender and the receiver.

Transposition algorithms used in isolation are generally easy to decrypt and therefore highly insecure. However, they can be very effective when used in combination with other cryptographic techniques.


## About the Algorithm

```text
The `columnar_transposition.py` file includes a `__main__` module. Executing this file directly from your terminal using the command `python columnar_transposition.py` will initiate an interactive session.

The script will first prompt you to enter the plaintext you wish to encrypt. After you provide the text, it will then ask for the encryption key (an integer representing the number of columns).

Once both the plaintext and the key are provided, the script will perform the columnar transposition encryption and display the resulting ciphertext in the terminal.

Like the other algorithm implementations, you can also import the encryption and decryption functions from the `columnar_transposition.py` module into your own Python scripts for integration into larger projects.
```

### Columnar Transposition Cipher

Columnar Transposition is a cipher with historical roots tracing back to ancient Greece, with early forms possibly used by the Spartans. More direct versions emerged in the 16th century but gained prominence in the late 19th and 20th centuries. Notably, the German military employed a double columnar transposition during World War I, which the French successfully cracked. Its relative simplicity made it practical for field use even into the mid-20th century.

### Explaining the Algorithm
The columnar transposition algorithm implemented in this code follows three straightforward steps:

1. **Process Text:** This stage involves removing any whitespace or special characters from the input text and converting it to uppercase. This standardization aims to eliminate potential clues related to the start of the text based on capitalization.

2. **Transpose Text:** The processed text is then arranged into a matrix with a fixed number of columns, where the number of columns is determined by the encryption key.

3. **Group Text:** Finally, the transposed text is segmented into blocks of five letters for the final output, ensuring a consistent format for the ciphertext.

## Functions of the algorithm

### `1) process_text (text)`

This function accepts a single argument, `text`, and utilizes a global variable `BASE` which defines the allowed characters (currently the alphabet; you can extend this to include special characters or whitespace if needed).

```python
for letter in text.upper():
    if letter in BASE:
        processed_text+=letter
```

The function iterates through each character in the input `text`. For every character found within the `BASE` set, it is appended to the `processed_text` string. Finally, after processing all characters, the `processed_text` string is returned.

### `2) transpose_text (text, key)`

This is the core function of the algorithm, where the majority of the encryption process takes place. To illustrate its operation, let's consider the example phrase: ***The quick brown fox jumps over the lazy sleeping dog***.

If we perform the columnar transposition manually, as one would with pencil and paper using the key `7`, the plaintext would be arranged into a matrix as follows:

|**T**|**H**|**E**|**Q**|**U**|**I**|**C**|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**K**|**B**|**R**|**O**|**W**|**N**|**F**|
|**O**|**X**|**J**|**U**|**M**|**P**|**S**|
|**O**|**V**|**E**|**R**|**T**|**H**|**E**|
|**L**|**A**|**Z**|**Y**|**S**|**L**|**E**|
|**E**|**P**|**I**|**N**|**G**|**D**|**O**|
|**G**|

For enhanced understanding, we can visualize the transposition process by adding an index to each cell of the conceptual matrix, making the letter positions easier to track.

|**$\substack{T \\ 0}$**|**$\substack{H \\ 1}$**|**$\substack{E \\ 2}$**|**$\substack{Q \\ 3}$**|**$\substack{U \\ 4}$**|**$\substack{I \\ 5}$**|**$\substack{C \\ 6}$**|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**$\substack{K \\ 7}$**|**$\substack{B \\ 8}$**|**$\substack{R \\ 9}$**|**$\substack{O \\ 10}$**|**$\substack{W \\ 11}$**|**$\substack{N \\ 12}$**|**$\substack{F \\ 13}$**|
|**$\substack{O \\ 14}$**|**$\substack{X \\ 15}$**|**$\substack{J \\ 16}$**|**$\substack{U \\ 17}$**|**$\substack{M \\ 18}$**|**$\substack{P \\ 19}$**|**$\substack{S \\ 20}$**|
|**$\substack{O \\ 21}$**|**$\substack{V \\ 22}$**|**$\substack{E \\ 23}$**|**$\substack{R \\ 24}$**|**$\substack{T \\ 25}$**|**$\substack{H \\ 26}$**|**$\substack{E \\ 27}$**|
|**$\substack{L \\ 28}$**|**$\substack{A \\ 29}$**|**$\substack{Z \\ 30}$**|**$\substack{Y \\ 31}$**|**$\substack{S \\ 32}$**|**$\substack{L \\ 33}$**|**$\substack{E \\ 34}$**|
|**$\substack{E \\ 35}$**|**$\substack{P \\ 36}$**|**$\substack{I \\ 37}$**|**$\substack{N \\ 38}$**|**$\substack{G \\ 39}$**|**$\substack{D \\ 40}$**|**$\substack{O \\ 41}$**|
|**$\substack{G \\ 42}$**|

Observing the transposed matrix, we can see a pattern in how the letters are arranged. For instance, the first column contains letters originally at indices `0, 7, 21, 28, 35 and 42` in the plaintext (corresponding to `T, K, O, O, L, E, G`). The second column holds letters from indices `1, 8, 15, 22, 29 and 36` (`H, B, X, V, A, P`), and so forth for the remaining columns.

Following this pattern, the letters for each column with a starting index `n` are derived from the plaintext at indices `n`, `n + 7`, `n + 14`, `n + 21`, and so on. This progression continues as long as the calculated index remains within the total length of the original message. Once the index exceeds the message length, we move to the next column's starting index and repeat the process.

Applying this logic to the example, we obtain the following intermediate transposed sequence (preserving original case) before grouping:

```python
['TKOOLEG','HBXVAP','ERJEZI','QOURYN','UWMTSG','INPHLD','CFSEEO']
```

The preceding logic is precisely what the `transpose_text` function simulates. Given that the number of columns in our conceptual matrix directly corresponds to the encryption key, we utilize a loop where the `position` variable effectively represents the current column being processed.

```python
for i in range (key):
    position = i
```

Following this, we will iteratively add letters to the transposed text as long as the calculated index remains within the bounds of the original text's length. This iterative process is managed using a `while` loop.

```python
while position < len(text):
    transposed[i] += text[position]
    position += key
```

This `while` loop continues to execute as long as the calculated index is less than or equal to the original text's length. Within the loop, after adding a letter, the index is incremented by the value of the `key`. To illustrate this graphically, consider our example:

Here, we begin with column index `0` and a key of `7`.

|$\substack{⮕ \\ T}$|H|E|...|C|$\substack{⮕ \\ K}$|B|...|$\substack{⮕ \\ O }$|X|...|$\substack{⮕ \\ O}$|V|...|H|E|$\substack{⮕ \\ L}$|A|Z|...|D|O|$\substack{⮕ \\ G}$|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|2|...|6|7|8|...|14|15|...|21|22|...|26|27|28|29|30|...|40|41|42|

No, let's refine that for clarity. Consider the process starting with the **second** column (index `1` in programming terms, but often thought of as the "2nd" column conceptually) and the same key `7`:

|~~T~~|$\substack{⮕ \\ H}$|E|...|C|~~K~~|$\substack{⮕ \\ B}$|...|~~O~~|$\substack{⮕ \\ X }$|...|~~O~~|$\substack{⮕ \\ V}$|...|H|E|~~L~~|$\substack{⮕ \\ A}$|Z|...|D|O|G|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|~~0~~|1|2|...|6|~~7~~|8|...|~~14~~|15|...|~~21~~|22|...|26|27|~~28~~|29|30|...|40|41|~~42~~|

Once this loop completes its iterations across all columns, we will have the following array representing the transposed text:

```python
['TKOOLEG','HBXVAP','ERJEZI','QOURYN','UWMTSG','INPHLD','CFSEEO']
```

Finally, we employ the `join()` method to concatenate the elements of this array (representing the columns read sequentially) into a single `string`, which is then returned as the result of the transposition.

```python
return ''.join(transposed)
```


### `3) group_text (text)`

After transforming and encrypting the text using the columnar transposition algorithm, we utilize the `group_text` function. This function inserts a whitespace character after every five characters in the ciphertext. This formatting is achieved through a straightforward `for` loop with a counter.

```python
GROUP = 5
grouped_text = ''

for i in range(len(text)):
    grouped_text += text[i]

    if (i+1) % GROUP == 0:
        grouped_text+=' '
```

Here, we have a `GROUP` variable set to `5`, which defines the standard length of the encrypted text segments. The conditional statement `if (i+1) % GROUP == 0` checks if the current character's position (`i+1`, as indexing starts from `0` while our positional count begins from `1`) is a multiple of the `GROUP` size.

### How to use

The `columnar_transposition.py` module provides functions for encrypting text using the Columnar Transposition.

#### `encrypt(text, key)`


**Example:**

```python
from columnar_transposition import encrypt

plaintext = "The quick brown fox jumps over the lazy sleeping dog"
encryption_key = 7

ciphertext = encrypt(plaintext, encryption_key)

print(f"Plaintext: {plaintext}") # Output: The quick brown fox jumps over the lazy sleeping dog

print(f"Ciphertext: {ciphertext}") # Output: TKOOL EGHBX VAPER JEZIQ OURYN UWMTS GINPH LDCFS EEO
```

## Contributing

If you have improvements or would like to add more columnar transposition implementations to this directory, feel free to contribute by following the guidelines outlined in the main repository's README.

## License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE). See the `LICENSE` file in the main repository for more details.