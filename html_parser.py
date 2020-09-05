import html
from html.parser import HTMLParser
from html.entities import name2codepoint

HTML_PARSE_OBJECT = {}

class TestFileVideoParser(HTMLParser):
    print("parse test html file")

class DocHTMLParser(HTMLParser):
    CHAR_PER_PAGE = 5000
    TABLE_ALIGNMENT = "left"

    previous_tag = None
    current_tag = None
    current_char_count = 0
    current_page_count = 0
    current_page_html = ""
    char_count_adjustment = 0
    page_image_count = 0

    chapter_list = []
    chapter_index_list = []
    content_html_list = []
    table_align = None

    def get_chapter_index_html_list(self):
        return self.chapter_index_list

    def get_chapter_html_list(self):
        return self.chapter_list

    def get_content_html_list(self):
        return self.content_html_list

    def reset_current_char_count(self):
        self.current_char_count = 0
        self.current_page_count = self.current_page_count + 1
        self.current_page_html = ""
        self.char_count_adjustment = 0
        self.page_image_count = 0

    def handle_starttag(self, tag, attrs):

        self.previous_tag = self.current_tag
        self.current_tag = tag
        self.current_page_html = self.current_page_html + "<" + tag

        if tag == "table":

            if self.table_align == None:
                if self.TABLE_ALIGNMENT == "alternate":
                    self.table_align = "left"
                else:
                    self.table_align = self.TABLE_ALIGNMENT

            self.current_page_html = self.current_page_html + ' style= "float:' + self.table_align +';"'

            if self.TABLE_ALIGNMENT == "alternate":
                
                if self.table_align == "left":
                    self.table_align = "right"
                    
                elif self.table_align == "right":
                    self.table_align = "left"

        
        for attr in attrs:
            if tag == "img":
                self.page_image_count = self.page_image_count  + 1
                self.current_page_html = self.current_page_html + ' class="img" id= "img_' + str(self.current_page_count) + '_' + str(self.page_image_count) + '" '

            
            self.current_page_html = self.current_page_html + " " + attr[0] + "="
            self.current_page_html = self.current_page_html + " '" + attr[1] + "'"

        self.current_page_html = self.current_page_html + ">"

    def handle_endtag(self, tag):
        page_count = self.current_page_count
        self.current_page_html = self.current_page_html + "</" + tag + ">"

        if tag == "h1":
            self.chapter_index_list.append(self.current_page_count)
            self.char_count_adjustment = self.char_count_adjustment + 500
        elif tag == "img":
            self.char_count_adjustment = self.char_count_adjustment + 1500

        elif tag == "p" and self.current_char_count >= (self.CHAR_PER_PAGE - self.char_count_adjustment):

            self.content_html_list.insert(page_count, self.current_page_html)
            self.reset_current_char_count()


    def handle_data(self, data):
        current_count = self.current_char_count + len(data)

        #Strip out quotes for now, until I can get parser to handle them properly.
        data = str(data).encode('ascii','ignore').decode()

        if self.previous_tag == "h1" and self.current_tag == "a":
            self.chapter_list.append(data)
        
        if self.current_tag == "p":
            self.current_char_count = current_count + len(data)

        if self.current_tag == "h1":
            self.chapter_list.append(data)

        if self.current_tag == "img":
            self.current_page_html = self.current_page_html + data + ">"

        else:
            self.current_page_html = self.current_page_html + data

