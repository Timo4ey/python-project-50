from gendiff.prepare_data.prepare_data import prepare_data
from gendiff.prepare_data.prepare_data import json_loader, yaml_loader, find_files, check_type_of_file, \
    download_two_json_files, download_two_yml_files, handle_load_files, serialize_output
import os

from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.json_format.json_format import json_format
from gendiff.scripts.plain.plain import plain
from gendiff.scripts.stylish import stylish

simple_dict = ({'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22', 'timeout': 50},
               {'host': 'hexlet.io', 'timeout': 20, 'verbose': True})


def fixture_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_file = os.path.join(current_dir + '/fixtures/' + file_path)
    return path_to_file


def files_reader(path):
    with open(path, 'r') as f:
        response = f.read()
    return response


def files_loader(path):
    list_if_files = path.rstrip().split('\n\n\n\n')
    return list_if_files


# def test_stylish_2():
#     path1 = "tests/tests_2/fixtures/file1.json"
#     path2 = "tests/tests_2/fixtures/file2.json"
#     file1, file2 = prepare_data(path1, path2)
#     result = generate_diff(file1, file2)
#     answer = files_loader(files_reader("tests/tests_2/fixtures/result_stylish"))
#     assert result == answer


def test_generate_diff_json():

    jsn_files = json_loader(files_loader(files_reader('tests/fixtures/answers/jsons.txt')))
    print("jsn_files!!!!",jsn_files)
    answers = files_loader(files_reader('tests/fixtures/answers/answers.txt'))
    # print("answers!!!", answers)
    for i, v in zip(range(0, len(jsn_files) - 1, 2), answers):
        assert generate_diff(jsn_files[i], jsn_files[i + 1]) == v


def test_generate_diff_yaml():
    jsn_files = yaml_loader(files_loader(files_reader('tests/fixtures/answers/yamls.txt')))
    answers = files_loader(files_reader('tests/fixtures/answers/answers.txt'))
    for i, v in zip(range(0, len(jsn_files) - 1, 2), answers):
        assert generate_diff(jsn_files[i], jsn_files[i + 1]) == v


def test_stylish_json():
    file1, file2 = prepare_data("test_5_recurs_file1.json", "test_5_recurs_file2.json")
    result = stylish(file1, file2)
    answer = files_reader('tests/fixtures/answers/test_5_recurs')
    assert result == answer


def test_stylish_yml():
    file1, file2 = prepare_data("test_5_yaml_file1.yml", "test_5_yaml_file2.yml")
    result = stylish(file1, file2)
    answer = files_reader('tests/fixtures/answers/test_5_recurs')
    assert result == answer


def test_plain_json_recurse():
    file1, file2 = prepare_data("test_5_recurs_file1.json", "test_5_recurs_file2.json")
    result = plain(file1, file2)
    answer = files_reader('tests/fixtures/answers/plain_flat_test1.txt')
    assert result == answer


def test_plain_flat_files():
    jsn_files = yaml_loader(files_loader(files_reader('tests/fixtures/answers/answers_flat.txt')))
    answers = files_loader(files_reader('tests/fixtures/answers/answer_plain_test1.txt'))
    for i, v in zip(range(0, len(jsn_files) - 1, 2), answers):
        assert plain(jsn_files[i], jsn_files[i + 1]) == v


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


def test_json_format():
    import json
    file1, file2 = prepare_data("test_1_file1.json", "test_1_file2.json")
    result = json_format(file1, file2)
    with open("tests/fixtures/answers/jsnon_test1_answer.json", 'r') as f:
        answer = json.dumps(json.loads(f.read()), indent=2)
    assert result == answer

