import itertools
from gendiff.prepare_data.prepare_data import (prepare_data,
                                               serialize_output)


def check_values_forms(first_values, second_values):
    set_of_unique_keys = None
    if is_dict(first_values) and is_dict(second_values):
        set_of_unique_keys = getting_unique_keys(first_values, second_values)
    if is_dict(first_values) and is_dict(second_values) is False:
        set_of_unique_keys = getting_unique_keys(first_values)
        second_values = {}
    if is_dict(first_values) is False and is_dict(second_values):
        set_of_unique_keys = getting_unique_keys(second_values)
        first_values = {}
    return set_of_unique_keys


def getting_unique_keys(*args: dict) -> list:
    output = []
    filtered = list(filter(lambda x: not isinstance(x,
                                                    type | None | int), args))
    [output.append(j) for d in filtered for j in d]
    output = set(output)
    output = list(output)
    output.sort()
    return output


def get_data(file_path1, file_path2):
    first_file = second_file = 0
    dict_predicate = is_dict(file_path1)
    if not dict_predicate:
        first_file, second_file = prepare_data(file_path1, file_path2)
    elif dict_predicate:
        first_file, second_file = file_path1, file_path2
    return first_file, second_file


def is_dict(array) -> bool:
    return isinstance(array, dict)


def convert_to_format(space_feeler: str, symbol: str, key: str | int,
                      value) -> list[str]:
    return [''.join([space_feeler, f' {symbol}', f' {key}:', f' {value}']
                    ).rstrip(' ')]


def compare_two_values(space_feeler, key, value_1, value_2):
    if dict not in (type(value_1), type(value_2)):
        if value_1 == value_2 \
                and type(value_1) not in (dict, type):

            return convert_to_format(space_feeler, ' ', key, value_1)

        elif value_1 != value_2 and \
                type(value_1) is not type and \
                type(value_2) is not type:
            return [*convert_to_format(space_feeler, '-', key, value_1),
                    *convert_to_format(space_feeler, '+', key, value_2)]

        elif value_1 != value_2 and \
                type(value_1) is not type and \
                type(value_2) is type:
            return convert_to_format(space_feeler, '-', key, value_1)

        elif value_1 != value_2 and \
                type(value_1) is type and \
                type(value_2) is not type:
            return convert_to_format(space_feeler, '+', key, value_2)
    return []


def is_dicts_equals(key, value_1, value_2) -> bool:
    if dict in (type(value_1), type(value_2)):
        if value_1 == value_2 and type(key) is dict \
                and type(value_2) is dict:
            return True
        return False


def is_both_dicts_not_equal(value_1, value_2) -> bool:
    if dict in (type(value_1), type(value_2)):
        if value_1 != value_2 and \
                type(value_1) is dict and\
                type(value_2) is dict:
            return True
        return False


def is_only_first_value_dict(value_1, value_2):
    if dict in (type(value_1), type(value_2)):
        if value_1 != value_2 and \
                type(value_1) is dict and \
                type(value_2) is type:
            return True
        return False


def is_only_second_value_dict(value_1, value_2):
    if dict in (type(value_1), type(value_2)):
        if value_1 != value_2 and \
                type(value_1) is type and \
                type(value_2) is dict:
            return True
    return False


def is_first_dict_second_value(value_1, value_2):
    if dict in (type(value_1), type(value_2)):
        if value_1 != value_2 and type(
                value_1) is dict and type(value_2) is not dict:
            return True
    return False


def compare_two_dicts(space_feeler, key, value_1, value_2, depth=0):
    next_depth = 3
    next_depth = depth + next_depth
    # 1
    if is_dicts_equals(key, value_1, value_2):
        return convert_to_format(space_feeler, ' ', key, dif(
            value_1, value_2, depth=next_depth))
    # 2
    if is_both_dicts_not_equal(value_1, value_2):
        return convert_to_format(space_feeler, ' ', key, dif(
            value_1, value_2, depth=next_depth))
    # 3
    if is_only_first_value_dict(value_1, value_2):
        return convert_to_format(space_feeler, '-', key, stringify(
            array=value_1, space_count=next_depth))
    # 4
    if is_only_second_value_dict(value_1, value_2):
        return convert_to_format(space_feeler, '+', key, stringify(
            array=value_2, space_count=next_depth))
    # 5
    if is_first_dict_second_value(value_1, value_2):
        return [*convert_to_format(space_feeler, '-', key, stringify(
            array=value_1, space_count=next_depth)),
            *convert_to_format(space_feeler, '+', key, value_2)]
    return []


def resizer(deep_size, replacer, max_depth):
    if deep_size < max_depth:
        return deep_size * replacer
    else:
        return (deep_size - 4) * replacer


def stringify(array, replacer=" ", space_count=1, max_depth=8):
    def inner(line, depth=4):
        if not isinstance(line, dict):
            return f'{line}'
        output = []
        deep_size = space_count + depth
        space_feeler = deep_size * replacer
        current_feeler = resizer(deep_size, replacer, max_depth)
        keyword = getting_unique_keys(line)
        for key in keyword:
            value = line.get(key)
            output.append(f'{space_feeler}{key}: {inner(value, deep_size)}')
        result = itertools.chain("{", output, [current_feeler + "}"])
        return '\n'.join(result)
    return inner(array)


def dif(first_dict: dict, second_dict: dict, depth=0, replacer=' ') -> str:
    output = []

    deep_size = depth + 1
    space_feeler = deep_size * replacer
    current_feeler = replacer * depth

    set_of_unique_keys = check_values_forms(first_dict, second_dict)
    for k in set_of_unique_keys:
        key, key2 = first_dict.get(k, type), second_dict.get(k, type)

        output.extend(compare_two_values(space_feeler, k, key, key2))
        output.extend(compare_two_dicts(space_feeler, k, key, key2,
                                        depth=deep_size))

    outcome = itertools.chain("{", output, [current_feeler + "}"])
    return serialize_output('\n'.join(outcome))


def generate_diff(dictionary_1: dict, dictionary_2: dict) -> str:
    return dif(dictionary_1, dictionary_2)


if __name__ == '__main__':
    data = get_data("test_5_recurs_file1.json", "test_5_recurs_file2.json")
    file1, file2 = data
    result = generate_diff(file1, file2)
    print(result)
