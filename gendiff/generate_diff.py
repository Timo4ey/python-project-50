import json
import os


def find_files(path='../files/'):
    _, _, files_dir = list(os.walk(path))[0]
    for indx in range(len(files_dir)):
        files_dir[indx] = f'{path}{files_dir[indx]}'
    return files_dir


def check_bool(predicate):
    encode_to_js = json.JSONEncoder().encode
    if type(predicate) is bool:
        return encode_to_js(predicate)
    return predicate


def find_paths_to_files(file_path1: json, file_path2: json) -> tuple:
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    return first_file, second_file


def generate_diff(file_path1: dict, file_path2: dict) -> str:
    first_file, second_file = find_paths_to_files(file_path1, file_path2)
    output = '{'
    frame = '\n  {} {}: {}'
    keys = list({*second_file.keys(), *first_file.keys()})
    keys.sort()
    for k in keys:
        key, key2 = check_bool(first_file.get(k)), \
            check_bool(second_file.get(k))
        if first_file.get(k) == second_file.get(k):
            output += frame.format(' ', k, key)
        elif (key is not None) and (key2 is None):
            output += frame.format('-', k, key)
        elif (key is None) and (key2 is not None):
            output += frame.format('+', k, key2)
        else:
            output += frame.format('-', k, key)
            output += frame.format('+', k, key2)
    output += '\n}'
    return output


if __name__ == '__main__':
    file2, file1 = find_files()
    diff = generate_diff(file1, file2)
    print(diff)
