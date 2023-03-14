import json
import os
import yaml
from yaml import Loader

from gendiff.scripts.checkers.checkers import is_same_type, is_dict


def find_files(file1, file2):
    file_type1, file_type2 = check_type_of_file(file1, file2)
    file_type1 = file_type1 if file_type1 in ('json', 'yml') else 'yml'
    file_type2 = file_type2 if file_type2 in ('json', 'yml') else 'yml'
    if file_type1 == file_type2:
        paths = {
            "json": '/tests/fixtures/json_tests',
            "yml": '/tests/fixtures/yml_tests'}
        path = os.path.abspath(__file__)
        main_dir = path.rfind('/gendiff')
        files_dir = paths.get(file_type1)
        path = path[:main_dir] + files_dir if main_dir != -1 else path
        return f'{path}/{file1}', f'{path}/{file2}'


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
    first_path, second_path = find_files(file_path1, file_path2)
    first_file, second_file = func(first_path, second_path)

    return first_file, second_file


def convert_data_to_dict(file_path1: str, file_path2: str):
    first_file = second_file = 0
    dict_predicate = is_dict(file_path1)
    if not dict_predicate:
        first_file, second_file = prepare_data(file_path1, file_path2)
    elif dict_predicate:
        first_file, second_file = file_path1, file_path2
    return first_file, second_file


def json_loader(array):
    output = []
    for jsn in array:
        output.append(json.loads(jsn))
    return output


def yaml_loader(array):
    output = []
    for yml in array:
        output.append(yaml.load(yml, yaml.Loader))
    return output
