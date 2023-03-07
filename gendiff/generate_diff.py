from gendiff.prepare_data.prepare_data import find_files, check_bool, prepare_data


def get_value_from_two_dicts(key, first_file, second_file):
    return check_bool(
        first_file.get(key, type)), check_bool(second_file.get(key, type))


def generate_diff(file_path1, file_path2) -> str:
    first_file, second_file, keys = prepare_data(file_path1, file_path2)
    output = '{'
    frame = '\n  {} {}: {}'
    for k in keys:
        key, key2 = get_value_from_two_dicts(k, first_file, second_file)
        if first_file.get(k) == second_file.get(k):
            output += frame.format(' ', k, key)
        else:
            output += frame.format('-', k, key) if \
                (key is not type) else ''
            output += frame.format('+', k, key2) if \
                (key2 is not type) else ''
    output += '\n}'

    if len(output) <= 3:
        return str(first_file)
    return output


if __name__ == '__main__':

    file1, file2 = find_files('../files/')
    diff = generate_diff(file1, file2)
    print(diff)
