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


def luhn_algorithm(card_number: str) -> bool:
    """
       Checks if a card number is valid using the Luhn algorithm.

       Args:
       card_number (str): The card number to be validated.

       Returns:
       bool: True if the card number is valid, False otherwise.
    """
    digits = [int(digit) for digit in reversed(card_number)]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = (digits[i] // 10) + (digits[i] % 10)
    return sum(digits) % 10 == 0


def graphing(original_hash: str, bins: list, last_digit: int) -> None:
    """
        Plots a graph of the execution time of the `get_number` function depending on the number of processes used.

        Args:
        original_hash: The hash value of the full card number to find a match for.
        bins: List of possible card number prefixes (BIN).
        last_digit: The last digit of the card number.
    """
    time_list = list()
    for count_process in tqdm(range(1, int(mp.cpu_count() * 1.5)), desc="Collision Search"):
        start_time = time.time()
        if get_number(original_hash, bins, last_digit, count_process):
            time_list.append(time.time() - start_time)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(range(1, int(mp.cpu_count() * 1.5)), time_list, color='#4CAF50', edgecolor='black', linewidth=1)
    ax.set_xlabel('Number of Processes')
    ax.set_ylabel('Time, s')
    ax.set_title("Execution Time Statistics")
    plt.show()


if __name__ == "__main__":
    setting = work_with_file.read_json("parameters_card.json")
    # number = work_with_file.read_json("card.json")
    # print(f'The card number is correct: {luhn_algorithm(number["card"])}')
    print(f'The card number is correct: {luhn_algorithm("2200700708409551")}')
    # graphing(setting["hash"], setting["bins"], setting["last_numbers"])
    get_number(setting["hash"], setting["bins"], setting["last_numbers"])
