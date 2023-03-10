import json
import os
import yaml
from yaml import Loader


def find_files(file1, file2):
    file_type1, file_type2 = check_type_of_file(file1, file2)
    file_type1 = file_type1 if file_type1 in ('json', 'yml') else 'yml'
    file_type2 = file_type2 if file_type2 in ('json', 'yml') else 'yml'
    if file_type1 == file_type2:
        paths = {
            "json": './tests/fixtures/json_tests/',
            "yml": './tests/fixtures/yml_tests/'}
        path1 = os.path.abspath(paths.get(file_type1))
        directory = list(os.walk(path1))[0][2]
        if file1 in directory and file2 in directory:
            return f'{path1}/{file1}', f'{path1}/{file2}'


def check_type_of_file(file_path1, file_path2):
    first_file_type = file_path1[file_path1.rfind('.') + 1:]
    second_file_type = file_path2[file_path2.rfind('.') + 1:]
    return first_file_type, second_file_type


def download_two_json_files(file_path1: json, file_path2: json) -> tuple:
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    return first_file, second_file


def download_two_yml_files(file_path1: yaml, file_path2: yaml):
    first_file = yaml.load(open(file_path1), Loader=Loader)
    second_file = yaml.load(open(file_path2), Loader=Loader)
    return first_file, second_file


def is_same_type(file1, file2):
    if file1 == file2:
        return True
    raise TypeError("Files must be the same type")


def handle_load_files(file_path1):
    rout = {
        "json": download_two_json_files,
    }
    function = rout.get(file_path1, download_two_yml_files)
    return function


def serialize_output(string: str) -> str:
    output = string.replace('True', 'true')
    output = output.replace('False', 'false')
    output = output.replace('None', 'null')
    return output


def prepare_data(file_path1, file_path2):
    first_type, second_type = check_type_of_file(file_path1, file_path2)
    is_same_type(first_type, second_type)
    func = handle_load_files(first_type)
    js_path = "../tests/fixtures/json_tests/"
    # path1, path2 = find_files(file_path1, file_path2),
    first_file, second_file = func(js_path+file_path1, js_path+file_path2)
    # keys = list({*second_file.keys(), *first_file.keys()})
    # keys.sort()

    return first_file, second_file


def get_unique_keys(first_item, second_item):
    if isinstance(first_item, dict) and isinstance(second_item, dict):
        value = list({*first_item.keys(), *second_item.keys()})
    elif isinstance(first_item, dict) and not isinstance(second_item, dict):
        value = list({*first_item.keys(), second_item})
    elif isinstance(second_item, dict) and not isinstance(first_item, dict):
        value = list({*second_item.keys(), first_item})
    else:
        value = list({second_item, first_item})
    return value

