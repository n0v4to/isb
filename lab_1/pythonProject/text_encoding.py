from typing import List


def encrypt(text: str, permutation: dict) -> str:
    """
        Encrypts the text using a permutation cipher.

        Args:
            text: The text to be encrypted.
            permutation: The permutation list to be applied for encryption.

        Returns:
            The encrypted text.
    """
    values_list = list(permutation.values())
    num_blocks = (len(text) + len(values_list) - 1) // len(values_list)
    padded_text = text.ljust(num_blocks * len(values_list))

    encrypted_text = [''] * len(padded_text)

    for i, perm_index in enumerate(values_list):
        for j in range(num_blocks):
            encrypted_text[j * len(values_list) + perm_index - 1] = padded_text[i * num_blocks + j]

    return ''.join(encrypted_text)


def decrypt(encrypted_text: str, permutation: dict) -> str:
    """
        Decrypts the encrypted text using a permutation cipher.

        Args:
            encrypted_text: The text to be decrypted.
            permutation: The permutation list used for encryption.

        Returns:
            The decrypted text.
    """
    values_list = list(permutation.values())
    num_blocks = len(encrypted_text) // len(values_list)

    decrypted_text = [''] * len(encrypted_text)

    for i, perm_index in enumerate(values_list):
        for j in range(num_blocks):
            decrypted_text[i * num_blocks + j] = encrypted_text[j * len(values_list) + perm_index - 1]

    return ''.join(decrypted_text).rstrip()
