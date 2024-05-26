import argparse
import json
import sys

from asymmetric import *
from symmetric import *
from read_write_file import *


def menu():
    setting = read_json("settings.json")
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Starts the key generation mode')
    group.add_argument('-enc', '--encryption', help='Starts the encryption mode')
    group.add_argument('-dec', '--decryption', help='Starts the decryption mode')
    group.add_argument('-enc_sym', '--encryption_symmetric', help='Starts symmetric key encryption mode')
    group.add_argument('-dec_sym', '--decryption_symmetric', help='Starts symmetric key decryption mode')
    parser.add_argument("setting", type=str, help="Path to the json file with the settings")

    args = parser.parse_args()

    sym = Symmetric()
    asym = Asymmetric()

    match args:
        case args if args.generation:
            key_length = int(input("Введите длину ключа в битах, в диапазоне [40, 128], шаг 8: "))
            print(f"(*≧ω≦) Выбрана длина ключа: {key_length} бит")
            asym.generate_keys()
            print("٩(◕‿◕｡) Созданы асимметричные ключи")
            asym.serialization_public(setting["public_key"])
            print(f"(＾_＾） Публичный ключ сериализован в {setting['public_key']}")
            asym.serialization_private(setting["private_key"])
            print(f"(＾_＾） Приватный ключ сериализован в {setting['private_key']}")
            sym.key_generation(key_length)
            print("(⌐■_■) Сгенерирован симметричный ключ")
            sym.key_serialization(setting["symmetric_key"])
            print(f"(⌐■_■) Симметричный ключ сериализован в {setting['symmetric_key']}")
        case args if args.encryption:
            sym.key_deserialization(setting["symmetric_key"])
            print(f"(¬‿¬) Симметричный ключ десериализован из {setting['symmetric_key']}")
            sym.encrypt(setting["initial_file"], setting["encrypted_file"])
            print(f"(¬‿¬) Файл {setting['initial_file']} зашифрован в {setting['encrypted_file']}")
        case args if args.decryption:
            sym.key_deserialization(setting["symmetric_key"])
            print(f"(¬‿¬) Симметричный ключ десериализован из {setting['symmetric_key']}")
            sym.decrypt(setting["encrypted_file"], setting["decrypted_file"])
            print(f"(¬‿¬) Файл {setting['encrypted_file']} расшифрован в {setting['decrypted_file']}")
        case args if args.encryption_symmetric:
            sym.key_deserialization(setting["symmetric_key"])
            print(f"(¬‿¬) Симметричный ключ десериализован из {setting['symmetric_key']}")
            asym.public_key_deserialization(setting["public_key"])
            print(f"(＾_＾） Публичный ключ десериализован из {setting['public_key']}")
            symmetric_key = sym.key
            encrypted_symmetric_key = asym.encrypt(symmetric_key)
            print("٩(◕‿◕｡) Симметричный ключ зашифрован публичным ключом")
            write_bytes_text(setting["encrypted_symmetric_key"], encrypted_symmetric_key)
            print(f"(¬‿¬) Зашифрованный симметричный ключ записан в {setting['encrypted_symmetric_key']}")
        case args if args.decryption_symmetric:
            sym.key_deserialization(setting["symmetric_key"])
            print(f"(¬‿¬) Симметричный ключ десериализован из {setting['symmetric_key']}")
            asym.private_key_deserialization(setting["private_key"])
            print(f"(＾_＾） Приватный ключ десериализован из {setting['private_key']}")
            encrypted_symmetric_key = read_bytes(setting["encrypted_symmetric_key"])
            print(f"(¬‿¬) Зашифрованный симметричный ключ считан из {setting['encrypted_symmetric_key']}")
            decrypted_symmetric_key = asym.decrypt(encrypted_symmetric_key)
            print("٩(◕‿◕｡) Симметричный ключ расшифрован приватным ключом")
            sym.key_serialization(setting["decrypted_symmetric_key"])
            print(f"(⌐■_■) Расшифрованный симметричный ключ сериализован в {setting['decrypted_symmetric_key']}")
            return decrypted_symmetric_key

if __name__ == "__main__":
    menu()


