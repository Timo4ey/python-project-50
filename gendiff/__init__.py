from gendiff.prepare_data.prepare_data import prepare_data
from gendiff.scripts.stylish.stylish import stylish


def generate_diff(dictionary_1: dict, dictionary_2: dict) -> str:
    file1 = prepare_data(dictionary_1, dictionary_2)
    file2 = prepare_data(dictionary_1, dictionary_2)
    return stylish(file1, file2).strip('\n')
