from gendiff.prepare_data.prepare_data import prepare_data
from gendiff.scripts.checkers.checkers import (check_values_forms,
                                               is_first_value_type,
                                               is_first_value_not_type,
                                               is_both_not_type)
from gendiff.scripts.plain.scr.plain_tools import (plain_format,
                                                   check_if_complex,
                                                   head_converter)


def convert_to_plain(first_value, second_value, key='', head=''):
    output = []
    old_value = check_if_complex(first_value)
    new_value = check_if_complex(second_value)

    if is_first_value_type(first_value, second_value):
        return plain_format("added", head=head, new_value=new_value)

    elif is_first_value_not_type(first_value, second_value):
        return plain_format("removed", head=head)

    elif is_both_not_type(first_value, second_value):
        return plain_format("updated", head=head, old_value=old_value,
                            new_value=new_value)

    elif first_value == second_value:
        return []
    get_of_unique_keys = check_values_forms(first_value, second_value)

    for keyword in get_of_unique_keys:
        head = head_converter(head)
        value_1 = first_value.get(keyword, type)
        value_2 = second_value.get(keyword, type)

        output.extend(
            convert_to_plain(
                value_1, value_2, key=keyword, head=f'{head}{keyword}'))
    return output


def plain(first_dict, second_dict, ):
    return '\n'.join(convert_to_plain(first_dict, second_dict))
