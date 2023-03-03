import pytest
from gendiff.generate_diff import find_files, check_bool, get_value_from_two_dicts, generate_diff
import os


# def test_find_files():
#     path1 = '../files/'
#     path2 = '../.github/workflows/'
#     assert find_files(path1) == ['../files/file1.json', '../files/file2.json']
#     assert find_files(path2) == ['../.github/workflows/README.md', '../.github/workflows/hexlet-check.yml']


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


def test_generate_diff():
    directory = os.path.abspath('tests/test1_plain_json.txt')
    file1 = os.path.abspath('./files/file1.json')
    file2 = os.path.abspath('./files/file2.json')
    with open(directory, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
