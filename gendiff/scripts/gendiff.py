import argparse
from gendiff.generate_diff import generate_diff
from gendiff.prepare_data.prepare_data import prepare_data
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
    file1, file2, style = command()
    first_data, second_data = prepare_data(file1, file2)
    if style == "stylish":
        output = stylish(first_data, second_data)
    else:
        output = generate_diff(first_data, second_data)
    print(output)


if __name__ == '__main__':
    main()
