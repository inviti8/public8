import html
from html.parser import HTMLParser
from html.entities import name2codepoint

HTML_PARSE_OBJECT = {}

class DocHTMLParser(HTMLParser):
    CHAR_PER_PAGE = 4500

    current_tag = None
    current_char_count = 0
    current_page_count = 0
    current_page_html = ""

    content_html_list = []

    def get_content_html_list(self):
        return self.content_html_list

    def reset_current_char_count(self):
        self.current_char_count = 0
        self.current_page_count = self.current_page_count + 1
        self.current_page_html = ""

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.current_page_html = self.current_page_html + "<" + tag
        
        for attr in attrs:
            self.current_page_html = self.current_page_html + " " + attr[0] + "="
            self.current_page_html = self.current_page_html + " '" + attr[1] + "'"

        self.current_page_html = self.current_page_html + ">"

    def handle_endtag(self, tag):
        page_count = self.current_page_count

        self.current_page_html = self.current_page_html + "</" + tag + ">"

        if self.current_char_count >= self.CHAR_PER_PAGE:

            self.content_html_list.insert(page_count, self.current_page_html)
            self.reset_current_char_count()

    def handle_data(self, data):
        current_count = self.current_char_count + len(data)

        data = html.unescape(str(data))
        
        if self.current_tag == "p":
            self.current_char_count = current_count + len(data)

        if self.current_tag == "img":
            self.current_page_html = self.current_page_html + data + ">"

        else:
            self.current_page_html = self.current_page_html + data

