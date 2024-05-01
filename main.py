from affine_cipher import AffineCipher

Af = AffineCipher()
plaintext = 'I want to work as a cyber security professional'
key = (3, 24)
ciphertext = Af.encrypt(plaintext, key)
decrypted_text = Af.decrypt(ciphertext, key)
print(plaintext)
print(ciphertext)
print(decrypted_text)
