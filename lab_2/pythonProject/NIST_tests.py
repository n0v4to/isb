import math
import mpmath
import os

from read_write_files import *


def frequency_test_nist(sequence: str, txt_file_path: str, key: str) -> None:
    """
        Perform frequency test based on NIST guidelines.

        Parameters:
        sequence (str): String of bits to be tested.
        txt_file_path (str): Path to the text file where results will be written.
        key (str): A key indicating which language the sequence was generated in.

        Returns:
        None
    """
    try:
        sequence_else = [-1 if bit == "0" else 1 for bit in sequence]
        s_n = sum(sequence_else) / math.sqrt(len(sequence_else))
        p_v = math.erfc(math.fabs(s_n) / math.sqrt(2))
        write_file(txt_file_path, f'{key} : {p_v}\n')
    except Exception as e:
        print("Frequency bitwise test, ERROR: ", e)

def same_bits_test_nist(sequence: str, txt_file_path: str, key: str) -> None:
    """
            Perform frequency test based on NIST guidelines.

            Parameters:
            sequence (str): String of bits to be tested.
            txt_file_path (str): Path to the text file where results will be written.
            key (str): A key indicating which language the sequence was generated in.

            Returns:
            None
    """


if __name__ == "__main__":
    config = read_json("settings_file.json")
    sequences = read_json(config["From"])
    sequences_cpp = sequences["C++"]
    sequences_java = sequences["Java"]
    print(type(sequences_cpp))
    print(type(sequences_java))
    # frequency_test_nist(sequences_cpp, config["To"], "C++")
    # frequency_test_nist(sequences_java, config["To"], "Java")
