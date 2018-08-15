import argparse
import sys


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser(
                description='Perform transformation on input text.')
    parser.add_argument('-u', '--upper',
                        help='convert text to uppercase', action="store_true")
    parser.add_argument('-l', '--lower',
                        help='convert text to lowercase', action="store_true")
    parser.add_argument('-t', '--title',
                        help='convert text to titlecase', action="store_true")
    parser.add_argument('text',
                        help='text to be manipulated')
    args = parser.parse_args()
    if not args:
        parser.print_help()
        sys.exit(1)
    text = args.text
    no_option = True
    if args.upper:
        no_option = False
        text = convert_to_upper(text)
    if args.lower:
        no_option = False
        text = convert_to_lower(text)
    if args.title:
        no_option = False
        text = convert_to_title(text)
    if no_option:
        print args.text
    else:
        print text


def convert_to_upper(text):
    return text.upper()


def convert_to_lower(text):
    return text.lower()


def convert_to_title(text):
    return text.title()


if __name__ == '__main__':
    main()
