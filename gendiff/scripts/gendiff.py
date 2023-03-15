import argparse
from gendiff.prepare_data.prepare_data import prepare_data
from gendiff.scripts.json_format.json_format import json_format
from gendiff.scripts.plain.plain import plain
from gendiff.scripts.stylish.stylish import stylish


def command():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description=description)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help="set format of output", default="stylish")

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    methods = {
        "stylish": stylish,
        "plain": plain,
        "json": json_format
    }
    file1, file2, style = command()
    first_data, second_data = prepare_data(file1, file2)
    output = methods.get(style)(first_data, second_data)
    print(output)


if __name__ == '__main__':
    main()
