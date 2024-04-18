from read_write_files import *
from text_encoding import *


if __name__ == "__main__":
    config = read_json_task_2("settings_file.json")
    text = config["path_text_task_1"]
    permutation = config["path_key_task_1"]

    encrypted_text = encrypt(text, permutation)
    decrypted_text = decrypt(encrypted_text, permutation)

    path_encrypted_text = config["path_encrypted_text"]
    path_decrypted_text = config["path_decrypted_text"]
    write_file(path_encrypted_text, encrypted_text)
    # write_file(path_decrypted_text, decrypted_text)
