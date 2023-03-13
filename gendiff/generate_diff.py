from gendiff.prepare_data.prepare_data import (prepare_data,
                                               serialize_output,
                                               get_unique_keys, find_files
                                               )





def handler(file_path1, file_path2):
    if type(file_path1) is not dict and type(file_path2) is not dict:
        first_file, second_file, keys = prepare_data(file_path1, file_path2)
    else:
        value = list({*file_path2.keys(), *file_path1.keys()})
        value.sort()
        first_file, second_file, keys = file_path1, file_path2, value
    return first_file, second_file, keys


def is_dict(*args):
    return any(filter(lambda x: isinstance(x, dict), args))


def getting_unique_keys(*args: dict) -> list:
    output = []
    filtred = list(filter(lambda x: not isinstance(x, type | None | int), args))
    [output.append(j) for d in filtred for j in d]
    output = set(output)
    output = list(output)
    output.sort()
    return output





def get_key_value(value) -> str:
    if not isinstance(value, dict):
        return f'{value}'
    output = ''
    for key, val in value.items():
        output += f'{key}: {get_key_value(value)}'
    return output


def is_not_type_or_dict(array) -> bool:
    return not isinstance(array, dict | type)


def is_dict(array) -> bool:
    return isinstance(array, dict)

def get_value(key, some_dict: dict) -> dict.values:
    if isinstance(some_dict, dict):
        return some_dict.get(key, type)
    return type


def is_equals(first, second):
    return first == second

def stringify(array,  replacer=" ", space_count=1):
    def inner(array, deph=0):
        if not isinstance(array, dict):
            return f'{array}'
        output = ""
        deep_size = space_count + deph
        space_feeler = deep_size * replacer
        for key, value in array.items():
            output += f'\n{space_feeler}{key}: {inner(value, deep_size)}'
        return output
    return inner(array)


def get_data(file_path1, file_path2):
    first_file = second_file = 0
    dict_predicate = is_dict(file_path1)
    if not dict_predicate:
        first_file, second_file = prepare_data(file_path1, file_path2)
    elif dict_predicate:
        first_file, second_file = file_path1, file_path2
    return first_file, second_file


def symble_checker(symle, to_change):
    if symle == " ":
        return to_change
    elif symle in ("+", "-"):
        return ' '

# def stringify(array,  , space_count=1):
import  itertools


def stringify(array,  replacer=" ", space_count=1):
    def inner(array, deph=2):
        if not isinstance(array, dict):
            return f'{array}'
        output = ""
        deep_size = space_count + deph
        space_feeler = deep_size * replacer
        current_feeler = replacer * deph
        keyword = getting_unique_keys(array)
        for key in keyword:
            value = array.get(key)
            output += f'\n{space_feeler}{key}: {inner(value, deep_size)}'
        result = f'{"{"}{output}\n{current_feeler}{"}"}'
        return result
    return inner(array)


def compare_two_values(key, value_1, value_2, depth=0):
    frame = '\n{} {}: {}'
    if dict not in (type(value_1), type(value_2)):
        if value_1 == value_2:
            return frame.format(' ', key, value_1)
        elif value_1 != value_2 and value_2 is type:
            return frame.format('-', key, value_1)
        elif value_1 != value_2 and value_1 is type:
            return frame.format('+', key, value_2)
        elif value_1 != value_2 and type not in (value_1, value_2):
            return f"{frame.format('-', key, value_1)}\n{frame.format('+', key, value_2)}"
    return ''


def compare_two_dicts(key, value_1, value_2, depth=2):
    frame = '\n{} {}: {}'
    if dict in (type(value_1), type(value_2)):
        uniques_keys = getting_unique_keys(value_1, value_2)
        for keyword in uniques_keys:
            if value_1 == value_2:
                return frame.format(' ', key, stringify(value_1, space_count=depth))
            if value_1 == value_2 and value_2 is type:
                return frame.format('-', keyword, stringify(value_1, space_count=depth))
            if value_1 != value_2 and value_1 is type:
                return frame.format('+', key, stringify(value_2, space_count=depth))
            if value_1 != value_2 and type not in (value_1, value_2):
                return f"{frame.format('-', keyword, stringify(value_1, space_count=depth + 1))}\n {frame.format('+', keyword, stringify(value_2, space_count=depth + 1))}"
    return ''



