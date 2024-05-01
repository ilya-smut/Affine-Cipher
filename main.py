from affine_cipher import AffineCipher

Af = AffineCipher()
plaintext = 'This is an example text. It works absolutely fine!!!'
key = Af.get_random_key()

ciphertext = Af.encrypt(plaintext, key)
print('CIPHERTEXT:', ciphertext)

decrypted_message = Af.decrypt(ciphertext, key)
print('DECRYPTED:', decrypted_message)

print('KEY:', key)
