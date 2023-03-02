import argparse


def main():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description=description)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT', help="set format of output")

    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
