from read_write_files import *
from text_encoding import *


if __name__ == "__main__":
    config = read_json("settings_file.json")
    text = read_file(config["path_text_task_1"])
    permutation = read_json(config["path_key_task_1"])

    encrypted_text = encrypt(text, permutation)
    decrypted_text = decrypt(encrypted_text, permutation)

    write_file(config["path_encrypted_text"], encrypted_text)
    write_file(config["path_decrypted_text"], decrypted_text)
