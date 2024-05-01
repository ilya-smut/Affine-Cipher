from affine_cipher import AffineCipher

Af = AffineCipher()
plaintext = 'This is an example text. It works absolutely fine!!!'

key = (13, 1)

ciphertext = Af.encrypt(plaintext, key)
decrypted_text = Af.decrypt(ciphertext, key)

print(ciphertext)
print(decrypted_text)
