import pytest
from gendiff.generate_diff import get_value_from_two_dicts, generate_diff
from gendiff.scripts.gendiff import command
import os
import subprocess


def test_get_value_from_two_dicts():
    assert get_value_from_two_dicts('a', {'a': 1}, {'a': 2}) == (1, 2)
    assert get_value_from_two_dicts('a', {'a': False}, {'a': 2}) == (False, 2)
    assert get_value_from_two_dicts('a', {'a': 1}, {'a': True}) == (1, True)
    assert get_value_from_two_dicts('a', {'a': False}, {'a': True}) == (False, True)
    assert get_value_from_two_dicts('a', {'a': None}, {'a': True}) == (None, True)


def test_generate_diff_json():
    # test 1
    directory = os.path.abspath('tests/fixtures/json_tests/test1_plain_json.txt')
    file1 = os.path.abspath('tests/fixtures/json_tests/test_1_file1.json')
    file2 = os.path.abspath('tests/fixtures/json_tests/test_1_file2.json')
    with open(directory, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 2
    directory1 = os.path.abspath('tests/fixtures/json_tests/test2_plain_json.txt')
    file3 = os.path.abspath('tests/fixtures/json_tests/test_2_file1.json')
    file4 = os.path.abspath('tests/fixtures/json_tests/test_2_file2.json')
    with open(directory1, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 3
    directory2 = os.path.abspath('tests/fixtures/json_tests/test3_positive_file5.txt')
    file3 = os.path.abspath('tests/fixtures/json_tests/test_3_positive.json')
    file4 = os.path.abspath('tests/fixtures/json_tests/test_3_positive.json')
    with open(directory2, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 5
    directory3 = os.path.abspath('tests/fixtures/json_tests/test4_empty_full.txt')
    file1 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    file2 = os.path.abspath('tests/fixtures/json_tests/test_4_file2.json')
    with open(directory3, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory4 = os.path.abspath('tests/fixtures/json_tests/test4_full_empty.txt')
    file1 = os.path.abspath('tests/fixtures/json_tests/test_4_file2.json')
    file2 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    with open(directory4, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory5 = os.path.abspath('tests/fixtures/json_tests/test7_empty_empty.txt')
    file1 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    file2 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    with open(directory5, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    directory1 = os.path.abspath('tests/fixtures/json_tests/test2_plain_json.txt')
    file3 = os.path.abspath('tests/fixtures/json_tests/test_2_file1.json')
    file4 = os.path.abspath('tests/fixtures/json_tests/test_2_file2.json')
    with open(directory1, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 3
    directory2 = os.path.abspath('tests/fixtures/json_tests/test3_positive_file5.txt')
    file3 = os.path.abspath('tests/fixtures/json_tests/test_3_positive.json')
    file4 = os.path.abspath('tests/fixtures/json_tests/test_3_positive.json')
    with open(directory2, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 5
    directory3 = os.path.abspath('tests/fixtures/json_tests/test4_empty_full.txt')
    file1 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    file2 = os.path.abspath('tests/fixtures/json_tests/test_4_file2.json')
    with open(directory3, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory4 = os.path.abspath('tests/fixtures/json_tests/test4_full_empty.txt')
    file1 = os.path.abspath('tests/fixtures/json_tests/test_4_file2.json')
    file2 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    with open(directory4, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory5 = os.path.abspath('tests/fixtures/json_tests/test7_empty_empty.txt')
    file1 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    file2 = os.path.abspath('tests/fixtures/json_tests/test_4_empty_file1.json')
    with open(directory5, 'r') as f:
        assert generate_diff(file1, file2) == f.read()

def test_generate_diff_yml():
    directory = os.path.abspath('tests/fixtures/json_tests/test1_plain_json.txt')
    file1 = os.path.abspath('tests/fixtures/yml_tests/test_1_yaml_file1.yml')
    file2 = os.path.abspath('tests/fixtures/yml_tests/test_1_yaml_file2.yml')
    with open(directory, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    directory1 = os.path.abspath('tests/fixtures/json_tests/test2_plain_json.txt')
    file3 = os.path.abspath('tests/fixtures/yml_tests/test_2_yaml_file1.yml')
    file4 = os.path.abspath('tests/fixtures/yml_tests/test_2_yaml_file2.yml')
    with open(directory1, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 3
    directory2 = os.path.abspath('tests/fixtures/json_tests/test3_positive_file5.txt')
    file3 = os.path.abspath('tests/fixtures/yml_tests/test_3_yaml_file1.yml')
    file4 = os.path.abspath('tests/fixtures/yml_tests/test_3_yaml_file2.yml')
    with open(directory2, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 5
    directory3 = os.path.abspath('tests/fixtures/json_tests/test4_empty_full.txt')
    file1 = os.path.abspath('tests/fixtures/yml_tests/test_4_yaml_file1.yml')
    file2 = os.path.abspath('tests/fixtures/yml_tests/test_4_yaml_file2.yml')
    with open(directory3, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory4 = os.path.abspath('tests/fixtures/json_tests/test4_full_empty.txt')
    file1 = os.path.abspath('tests/fixtures/yml_tests/test_4_yaml_file2.yml')
    file2 = os.path.abspath('tests/fixtures/yml_tests/test_4_yaml_file1.yml')
    with open(directory4, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory5 = os.path.abspath('tests/fixtures/json_tests/test7_empty_empty.txt')
    file1 = os.path.abspath('tests/fixtures/yml_tests/test_4_yaml_file1.yml')
    file2 = os.path.abspath('tests/fixtures/yml_tests/test_4_yaml_file1.yml')
    with open(directory5, 'r') as f:
        assert generate_diff(file1, file2) == f.read()


def test_command():
    execute = subprocess.getoutput("poetry run gendiff -f plain tests/fixtures/json_tests/test_1_file1.json tests/fixtures/json_tests/test_1_file2.json")
    directory = os.path.abspath('tests/fixtures/json_tests/test1_plain_json.txt')
    with open(directory, 'r') as f:
        assert execute == f.read()



