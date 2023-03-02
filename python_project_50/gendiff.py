import argparse


def main():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description=description,
        epilog='Text at the bottom of help')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()