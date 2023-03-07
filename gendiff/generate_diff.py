from gendiff.prepare_data.prepare_data import (prepare_data,
                                               serialize_output,
                                               get_unique_keys
                                               )


def get_value_from_two_dicts(key, first_file, second_file):
    return first_file.get(key, type), second_file.get(key, type)


def generate_diff(file_path1, file_path2) -> str:
    first_file, second_file, keys = prepare_data(file_path1, file_path2)
    frame = '\n  {} {}: {}'
    if not first_file and not second_file:
        return f'{first_file}'

    def dif(first_dict, second_dict, keys2):
        output = ""
        if len(keys2) == 0:
            return output
        for k in keys2:
            key, key2 = get_value_from_two_dicts(k, first_dict, second_dict)
            if isinstance(key, dict):
                new_keys = get_unique_keys(key, key2)
                output += dif(key, key2, new_keys)
            if first_dict.get(k) == second_dict.get(k):
                output += frame.format(' ', k, key)
            else:
                output += frame.format('-', k, key) if \
                    (key is not type) else ''
                output += frame.format('+', k, key2) if \
                    (key2 is not type) else ''
        output = serialize_output(output)
        return output
    return f'{"{"}{dif(first_file, second_file, keys)}\n{"}"}'



if __name__ == "__main__":
    a = "/home/timofey/Desktop/workspace/pythonProject/difference_calculator/python-project-50/tests/fixtures/json_tests/test_6_recurs_file1.json"
    b = "/home/timofey/Desktop/workspace/pythonProject/difference_calculator/python-project-50/tests/fixtures/json_tests/test_6_recurs_file2.json"
    g = generate_diff(a, b)
    print(g)