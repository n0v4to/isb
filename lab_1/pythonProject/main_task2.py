from decrypt_text import *
from frequency_analysis import *
from read_write_files import *


if __name__ == "__main__":
    text = read_file("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_2/cod4.txt")
    # frequency_analysis(text)
    # frequency = read_json_task_2("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_2/frequencies.json")
    # alphabet = read_json_task_2("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_2/data.json")
    # compare_frequencies(frequency, alphabet)

    key = read_json_task_2("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_2/decryption_key.json")
    decrypt_task_2(text, key)
