# Simple HTML Parser

Simple HTML Parser is a lightweight Python library designed to extract content from HTML elements based on their ID or class attributes.

## Features

- Fetch inner content from HTML elements by ID or class.
- Easy-to-use interface with clear error messages.
- Unit tests included for reliability.

## Installation (WIP)

To install Simple HTML Parser, simply run:

```bash
pip install simple-html-parser
```

## Usage

Import the `HtmlParser` class and initialize it with the URL of the HTML page you want to parse:

```python
from html_parser import HtmlParser

# Initialize HtmlParser with URL
parser = HtmlParser('http://example.com')
```

To extract content by ID:

```python
content_by_id = parser.with_id('example-id').get_inner_content()
print(f'Content by ID: {content_by_id}')
```

To extract content by class:

```python
content_by_class = parser.with_class('example-class').get_inner_content()
print(f'Content by Class: {content_by_class}')
```

## Testing

To run the unit tests, execute:

```bash
python -m unittest test_html_parser.py
```

## Contributions

Contributions are welcome! Please submit a pull request or open an issue if you have any suggestions or improvements.

## License

Simple HTML Parser is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
