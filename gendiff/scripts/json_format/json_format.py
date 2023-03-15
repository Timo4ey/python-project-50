from gendiff.prepare_data.prepare_data import prepare_data
from gendiff.scripts.checkers.checkers import \
    check_values_forms, is_first_value_not_type, is_first_value_type, \
    is_both_not_type
import json


def add_values(response, output):
    if response.get('added'):
        output['added'].update(response.get('added'))

    elif response.get('removed'):
        output['removed'].update(response.get('removed'))

    elif response.get('updated'):
        output['updated'].update(response.get('updated'))
    return output


def format_to_json(first_value, second_value, key=''):
    output = {'added': {},
              'removed': {},
              'updated': {}}
    if is_first_value_type(first_value, second_value):
        output['added'][key] = second_value
        return output
    elif is_first_value_not_type(first_value, second_value):
        output['removed'][key] = first_value
        return output

    elif is_both_not_type(first_value, second_value):
        output['updated'][key] = {"from": first_value, "to": second_value}
        return output

    if first_value == second_value:
        return {}

    get_of_unique_keys = check_values_forms(first_value, second_value)
    for keyword in get_of_unique_keys:
        value_1 = first_value.get(keyword, type)
        value_2 = second_value.get(keyword, type)

        response = format_to_json(value_1, value_2, keyword)
        output.update(add_values(response, output))

    return output


def json_format(first_dict, second_dict):
    response = format_to_json(first_dict, second_dict)
    return json.dumps(response, indent=2)


if __name__ == "__main__":
    file1, file2 = prepare_data("test_5_recurs_file1.json",
                                "test_5_recurs_file2.json")
    resp = json_format(file1, file2)
    print(resp)
