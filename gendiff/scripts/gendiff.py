import argparse
from gendiff.generate_diff import generate_diff
from gendiff.prepare_data.prepare_data import prepare_data


def command():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description=description)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help="set format of output", default="plain")

    args = parser.parse_args()
    return args.first_file, args.second_file


def main():
    file1, file2 = command()
    # path1, path2 = find_files(file1, file2)
    first_data, second_data = prepare_data(file1, file2)

    diff = generate_diff(first_data, second_data)
    print(diff)


if __name__ == '__main__':
    main()
