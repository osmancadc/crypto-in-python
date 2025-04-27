# Crypto In Python
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/osmancadc/crypto-in-python/commits/main)

Welcome to **PyCryptopedia**, a growing collection of encryption algorithms implemented in Python. This repository aims to provide clear, concise, and well-documented implementations of various cryptographic techniques, along with brief explanations of their principles and historical context.

## About

This project is intended for educational purposes, allowing developers and enthusiasts to explore and understand the inner workings of different encryption methods. Each algorithm is implemented in Python and includes a dedicated README file within its directory, detailing its functionality, historical background, and usage examples.

## Algorithms

Below is a list of the encryption algorithms currently included in this repository. This list will expand as more algorithms are added over time. Click on the algorithm name to navigate to its dedicated folder for more information and the Python implementation.

* [**Classical Substitution**](classical-substitution) - Contains implementations of fundamental substitution ciphers like Atbash and Caesar, where plaintext units are systematically replaced.

* [**More algorithms coming soon...**](https://github.com/osmancadc/crypto-in-python/tree/main)


## Attack Scripts

The `attacks/` directory contains basic scripts demonstrating how some of the implemented ciphers can be broken. These scripts are provided for educational purposes to illustrate the weaknesses of these algorithms.

* [**Atbash Attack**](attacks/atbash_reverse_algorithm.py) - A simple script as the Atbash cipher is trivially broken.
* [**Caesar Attack**](attacks/caesar_brute_force.py) - A basic brute-force attack to try all possible shift values.
* [**More attack scripts coming soon...**](https://github.com/osmancadc/crypto-in-python/tree/main/attacks)

**Warning:** These attack scripts are for educational purposes only. Do not use them for any illegal or unethical activities.

## Structure


## Contributing

Contributions to this repository are welcome! If you'd like to add a new algorithm or improve an existing one, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your contribution (`git checkout -b feature/new-algorithm`).
3.  Implement the algorithm in Python within a new directory under the algorithm `./new-algorithm` folder.
4.  Include a detailed `README.md` file in the algorithm's directory, explaining the algorithm, its history, and usage examples.
5.  Add a link to your new algorithm in the "Algorithms" section of this main `README.md` file.
6.  Commit your changes (`git commit -am 'Add implementation for New Algorithm'`).
7.  Push to the branch (`git push origin feature/new-algorithm`).
8.  Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details.

## Stay Updated

Keep an eye on this repository for new algorithm implementations and updates! Feel free to star the repository to stay informed.

---

Thank you for exploring **Crypto In Python**!