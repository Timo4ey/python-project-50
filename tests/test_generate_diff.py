import pytest
from gendiff.generate_diff import get_value_from_two_dicts, generate_diff
from gendiff.scripts.gendiff import command
import os
import subprocess
import yaml
import json
def fixture_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(current_dir + '/fixtures/' + file_path)
    return path_to_file


def files_loader(path):
    the_file = fixture_path(path)
    files = open(the_file, 'r')
    list_if_files = files.read().rstrip().split('\n\n\n\n')
    return list_if_files


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



def test_get_value_from_two_dicts():
    assert get_value_from_two_dicts('a', {'a': 1}, {'a': 2}) == (1, 2)
    assert get_value_from_two_dicts('a', {'a': False}, {'a': 2}) == (False, 2)
    assert get_value_from_two_dicts('a', {'a': 1}, {'a': True}) == (1, True)
    assert get_value_from_two_dicts('a', {'a': False}, {'a': True}) == (False, True)
    assert get_value_from_two_dicts('a', {'a': None}, {'a': True}) == (None, True)


def test_json():
    jsn_files = json_loader(files_loader('jsons.txt'))
    answers = files_loader('answers.txt')
    for i, v in zip(range(0, len(jsn_files) - 1, 2), answers):
        assert generate_diff(jsn_files[i], jsn_files[i + 1]) == v


def test_yaml():
    jsn_files = yaml_loader(files_loader('yamls.txt'))
    answers = files_loader('answers.txt')
    for i, v in zip(range(0, len(jsn_files) - 1, 2), answers):
        assert generate_diff(jsn_files[i], jsn_files[i + 1]) == v