def generate_diff(dictionary_1, dictionary_2,  space_count: int = 1) -> str:

    frame = '{}{} {}: {}'
    replacer = ' '

    def dif(first_dict, second_dict, depth=0, symble=' '):
        output = []

        deep_size = depth + 1
        space_feeler = deep_size * replacer
        current_feeler = replacer * depth
        set_of_unique_keys = None
        if is_dict(first_dict) and is_dict(second_dict):
            set_of_unique_keys = getting_unique_keys(first_dict, second_dict)
        if is_dict(first_dict) and is_dict(second_dict) is False:
            set_of_unique_keys = getting_unique_keys(first_dict)
            second_dict = {}
        if is_dict(first_dict) is False and is_dict(second_dict):
            set_of_unique_keys = getting_unique_keys(second_dict)
            first_dict = {}
        for k in set_of_unique_keys:

            key, key2 = first_dict.get(k, type), second_dict.get(k, type)

            if key == key2 and type(key) is dict \
                    and type(key2) is dict:
                output.append(frame.format(space_feeler, ' ', k, dif(key, key2,depth=deep_size + 1)))

            elif key != key2 and\
                    type(key) is dict and\
                    type(key2) is dict:
                output.append(frame.format(space_feeler, ' ', k, dif(key, key2,depth=deep_size +3)))
            elif key != key2 and\
                    type(key) is dict and\
                    type(key2) is type:
                output.append(frame.format(space_feeler, '-', k, stringify(array=key, space_count = deep_size + 3)))
            elif key != key2 and\
                    type(key) is type and\
                    type(key2) is dict:
                output.append(frame.format(space_feeler, '+', k, stringify(array=key2, space_count = deep_size +4)))
            elif key != key2 and \
                    type(key) is dict and \
                    type(key2) is not dict:
                output.append(frame.format(space_feeler, '-', k, stringify(array=key, space_count=deep_size + 3 )))
                output.append(frame.format(space_feeler, '+', k, key2))
            elif key == key2 and \
                    type(key) not in (dict, type):
                output.append(frame.format(space_feeler, symble, k, key))
            elif key != key2 and \
                    type(key) is not type and \
                    type(key2) is not type:
                output.append(frame.format(space_feeler, '-', k, key))
                output.append(frame.format(space_feeler, '+', k, key2))
            elif key != key2 and \
                    type(key) is not type and \
                    type(key2) is type:
                output.append(frame.format(space_feeler, '-', k, key))
            elif key != key2 and \
                    type(key) is type and \
                    type(key2) is not type:
                output.append(frame.format(space_feeler, '+', k, key2))

        # output = serialize_output(output)
        result = itertools.chain("{", output, [current_feeler + "}"])
        return serialize_output('\n'.join(result).strip())
    return dif(dictionary_1, dictionary_2)


if __name__ == '__main__':
    # print(generate_diff('test_1_file1.json', 'test_1_file2.json'))
    dict1 = {
        'first': 1,
        'second': 2,
        'third': {
            'tree': 3
        },
        'del': 0
    }
    dict2 = {
        'first': 1,
        'second': 2,
        'one': 7,
        'third': {
            'tree': 3
        },
        'inner': {
            'deep': 2
        }
    }

    # print(generate_diff(dict1, dict2))
    # data = get_data('test_1_file1.json', 'test_1_file2.json')
    data = get_data("test_5_recurs_file1.json", "test_5_recurs_file2.json")
    file1, file2 = data
    print(generate_diff(file1, file2))

# for k in key_words:
#     key, key2 = get_value_from_two_dicts(k, first_dict, second_dict)
#     if first_dict.get(k) == second_dict.get(k):
#         output += frame.format(' ', k, key)
#     else:
#         output += frame.format('-', k, key) if \
#             (key is not type) else ''
#         output += frame.format('+', k, key2) if \
#             (key2 is not type) else ''