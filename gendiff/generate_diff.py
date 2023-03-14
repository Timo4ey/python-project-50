from gendiff.prepare_data.prepare_data import (prepare_data)
from gendiff.scripts.compare_data.compare_data import compare_engine


def dif(first_dict: dict, second_dict: dict) -> str:
    outcome = compare_engine(first_dict, second_dict)
    return outcome


def generate_diff(dictionary_1: dict, dictionary_2: dict) -> str:
    return dif(dictionary_1, dictionary_2)


if __name__ == '__main__':

    data = prepare_data("test_5_recurs_file1.json", "test_5_recurs_file2.json")
    file1, file2 = data
    out = generate_diff(file1, file2)
    with open("../tests/fixtures/json_tests/test_5_recurs.txt", 'r') as f:
        answer = f.read()
        print(answer == out)
    print(out)
