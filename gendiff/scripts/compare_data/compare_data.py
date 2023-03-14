import itertools

from gendiff.prepare_data.prepare_data import serialize_output
from gendiff.scripts.checkers.checkers import (is_dicts_equals,
                                               is_both_dicts_not_equal,
                                               is_only_first_value_dict,
                                               is_only_second_value_dict,
                                               is_first_dict_second_value,
                                               check_values_forms)
from gendiff.scripts.formartter.formartter import convert_to_format
from gendiff.scripts.get_unique_keys.unique_keys import getting_unique_keys


def compare_two_values(space_filler: str, key, value_1, value_2) -> list[str]:
    output = []
    if dict not in (type(value_1), type(value_2)):
        if value_1 == value_2 \
                and type(value_1) not in (dict, type):
            output = convert_to_format(space_filler, ' ', key, value_1)

        elif value_1 != value_2 and \
                type(value_1) is not type and \
                type(value_2) is not type:
            output = [*convert_to_format(space_filler, '-', key, value_1),
                      *convert_to_format(space_filler, '+', key, value_2)]

        elif value_1 != value_2 and \
                type(value_1) is not type and \
                type(value_2) is type:
            output = convert_to_format(space_filler, '-', key, value_1)

        elif value_1 != value_2 and \
                type(value_1) is type and \
                type(value_2) is not type:
            output = convert_to_format(space_filler, '+', key, value_2)
    return output


def compare_two_dicts(space_filler: str, key,
                      value_1: dict, value_2: dict, depth=0):
    next_depth = 3
    next_depth = depth + next_depth
    output = []
    # 1
    if is_dicts_equals(key, value_1, value_2):
        output = convert_to_format(space_filler, ' ', key, compare_engine(
            value_1, value_2, depth=next_depth))
    # 2
    elif is_both_dicts_not_equal(value_1, value_2):
        output = convert_to_format(space_filler, ' ', key, compare_engine(
            value_1, value_2, depth=next_depth))
    # 3
    elif is_only_first_value_dict(value_1, value_2):
        output = convert_to_format(space_filler, '-', key, stringify(
            array=value_1, space_count=next_depth))
    # 4
    elif is_only_second_value_dict(value_1, value_2):
        output = convert_to_format(space_filler, '+', key, stringify(
            array=value_2, space_count=next_depth))
    # 5
    elif is_first_dict_second_value(value_1, value_2):
        output = [*convert_to_format(space_filler, '-', key, stringify(
            array=value_1, space_count=next_depth)),
            *convert_to_format(space_filler, '+', key, value_2)]
    return output


def resizer(deep_size: int, replacer: str, max_depth: int) -> str:
    if deep_size < max_depth:
        return deep_size * replacer
    else:
        return (deep_size - 4) * replacer


def stringify(array: dict, replacer=" ", space_count=1, max_depth=8) -> str:
    def inner(line, depth=4):
        if not isinstance(line, dict):
            return f'{line}'
        output = []
        deep_size = space_count + depth
        space_filler = deep_size * replacer
        current_feeler = resizer(deep_size, replacer, max_depth)
        keyword = getting_unique_keys(line)
        for key in keyword:
            value = line.get(key)
            output.append(f'{space_filler}{key}: {inner(value, deep_size)}')
        result = itertools.chain("{", output, [current_feeler + "}"])
        return '\n'.join(result)
    return inner(array)


def compare_engine(first_dict: dict, second_dict: dict, depth=0, replacer=' '):
    output = []

    deep_size = depth + 1
    space_filler = deep_size * replacer
    current_feeler = replacer * depth

    set_of_unique_keys = check_values_forms(first_dict, second_dict)
    for k in set_of_unique_keys:
        key, key2 = first_dict.get(k, type), second_dict.get(k, type)

        output.extend(compare_two_values(space_filler, k, key, key2))
        output.extend(compare_two_dicts(space_filler, k, key, key2,
                                        depth=deep_size))

    outcome = itertools.chain("{", output, [current_feeler + "}"])
    return serialize_output('\n'.join(outcome))
