from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64

class PasswordEncryptor:
    def __init__(self, password_to_save, password_to_encrypt):
        self.password_to_save = password_to_save
        self.password_to_encrypt = password_to_encrypt
        self.salt = os.urandom(16)

    def generate_key_from_password(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def encrypt_password(self):
        key = self.generate_key_from_password(self.password_to_encrypt, self.salt)

        # Generar un IV (Initialization Vector) aleatorio para el modo CBC
        iv = os.urandom(16)

        # Crear el cifrador AES en modo CBC
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

        # Obtener el objeto para cifrar
        encryptor = cipher.encryptor()

        # Padding: asegurar que el mensaje sea un múltiplo del tamaño del bloque (en este caso, 16 bytes)
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(self.password_to_save.encode()) + padder.finalize()

        # Cifrar el mensaje
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        # Concatenar el IV y la sal al principio del mensaje cifrado para usarlo en el descifrado
        encrypted_password = self.salt + iv + ciphertext

        return encrypted_password

    def decrypt_password(self, encrypted_password):
        key = self.generate_key_from_password(self.password_to_encrypt, self.salt)

        # Extraer la sal y el IV del mensaje cifrado
        salt = encrypted_password[:16]
        iv = encrypted_password[16:32]

        # Crear el cifrador AES en modo CBC con el IV extraído
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

        # Obtener el objeto para descifrar
        decryptor = cipher.decryptor()

        # Descifrar el mensaje
        decrypted_padded_data = decryptor.update(encrypted_password[32:]) + decryptor.finalize()

        # Deshacer el padding para obtener la contraseña original
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

        return decrypted_data.decode()

if __name__ == "__main__":
    # Contraseñas para guardar cifrada y cifrar
    password_to_save = "contraseña1"
    password_to_encrypt = "contraseñaSegura"

    # Crear una instancia de la clase con las contraseñas
    password_encryptor = PasswordEncryptor(password_to_save, password_to_encrypt)

    # Cifrar la contraseña para guardar
    encrypted_password = password_encryptor.encrypt_password()

    # Descifrar la contraseña guardada
    decrypted_password = password_encryptor.decrypt_password(encrypted_password)

    print(f"Contraseña original para guardar: {password_to_save}")
    print(f"Contraseña cifrada: {base64.urlsafe_b64encode(encrypted_password).decode()}")
    print(f"Contraseña descifrada: {decrypted_password}")
