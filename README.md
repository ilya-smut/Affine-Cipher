# Affine Cipher Project 👨‍💻

## Description 📝

This project includes a Python implementation of the Affine Cipher, a type of monoalphabetic substitution cipher. It provides a simple (but INSECURE by modern standards!!!) method for encryption and decryption of text.

## Code Structure 🏗️

The project consists of three main Python files:

1. **utils.py**: This file contains utility functions used in the project. These include functions for generating character maps, sanitizing input, and performing mathematical operations necessary for the cipher, including finding gcd, performing reverse factor search using extended Euclidean algorithm, validating keys, etc. 
2. **affine_cipher.py**: This file contains the main implementation of the Affine Cipher. It includes methods for matching maps, converting strings to indexes and vice versa, generating keys, and executing the encryption and decryption processes.
3. **main.py**: This file is where the AffineCipher class is instantiated and used. It demonstrates the encryption and decryption process with an example.

## Usage 💻

To use the Affine Cipher, you need to instantiate the `AffineCipher` class and use the `encrypt` and `decrypt` methods. The `get_random_key` method can be used to generate a random key for encryption.

Example:

```python
from affine_cipher import AffineCipher

Af = AffineCipher()
plaintext = 'This is an example text. It works absolutely fine!!!'
key = Af.get_random_key()

ciphertext = Af.encrypt(plaintext, key)
print('CIPHERTEXT:', ciphertext)

decrypted_message = Af.decrypt(ciphertext, key)
print('DECRYPTED:', decrypted_message)

print('KEY:', key)

```

This project represents a basic implementation of the Affine Cipher in Python. It serves as a good starting point for those interested in learning more about encryption and cryptography. 🔒
