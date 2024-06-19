import re
import urllib.request


class HtmlParser:
    def __init__(self, url: str):
        self.url = url
        self.html_content = self._fetch_html_content()
        self.element = None

    def _fetch_html_content(self):
        with urllib.request.urlopen(self.url) as response:
            return response.read().decode('utf-8')

    def with_id(self, element_id: str):
        self.element = self._extract_element_by_id(element_id)
        return self

    def with_class(self, class_name: str):
        self.element = self._extract_element_by_class(class_name)
        return self

    def get_inner_content(self):
        return self.element

    def _extract_element_by_id(self, element_id: str):
        pattern = fr'<([a-zA-Z]+)[^>]*\s+id="{element_id}"[^>]*>(.*?)</\1>'
        match = re.search(pattern, self.html_content, re.DOTALL)
        return match.group(2).strip() if match else None

    def _extract_element_by_class(self, class_name: str):
        pattern = fr'<([a-zA-Z]+)[^>]*\s+class="[^"]*\b{class_name}\b[^"]*"[^>]*>(.*?)</\1>'
        match = re.search(pattern, self.html_content, re.DOTALL)
        return match.group(2).strip() if match else None
