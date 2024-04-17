import json


def read_file(path: str) -> str:
    """The function of reading text from a file
    Args:
      path: the path to the file
    Returns:
      text from the file
    """
    with open(path, "r", encoding='UTF-8') as file:
        text = file.read()
    return text


def write_file(path: str, info: str) -> None:
    """The function of writing information to a file
    Args:
      path: the path to the file
      info: information written to file
    """
    with open(path, "w", encoding='UTF-8') as file:
        file.write(info)


def read_json(path: str) -> dict:
    """The function of reading data from a json file
    Args:
      path: the path to the file
    Returns:
      Dictionary with json file structure
    """
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)


def write_json(path: str, info: dict) -> None:
    """The function for writing data to a json file
    Args:
      info: the data to be written to the file
      path: the path to the file
    """
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(info, file, ensure_ascii=False, indent=4)
