import utils


class AffineCipher:
    def __init__(self):
        self.char_to_int_map, self.int_to_char_map = utils.generate_letter_map()

    def match_map(self, match_element):
        if type(match_element) is str:
            return self.char_to_int_map[match_element]
        elif type(match_element) is int:
            return self.int_to_char_map[match_element]

    def string_to_indexes(self, string):
        string = utils.sanitize_input(string)
        index_list = []
        for char in string:
            index_list.append(self.match_map(char))
        return index_list

    def indexes_to_string(self, index_list):
        string = ''
        for i in index_list:
            string += self.match_map(i)
        return string

    def encrypt(self, plaintext, key):
        ciphertext = []
        plaintext_indexes = self.string_to_indexes(plaintext)
        factor, additive = key

        # Ciphertext index = (index * factor + additive ) modulo 26 for English Alphabet

        for i in plaintext_indexes:
            ciphertext.append((i*factor + additive) % 26)
        return self.indexes_to_string(ciphertext)

    def decrypt(self, ciphertext, key):
        plaintext = []
        ciphertext_indexes = self.string_to_indexes(ciphertext)
        factor, additive = key
        reverse_factor = utils.find_mod_inverse(factor, 26)
        for index in ciphertext_indexes:
            index = (index - additive) % 26
            index = (index * reverse_factor) % 26
            plaintext.append(index)
        return self.indexes_to_string(plaintext)
