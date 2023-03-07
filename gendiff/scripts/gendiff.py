import argparse
from gendiff.generate_diff import generate_diff


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
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
