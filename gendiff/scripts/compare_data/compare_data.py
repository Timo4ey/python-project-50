import itertools

from gendiff.generate_diff import dif
from gendiff.scripts.checkers.checkers import is_dicts_equals, is_both_dicts_not_equal, is_only_first_value_dict, \
    is_only_second_value_dict, is_first_dict_second_value
from gendiff.scripts.formartter.formartter import convert_to_format
from gendiff.scripts.get_unique_keys.unique_keys import getting_unique_keys


def compare_two_values(space_feeler: str, key, value_1, value_2) -> list[str]:
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


def compare_two_dicts(space_feeler:  str, key, value_1: dict, value_2: dict, depth=0):
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
        space_feeler = deep_size * replacer
        current_feeler = resizer(deep_size, replacer, max_depth)
        keyword = getting_unique_keys(line)
        for key in keyword:
            value = line.get(key)
            output.append(f'{space_feeler}{key}: {inner(value, deep_size)}')
        result = itertools.chain("{", output, [current_feeler + "}"])
        return '\n'.join(result)
    return inner(array)
