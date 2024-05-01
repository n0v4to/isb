import math
import mpmath

from read_write_files import *

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


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
    try:
        n = len(sequence)
        ones_count = sequence.count("1")
        share_of_unit = ones_count / n
        if abs(share_of_unit - 0.5) < (2 / math.sqrt(n)):
            v = 0
            for bit in range(n - 1):
                if sequence[bit] != sequence[bit + 1]:
                    v += 1
            numerator = abs(v - 2 * n * share_of_unit * (1 - share_of_unit))
            denominator = 2 * math.sqrt(2 * n) * share_of_unit * (1 - share_of_unit)
            p_v = math.erfc(numerator / denominator)
        else:
            p_v = 0
        write_file(txt_file_path, f'{key} : {p_v}\n')
    except Exception as e:
        print("Test for the same consecutive bits, ERROR:", e)


def longest_run_ones_test_nist(sequence: str, txt_file_path: str, key: str) -> None:
    """
        Perform frequency test based on NIST guidelines

        Parameters:
        sequence (str): String of bits to be tested.
        txt_file_path (str): Path to the text file where results will be written.
        key (str): A key indicating which language the sequence was generated in

        Returns:
        None
    """
    try:
        n = len(sequence)
        m = 8
        blocks = [sequence[i:i + m] for i in range(0, n, m)]
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            max_count = 0
            count = 0
            for bit in block:
                count = count + 1 if bit == "1" else 0
                max_count = max(max_count, count)
            match max_count:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case _:
                    v[4] += 1
        xi_square = 0
        for i in range(4):
            xi_square += pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        p_v = mpmath.gammainc(3 / 2, xi_square / 2)
        write_file(txt_file_path, f'{key} : {p_v}\n')
    except Exception as e:
        print("Test for the longest sequence of ones in the block, ERROR:", e)
