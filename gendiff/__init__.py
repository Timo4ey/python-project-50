from gendiff.gen_diff_simple import dif


def generate_diff(dictionary_1: dict, dictionary_2: dict) -> str:
    return dif(dictionary_1, dictionary_2).strip('\n')
