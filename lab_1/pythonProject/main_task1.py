from read_write_files import *
from text_encoding import *


if __name__ == "__main__":
    path = "D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_1/key.json"
    info = [2, 1, 4, 5, 3]
    write_json(path, info)

    text = read_file("/texts/task_1/text1.txt")
    permutation = read_json("D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_1/key.json")
    print(permutation)
    encrypted_text = encrypt(text, permutation)
    decrypted_text = decrypt(encrypted_text, permutation)

    path_encrypted_text = "D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_1/encrypted_text.txt"
    path_decrypted_text = "D:/Code/3sem/isb/isb/lab_1/pythonProject/texts/task_1/decrypted_text.txt"
    write_file(path_encrypted_text, encrypted_text)
    # write_file(path_decrypted_text, decrypted_text)
