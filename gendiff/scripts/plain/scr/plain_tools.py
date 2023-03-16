def plain_format(keyword, head='', old_value='', new_value=''):
    formats = {
        "added": "Property '{head}' was added with value: {new_value}",
        "removed": "Property '{head}' was removed",
        "updated":
            "Property '{head}' was updated. From {old_value} to {new_value}",
    }
    response = formats.get(keyword, type).format(
        head=head, old_value=old_value, new_value=new_value)
    return [''.join(response)]


def change_format(string):
    output = string
    values = {
        True: 'true',
        False: 'false',
        None: 'null'}
    value = values.get(string, type)
    if type(string) is str:
        output = f"'{string}'"
    elif type(string) in (float, int):
        output = string
    elif value is not type:
        output = value
    return output


def check_if_complex(value):
    if type(value) is dict:
        output = '[complex value]'
    else:
        output = change_format(value)
    return output


def head_converter(string):
    if len(string) > 0 and \
            f'{string}.'.find('..') == -1:
        return f'{string}.'
    return string
