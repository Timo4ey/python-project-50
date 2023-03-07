import json
import os
import yaml
from yaml import Loader


def find_files(path):
    directory = os.walk(os.path.abspath(path))
    files_dir = [f'{path}{x}' for x in list(directory)[0][-1][::-1]]
    return files_dir


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

    first_file, second_file = func(file_path1, file_path2)
    keys = list({*second_file.keys(), *first_file.keys()})
    keys.sort()

    return first_file, second_file, keys
