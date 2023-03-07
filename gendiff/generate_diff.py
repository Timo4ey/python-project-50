from gendiff.prepare_data.prepare_data import (prepare_data,
                                               serialize_output
                                               )


def get_value_from_two_dicts(key, first_file, second_file):
    return first_file.get(key, type), second_file.get(key, type)


def generate_diff(file_path1, file_path2) -> str:
    first_file, second_file, keys = prepare_data(file_path1, file_path2)
    frame = '\n  {} {}: {}'
    if not first_file and not second_file:
        return f'{first_file}'

    def dif(first_dict, second_dict, key):
        output = ""
        for k in key:
            key, key2 = get_value_from_two_dicts(k, first_dict, second_dict)
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
