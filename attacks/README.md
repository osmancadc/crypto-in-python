# Attack Scripts

This directory contains simple scripts demonstrating how to break the encryption algorithms implemented in the main repository. These scripts are provided for educational purposes to illustrate the vulnerabilities of these classical ciphers.

## Usage

To use these attack scripts, you will need to have Python installed on your system. Navigate to this `attacks/` directory in your terminal and run the desired script.

### Disclaimer
These attack scripts are intended for educational purposes only. They demonstrate the weaknesses of simple classical ciphers and should not be used for any illegal or unethical activities.

## Currently Included Attacks

* **`caesar_brute_force.py`**: This script performs a brute-force attack against the Caesar cipher. It attempts to decrypt the provided ciphertext by trying every possible shift value (key) within the alphabet. For each possible key, it prints the resulting decrypted text, allowing a user to visually identify the correct plaintext. 
    ```bash
        python caesar_brute_force.py 
    ```


* **`atbash_reverse_algorithm.py`**: This script implements the decryption logic for the Atbash cipher. Since the Atbash cipher's encryption is a direct reversal of the alphabet, the decryption process is identical. The script takes ciphertext as input and applies the Atbash substitution to recover the original plaintext.
    ```bash
        python atbash_reverse_algorithm.py
    ```

 

## Contributing
If you develop attack scripts for any algorithm in this repository, feel free to contribute them by following the guidelines in the main repository's README. Ensure your scripts are well-commented and include clear usage instructions.