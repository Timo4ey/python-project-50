import json
import os
import yaml


def find_files(path):
    directory = os.walk(os.path.abspath(path))
    files_dir = [f'{path}{x}' for x in list(directory)[0][-1][::-1]]
    return files_dir


def check_bool(predicate):
    encode_to_js = json.JSONEncoder().encode
    if type(predicate) is bool:
        return encode_to_js(predicate)
    if predicate is None:
        return encode_to_js(predicate)
    return predicate


def check_type_of_file(file_path1, file_path2):
    first_file_type = file_path1[file_path1.rfind('.') + 1:]
    second_file_type = file_path2[file_path2.rfind('.') + 1:]
    return first_file_type, second_file_type


def download_two_json_files(file_path1: json, file_path2: json) -> tuple:
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    return first_file, second_file


def download_two_yml_files(file_path1: yaml, file_path2: yaml):
    first_file = yaml.load(open(file_path1))
    second_file = yaml.load(open(file_path2))
    return first_file, second_file


def is_same_type(array):
    file1, file2 = array
    file1 = check_type_of_file(file1)
    file2 = check_type_of_file(file2)
    if file1 == file2:
        return True
    return False


def handler(file_path1, file_path2):
    rout = {
        "json": download_two_json_files,
    }
    files_types = check_type_of_file(file_path1, file_path2)
    first_file, _ = files_types
    if is_same_type(files_types):
        return rout.get(first_file, )(file_path1, file_path2)


def prepare_data(file_path1, file_path2):
    first_file, second_file = download_two_json_files(file_path1, file_path2)
    keys = list({*second_file.keys(), *first_file.keys()})
    keys.sort()
    return first_file, second_file, keys
