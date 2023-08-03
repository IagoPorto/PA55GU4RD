import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
class AES:

    def __init__(self):
        pass

    def encrypt_data(self, key, data):
        iv = os.urandom(16)
        encryptor = Cipher(algorithms.AES(key.encode('utf-8')), modes.GCM(iv), backend=default_backend()).encryptor()
        ciphertext = encryptor.update(data.encode('utf-8')) + encryptor.finalize()
        return (iv, ciphertext, encryptor.tag)

    def decrypt_data(self, key, iv, ciphertext, tag):
        decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend()).decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data.decode('utf-8')