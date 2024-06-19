import json


def write_file(path: str, info: str) -> None:
    """The function of writing information to a file
    Args:
      path: the path to the file
      info: information written to file
    """
    try:
        with open(path, "w", encoding='UTF-8') as file:
            json.dump({"card_number":  info}, file)
    except Exception as e:
        print(f"Непредвиденная ошибка: {str(e)}")


def read_json(path: str) -> dict:
    """The function of reading data from a json file
    Args:
      path: the path to the file
    Returns:
      Dictionary with json file structure
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка! Файл {path} не найден.")
    except Exception as e:
        print(f"Непредвиденная ошибка: {str(e)}")
