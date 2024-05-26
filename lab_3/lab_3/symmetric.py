import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from read_write_file import *


class Symmetric:
    """
    A class that implements symmetric encryption using the SM4 algorithm.

    Attributes
        key: encryption key
    """

    def __init__(self):
        self.key = None

    def key_generation(self, size_key: int) -> bytes:
        """
        Generates a random encryption key of the specified length in bits.

        Args:
            size_key: The desired length of the encryption key in bits.
        Returns:
            The generated encryption key.
        """
        if size_key < 40 or size_key > 128 or size_key % 8 != 0:
            raise ValueError("Некорректная длина ключа. Длина должна быть от 40 до 128 кратно 8.")

        self.key = os.urandom(size_key // 8)
        return self.key

    def key_serialization(self, path: str) -> None:
        """
        Serializes the encryption key to a file.

        Args:
        path: The path to the file where the encryption key will be saved.
        """
        try:
            with open(path, 'wb') as key_file:
                key_file.write(self.key)
        except FileNotFoundError:
            print(f"Ошибка! Файл {path} не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

    def key_deserialization(self, path: str) -> None:
        """
        Deserializes the encryption key from a file.
        Parameters
            path: The path to the file containing the encryption key.
        """
        with open(path, "rb") as file:
            self.key = file.read()
        try:
            with open(path, "rb") as file:
                self.key = file.read()
        except FileNotFoundError:
            print(f"Ошибка! Файл {path} не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

    def encrypt(self, path: str, encrypted_path: str) -> bytes:
        """
        Encrypts data from a file using the SM4 algorithm in CFB mode.

        Args:
            path: The path to the file with the source data.
            encrypted_path: The path to the file where the encrypted data will be written.
        Returns:
            The encrypted data.
                """
        text = read_bytes_from_text(path)
        iv = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(self.key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(64).padder()
        padded_text = padder.update(text) + padder.finalize()
        cipher_text = iv + encryptor.update(padded_text) + encryptor.finalize()
        write_bytes_text(encrypted_path, cipher_text)
        return cipher_text

    def decrypt(self, encrypted_path: str, decrypted_path: str) -> str:
        """
        Decrypts data from a file using the SM4 algorithm in CFB mode.

        Parameters
            encrypted_path: The path to the file with the encrypted data.
            decrypted_path: The path to the file where the decrypted data will be written.
        Returns
            The decrypted data as a string.
        """
        encrypted_text = read_bytes(encrypted_path)
        iv = encrypted_text[:8]
        cipher_text = encrypted_text[8:]
        cipher = Cipher(algorithms.CAST5(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypt_text = decryptor.update(cipher_text) + decryptor.finalize()
        unpadder = padding.PKCS7(64).unpadder()
        unpadded_dc_text = unpadder.update(decrypt_text) + unpadder.finalize()
        decrypt_text = unpadded_dc_text.decode('UTF-8')
        write_file(decrypted_path, decrypt_text)
        return decrypt_text
