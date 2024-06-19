import hashlib
import multiprocessing as mp
import time
import work_with_file

from matplotlib import pyplot as plt
from tqdm import tqdm


def check_number(part: int, bins: list, last_digit: int, original_hash: str) -> str:
    """
        Checks a card number based on the specified conditions.

        Args:
        part (int): A part of the card number.
        bins (list): List of card number prefixes.
        last_digit (int): The last digit of the card number.
        original_hash (str): The hash to compare against.

        Returns:
        str: The found card number that matches the hash. Returns None if nothing is found.
    """
    for card_bin in bins:
        card_number = f"{card_bin}{str(part).zfill(6)}{last_digit}"
        if hashlib.sha1(card_number.encode()).hexdigest() == original_hash:
            return card_number


def get_number(original_hash: str, bins: list, last_digit: int, count_process: int = mp.cpu_count()) -> str:
    """
        Finds a card number that matches the original hash using multiprocessing.

        Args:
        original_hash (str): The original hash to match against.
        bins (list): List of card number prefixes.
        last_digit (int): The last digit of the card number.
        count_process (int): Number of processes to use for multiprocessing (default is CPU count).

        Returns:
        str: The found card number that matches the hash. Returns None if nothing is found.
    """
    with mp.Pool(count_process) as p:
        for result in p.starmap(check_number,
                                [(i, bins, last_digit, original_hash) for i in list(range(0, 999999))]):
            if result:
                print(f"The number of the selected card with the number of processes = {count_process} : {result}")
                p.terminate()
                return result
