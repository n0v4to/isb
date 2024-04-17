from read_write_files import *


def decrypt_task_2(encoded_text: str, decryption_key: dict) -> None:
    """
    Decrypts the encoded text using a simple substitution cipher decryption key from a JSON file.

    Args:
        encoded_text (str): The text to decrypt.
        decryption_key (dict): The path to the JSON file containing the decryption key.
    """
    decrypted_text = ''
    for char in encoded_text:
        if char in decryption_key:
            decrypted_text += decryption_key[char]
        else:
            decrypted_text += char
    write_file("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_2/decryption_text.txt", decrypted_text)

