import os
import webbrowser
import jinja2
import inspect
import html_parser

import index_render_data

SCRIPT_PATH = os.path.realpath(__file__)
FILE_NAME = os.path.basename(SCRIPT_PATH)
PATH = os.path.dirname(os.path.realpath(inspect.stack()[0][1]))

TITLE = None
CSS = None
PAGE_DIRECTION = None
TEMPLATE_DIR = None
CONTENT_TYPE = None
THEME = "css/onsen-css-components.css"
TEMPLATE_FILE = "index.html.j2"
TEMPLATE_RENDER_DATA = "index_render_data.py"
PAGE = "index.html"
DOC_CONTENT = None
PSD_CONTENT = None
VIDEO_CONTENT = None
TABLE_ALIGN = "LEFT"

def UpdateCss():
    print("Update Css")
    CSS = index_render_data.DATA[TEMPLATE_DIR]
    return CSS["css"]

def open_test_page():
    print("open test page")

    if CONTENT_TYPE == "Docx":
        create_text_content_and_open()
    elif CONTENT_TYPE == "Psd":
        create_psd_content_and_open()
    elif CONTENT_TYPE == "Video":
        create_video_content_and_open()


def create_text_content_and_open():
    print("creating text content to test")
    if TEMPLATE_DIR is not None or TEMPLATE_DIR is not "None":
        new_tab = 2
        template_path = os.path.join(PATH, "templates")
        template_path = os.path.join(template_path, TEMPLATE_DIR)
        template_file = os.path.join(template_path, TEMPLATE_FILE)
        html_file = os.path.join(template_path, PAGE)
        
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

        if DOC_CONTENT != None:
            parser = html_parser.DocHTMLParser()
            parser.TABLE_ALIGNMENT = TABLE_ALIGN
            parser.reset()
            parser.feed(DOC_CONTENT)
            content = parser.get_content_html_list()
            chapters = parser.get_chapter_html_list()
            chapter_indexes = parser.get_chapter_index_html_list()
            template_data.update({"content_list": content})
            template_data.update({"chapter_list": chapters})
            template_data.update({"chapter_index_list": chapter_indexes})


        render_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        output_text = render_environment.get_template(TEMPLATE_FILE).render(template_data)

        with open(html_file, "w") as result_file:
            result_file.write(output_text)
            result_file.close

        webbrowser.open(html_file, new_tab)

def create_psd_content_and_open():
    print(" creating psd content and opening")
    if TEMPLATE_DIR is not None or TEMPLATE_DIR is not "None":
        new_tab = 2
        template_path = os.path.join(PATH, "templates")
        template_path = os.path.join(template_path, TEMPLATE_DIR)
        template_file = os.path.join(template_path, TEMPLATE_FILE)
        html_file = os.path.join(template_path, PAGE)
        
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

        if PSD_CONTENT != None:
            content = PSD_CONTENT['html']
            chapters = PSD_CONTENT['chapter']
            chapter_indexes = PSD_CONTENT['index']
            inline_css = PSD_CONTENT['css']
            template_data.update({"content_list": content})
            template_data.update({"chapter_list": chapters})
            template_data.update({"chapter_index_list": chapter_indexes})
            template_data.update({"inline_css_list": inline_css})


        render_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        output_text = render_environment.get_template(TEMPLATE_FILE).render(template_data)

        with open(html_file, "w") as result_file:
            result_file.write(output_text)
            result_file.close

        webbrowser.open(html_file, new_tab)


def create_video_content_and_open():
    print(" creating video content and opening")
    if TEMPLATE_DIR is not None or TEMPLATE_DIR is not "None":
        new_tab = 2
        template_path = os.path.join(PATH, "templates")
        template_path = os.path.join(template_path, TEMPLATE_DIR)
        template_file = os.path.join(template_path, TEMPLATE_FILE)
        html_file = os.path.join(template_path, PAGE)
        
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

        if VIDEO_CONTENT != None:
            content = VIDEO_CONTENT['html']
            chapters = VIDEO_CONTENT['chapter']
            chapter_indexes = VIDEO_CONTENT['index']
            template_data.update({"content_list": content})
            template_data.update({"chapter_list": chapters})
            template_data.update({"chapter_index_list": chapter_indexes})


        render_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        output_text = render_environment.get_template(TEMPLATE_FILE).render(template_data)

        with open(html_file, "w") as result_file:
            result_file.write(output_text)
            result_file.close

        webbrowser.open(html_file, new_tab)
        
