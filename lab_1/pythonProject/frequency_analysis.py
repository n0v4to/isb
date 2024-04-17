from collections import Counter
from read_write_files import *


def frequency_analysis(info: str) -> None:
    """
    Performs a frequency analysis of the text and returns a dictionary with character frequencies.

    Args:
        info (str): The text to analyze.
    """
    total = len(info)
    frequencies = {char: count / total for char, count in Counter(info).items()}
    write_json_task_2("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_2/frequencies.json", frequencies)


def compare_frequencies(frequencies: dict, alphabet_frequencies: dict) -> None:
    """
    Compares the frequencies dictionary with the letter frequencies of the Russian alphabet
    and creates a decryption key.

    Args:
        frequencies (dict): The dictionary of character frequencies to compare.
        alphabet_frequencies (dict): The dictionary of alphabet letter frequencies.
    """
    sorted_frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
    # sorted_alphabet_frequencies = dict(sorted(alphabet_frequencies.items(), key=lambda x: x[1], reverse=True))

    decryption_key = {}
    for char, freq in sorted_frequencies.items():
        for alpha_char, alpha_freq in alphabet_frequencies.items():
            if alpha_char not in decryption_key.values() and alpha_char not in decryption_key.keys():
                decryption_key[char] = alpha_char
                break
    write_json_task_2("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_2/decryption_key.json", decryption_key)
