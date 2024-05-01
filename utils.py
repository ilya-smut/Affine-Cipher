import re


def generate_letter_map():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    alphabet_mapping = {letter: index for index, letter in enumerate(alphabet)}
    index_mapping = {index: letter for index, letter in enumerate(alphabet)}
    return alphabet_mapping, index_mapping


def sanitize_input(input_string):
    # Remove everything but capital English letters
    sanitized_string = re.sub(r'[^A-Za-z0-9 !?.]', '', input_string)
    return sanitized_string


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def find_mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m aren't relatively prime.
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
