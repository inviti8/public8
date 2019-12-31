import os
import webbrowser
import jinja2
import html_parser

import index_render_data

SCRIPT_PATH = os.path.realpath(__file__)
FILE_NAME = os.path.basename(SCRIPT_PATH)
PATH = SCRIPT_PATH.replace(FILE_NAME, "")

TITLE = None
CSS = None
PAGE_DIRECTION = None
TEMPLATE_DIR = None
THEME = "css/onsen-css-components.css"
TEMPLATE_FILE = "index.html.j2"
TEMPLATE_RENDER_DATA = "index_render_data.py"
PAGE = "index.html"
CONTENT = None

def UpdateCss():
    print("Update Css")
    CSS = index_render_data.DATA[TEMPLATE_DIR]
    return CSS["css"]

def open_test_page():
    print("open test page")
    if TEMPLATE_DIR is not None or TEMPLATE_DIR is not "None":
        new_tab = 2
        template_path = os.path.join(PATH, "templates")
        template_path = os.path.join(template_path, TEMPLATE_DIR)
        template_file = os.path.join(template_path, TEMPLATE_FILE)
        html_file = os.path.join(template_path, PAGE)
        
        # print(template_file)
        # print(index_render_data.DATA[TEMPLATE_DIR])
        template_data = index_render_data.DATA[TEMPLATE_DIR]

        if TITLE != None:
            template_data.update({"title": TITLE})

        if CSS != None:
            template_data.update({"css": CSS})

        if PAGE_DIRECTION != None:
            template_data.update({"page_direction": PAGE_DIRECTION})

        if THEME == "Dark Theme":
            template_data.update({"css_theme": "css/dark-onsen-css-components.css"})

        elif THEME == "Light Theme":
            template_data.update({"css_theme": "css/onsen-css-components.css"})

        elif THEME == "Gray Theme":
            template_data.update({"css_theme": "css/old-onsen-css-components.css"})

        if CONTENT != None:
            parser = html_parser.DocHTMLParser()
            parser.reset()
            parser.reset_current_char_count()
            parser.feed(CONTENT)
            content = parser.get_content_html_list()
            template_data.update({"content_list": content})


        render_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        output_text = render_environment.get_template(TEMPLATE_FILE).render(template_data)

        with open(html_file, "w") as result_file:
            result_file.write(output_text)
            result_file.close

        webbrowser.open(html_file, new_tab)
        
