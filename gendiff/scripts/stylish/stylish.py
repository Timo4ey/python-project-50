from gendiff.prepare_data.prepare_data import (prepare_data)
from gendiff.scripts.compare_data.compare_data import compare_engine


def stylish(first_dict: dict, second_dict: dict) -> str:
    outcome = compare_engine(first_dict, second_dict)
    return outcome
