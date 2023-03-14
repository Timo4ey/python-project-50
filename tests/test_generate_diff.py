from gendiff.generate_diff import generate_diff
from gendiff.prepare_data.prepare_data import prepare_data
from gendiff.prepare_data.prepare_data import json_loader, yaml_loader, find_files, check_type_of_file, \
    download_two_json_files, download_two_yml_files, handle_load_files, serialize_output
import os


simple_dict = ({'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50},
               {'host': 'hexlet.io', 'timeout': 20, 'verbose': True})

def fixture_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(current_dir + '/fixtures/' + file_path)
    return path_to_file


def files_loader(path):
    the_file = fixture_path(path)
    files = open(the_file, 'r')
    list_if_files = files.read().rstrip().split('\n\n\n\n')
    return list_if_files


def test_generate_diff_json():
    jsn_files = json_loader(files_loader('jsons.txt'))
    answers = files_loader('answers.txt')
    for i, v in zip(range(0, len(jsn_files) - 1, 2), answers):
        assert generate_diff(jsn_files[i], jsn_files[i + 1]) == v


def test_generate_diff_yaml():
    jsn_files = yaml_loader(files_loader('yamls.txt'))
    answers = files_loader('answers.txt')
    for i, v in zip(range(0, len(jsn_files) - 1, 2), answers):
        assert generate_diff(jsn_files[i], jsn_files[i + 1]) == v


def test_find_files():
    file1 = '/home/timofey/Desktop/workspace/pythonProject/difference_calculator/python-project-50/tests/fixtures/json_tests/test_5_recurs_file1.json'
    file2 = '/home/timofey/Desktop/workspace/pythonProject/difference_calculator/python-project-50/tests/fixtures/json_tests/test_5_recurs_file2.json'
    answer = (file1, file2)
    result = find_files('test_5_recurs_file1.json', 'test_5_recurs_file2.json')
    assert result == answer, "Paths are not equal"


def test_check_type_of_file():
    result = check_type_of_file('test_5_recurs_file1.json', 'test_5_recurs_file2.json',)
    answer = ('json', 'json')
    assert result == answer
    result = check_type_of_file('test_5_recurs_file1.json', 'test_1_yaml_file1.yml',)
    answer = ('json', 'yml')
    assert result == answer
    result = check_type_of_file('test_1_yaml_file1.yml', 'test_1_yaml_file1.yml',)
    answer = ('yml', 'yml')
    assert result == answer


def test_download_two_json_files():
    result = download_two_json_files('tests/fixtures/json_tests/test_1_file1.json',
                                     'tests/fixtures/json_tests/test_1_file2.json')
    answer = ({'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50},
              {'host': 'hexlet.io', 'timeout': 20, 'verbose': True})
    assert result == answer


def test_download_two_yml_files():
    result = download_two_yml_files('tests/fixtures/yml_tests/test_1_yaml_file1.yml',
                                    'tests/fixtures/yml_tests/test_1_yaml_file2.yml')
    answer = simple_dict
    assert result == answer


def test_handle_load_files():
    result = handle_load_files('json').__name__
    answer = 'download_two_json_files'
    assert result == answer
    result = handle_load_files('yml').__name__
    answer = 'download_two_yml_files'
    assert result == answer


def test_serialize_output():
    result = serialize_output('True')
    answer = 'true'
    assert result == answer
    result = serialize_output('False')
    answer = 'false'
    assert result == answer
    result = serialize_output('None')
    answer = 'null'
    assert result == answer


def test_prepare_data():
    result = prepare_data('test_1_file1.json', 'test_1_file2.json')
    answer = simple_dict
    assert result == answer
