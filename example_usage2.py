import sys
import argparse
from html_parser import HtmlParser


def main():
    parser = argparse.ArgumentParser(
        description='Fetch inner content from an HTML element by ID or Class.')
    parser.add_argument('--url', required=True,
                        help='The URL of the HTML page.')
    parser.add_argument(
        '--id', help='The ID of the HTML element to fetch content from.')
    parser.add_argument(
        '--classname', help='The class of the HTML element to fetch content from.')

    args = parser.parse_args()

    if not args.id and not args.classname:
        print("Error: You must provide either an 'id' or a 'class'.")
        sys.exit(1)
    if args.id and args.classname:
        print("Error: You must provide either an 'id' or a 'class', not both.")
        sys.exit(1)

    parser = HtmlParser(args.url)

    if args.id:
        content = parser.with_id(args.id).get_inner_content()
    elif args.classname:
        content = parser.with_class(args.classname ).get_inner_content()

    if content:
        print(content)
    else:
        print("No content found for the specified ID or class.")


if __name__ == '__main__':
    main()
