from decrypt_text import *
from frequency_analysis import *
from read_write_files import *


if __name__ == "__main__":
    config = read_json_task_2("settings_file.json")
    text = config["path_text_task_2"]
    path_decryption_text = config["path_decryption_text"]
    path_frequencies = config["path_frequencies"]
    path_decryption_key = config["path_decryption_key"]

    # frequency_analysis(path_decryption_key, text)
    # frequency = config["path_frequency"]
    # alphabet = config["path_alphabet"]
    # compare_frequencies(path_frequencies, frequency, alphabet)

    key = config["path_key_task_2"]
    decrypt_task_2(path_decryption_text, text, key)
