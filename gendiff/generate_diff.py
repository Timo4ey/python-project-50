import itertools
from gendiff.prepare_data.prepare_data import (prepare_data, serialize_output)
from gendiff.scripts.checkers.checkers import check_values_forms
from gendiff.scripts.compare_data.compare_data import compare_two_values


def dif(first_dict: dict, second_dict: dict, depth=0, replacer=' ') -> str:
    output = []

    deep_size = depth + 1
    space_filler = deep_size * replacer
    current_feeler = replacer * depth

    set_of_unique_keys = check_values_forms(first_dict, second_dict)
    for k in set_of_unique_keys:
        key, key2 = first_dict.get(k, type), second_dict.get(k, type)

        output.extend(compare_two_values(space_filler, k, key, key2))
    outcome = itertools.chain("{", output, [current_feeler + "}"])
    return serialize_output('\n'.join(outcome))


def generate_diff(dictionary_1: dict, dictionary_2: dict) -> str:
    return dif(dictionary_1, dictionary_2).strip('\n')


if __name__ == '__main__':

    data = prepare_data("test_1_file1.json", "test_1_file2.json")
    file1, file2 = data
    out = generate_diff(file1, file2)
    with open("../tests/fixtures/json_tests/test1_plain_json.txt", 'r') as f:
        answer = f.read()
    print(out)
