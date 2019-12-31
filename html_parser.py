from html.parser import HTMLParser
from html.entities import name2codepoint

HTML_PARSE_OBJECT = {}

class DocHTMLParser(HTMLParser):
    CHAR_PER_PAGE = 4500

    current_tag = None
    current_char_count = 0
    current_page_count = 0
    current_page_html = ""

    close_tag = ">"
    p_open = "<p>"
    p_close = "</p>"
    img_open = "<img>"
    img_close = "</img src="
    table_open = "<table><tr><td><p>"
    table_close = "</p></td></tr></table>"

    content_html_list = []

    def get_content_html_list(self):
        return self.content_html_list

    def reset_current_char_count(self):
        self.current_char_count = 0
        self.current_page_count = self.current_page_count + 1
        self.current_page_html = ""

    def handle_starttag(self, tag, attrs):
        # print("Start tag:", tag)
        self.current_tag = tag
        self.current_page_html = self.current_page_html + "<" + tag + ">"
        # for attr in attrs:
        #     print("     attr:", attr)

    def handle_endtag(self, tag):
        page_count = self.current_page_count

        self.current_page_html = self.current_page_html + "</" + tag + ">"

        if self.current_char_count >= self.CHAR_PER_PAGE:
            # print("THIS WORKS!!!!!!!!!!!!!!!!!!!!")
            # print(self.current_page_html)
            # print(self.current_char_count)
            self.content_html_list.insert(page_count, self.current_page_html)
            self.reset_current_char_count()

    def handle_data(self, data):
        current_count = self.current_char_count + len(data)

        if self.current_tag == "p":
            self.current_char_count = current_count + len(data)
            # html = self.p_open + data + self.p_close

        self.current_page_html = self.current_page_html + data

        # if self.current_tag == "table":
        #     html = self.table_open + data + self.table_close

        # if html != None:
        #     self.current_page_html = self.current_page_html + html
            # print("Data     :", data)


    # def handle_comment(self, data):
    #     print("Comment  :", data)

    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)

    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)

    # def handle_decl(self, data):
    #     print("Decl     :", data)

