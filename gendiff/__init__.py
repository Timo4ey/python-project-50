from gendiff.scripts.stylish.stylish import stylish


def generate_diff(dictionary_1: dict, dictionary_2: dict) -> str:
    return stylish(dictionary_1, dictionary_2).strip('\n')
