import pytest
from gendiff.generate_diff import find_files, check_bool, get_value_from_two_dicts, generate_diff
from gendiff.scripts.gendiff import command
import os
import subprocess


def test_check_bool():
    assert check_bool(True) == 'true'
    assert check_bool(False) == 'false'
    assert check_bool(0) == 0
    assert check_bool([]) == []
    assert check_bool(1) == 1


def test_get_value_from_two_dicts():
    assert get_value_from_two_dicts('a', {'a': 1}, {'a': 2}) == (1, 2)
    assert get_value_from_two_dicts('a', {'a': False}, {'a': 2}) == ('false', 2)
    assert get_value_from_two_dicts('a', {'a': 1}, {'a': True}) == (1, 'true')
    assert get_value_from_two_dicts('a', {'a': False}, {'a': True}) == ('false', 'true')
    assert get_value_from_two_dicts('a', {'a': None}, {'a': True}) == ('null', 'true')


def test_generate_diff():
    # test 1
    directory = os.path.abspath('tests/fixtures/test1_plain_json.txt')
    file1 = os.path.abspath('tests/fixtures/test_1_file1.json')
    file2 = os.path.abspath('tests/fixtures/test_1_file2.json')
    with open(directory, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 2
    directory1 = os.path.abspath('tests/fixtures/test2_plain_json.txt')
    file3 = os.path.abspath('tests/fixtures/test_2_file1.json')
    file4 = os.path.abspath('tests/fixtures/test_2_file2.json')
    with open(directory1, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 3
    directory2 = os.path.abspath('tests/fixtures/test3_positive_file5.txt')
    file3 = os.path.abspath('tests/fixtures/test_3_positive.json')
    file4 = os.path.abspath('tests/fixtures/test_3_positive.json')
    with open(directory2, 'r') as f:
        assert generate_diff(file3, file4) == f.read()
    # test 5
    directory3 = os.path.abspath('tests/fixtures/test4_empty_full.txt')
    file1 = os.path.abspath('tests/fixtures/test_4_empty_file1.json')
    file2 = os.path.abspath('tests/fixtures/test_4_file2.json')
    with open(directory3, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory4 = os.path.abspath('tests/fixtures/test4_full_empty.txt')
    file1 = os.path.abspath('tests/fixtures/test_4_file2.json')
    file2 = os.path.abspath('tests/fixtures/test_4_empty_file1.json')
    with open(directory4, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
    # test 6
    directory5 = os.path.abspath('tests/fixtures/test7_empty_empty.txt')
    file1 = os.path.abspath('tests/fixtures/test_4_empty_file1.json')
    file2 = os.path.abspath('tests/fixtures/test_4_empty_file1.json')
    with open(directory5, 'r') as f:
        assert generate_diff(file1, file2) == f.read()


def test_command():
    execute = subprocess.getoutput("poetry run gendiff -f plain tests/fixtures/test_1_file1.json tests/fixtures/test_1_file2.json")
    directory = os.path.abspath('tests/fixtures/test1_plain_json.txt')
    with open(directory, 'r') as f:
        assert execute == f.read()



