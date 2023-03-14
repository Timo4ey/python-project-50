import itertools
from gendiff.prepare_data.prepare_data import (prepare_data,
                                               serialize_output)
from gendiff.scripts.checkers.checkers import check_values_forms
from gendiff.scripts.compare_data.compare_data import compare_two_values, compare_two_dicts


def dif(first_dict: dict, second_dict: dict, depth=0, replacer=' ') -> str:
    output = []

    deep_size = depth + 1
    space_feeler = deep_size * replacer
    current_feeler = replacer * depth

    set_of_unique_keys = check_values_forms(first_dict, second_dict)
    for k in set_of_unique_keys:
        key, key2 = first_dict.get(k, type), second_dict.get(k, type)

        output.extend(compare_two_values(space_feeler, k, key, key2))
        output.extend(compare_two_dicts(space_feeler, k, key, key2,
                                        depth=deep_size))

    outcome = itertools.chain("{", output, [current_feeler + "}"])
    return serialize_output('\n'.join(outcome))


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
