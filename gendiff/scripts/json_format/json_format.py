from gendiff.prepare_data.prepare_data import prepare_data
from gendiff.scripts.checkers.checkers import \
    check_values_forms, is_first_value_not_type, is_first_value_type, \
    is_both_not_type
import json


def add_values(data: dict, output: dict) -> dict:
    if data.get('added'):
        output['added'].update(data.get('added'))

    elif data.get('removed'):
        output['removed'].update(data.get('removed'))

    elif data.get('updated'):
        output['updated'].update(data.get('updated'))

    return output


def json_format(first_value: dict, second_value: dict, key='') -> json.dumps:
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

        response = json_format(value_1, value_2, keyword)
        output = add_values(response, output)

    return json.dumps(output, indent=2)


if __name__ == "__main__":
    file1, file2 = prepare_data("test_1_file1.json", "test_1_file2.json")
    resp = json_format(file1, file2)
    print(resp)
