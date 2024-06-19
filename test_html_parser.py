import unittest
from html_parser import HtmlParser
from unittest.mock import patch

class TestHtmlParser(unittest.TestCase):
    def setUp(self):
        self.sample_html = '''
        <html>
            <body>
                <div id="test-id">Content with ID</div>
                <div class="test-class">Content with Class</div>
            </body>
        </html>
        '''

    @patch('html_parser.HtmlParser._fetch_html_content')
    def test_with_id(self, mock_fetch_html):
        mock_fetch_html.return_value = self.sample_html
        parser = HtmlParser('http://example.com')
        content = parser.with_id('test-id').get_inner_content()
        self.assertEqual(content, 'Content with ID')

    @patch('html_parser.HtmlParser._fetch_html_content')
    def test_with_class(self, mock_fetch_html):
        mock_fetch_html.return_value = self.sample_html
        parser = HtmlParser('http://example.com')
        content = parser.with_class('test-class').get_inner_content()
        self.assertEqual(content, 'Content with Class')

if __name__ == '__main__':
    unittest.main()
