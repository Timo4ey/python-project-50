from gendiff.scripts.get_unique_keys.unique_keys import getting_unique_keys


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


def is_dict(array) -> bool:
    return isinstance(array, dict)


def is_same_type(file1, file2):
    if file1 == file2:
        return True
    raise TypeError("Files must be the same type")


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
