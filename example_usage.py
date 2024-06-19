from html_parser import HtmlParser

# Example URL
url = 'http://example.com'

# Initialize HtmlParser with URL
parser = HtmlParser(url)

# Extract inner content by ID
inner_content_by_id = parser.with_id('example-id').get_inner_content()
print(f'Content by ID: {inner_content_by_id}')

# Extract inner content by Class
inner_content_by_class = parser.with_class('example-class').get_inner_content()
print(f'Content by Class: {inner_content_by_class}')
