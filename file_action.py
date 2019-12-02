import os
import webbrowser

SCRIPT_PATH = scriptpath = os.path.realpath(__file__)
FILE_NAME = os.path.basename(SCRIPT_PATH)
PATH = SCRIPT_PATH.replace(FILE_NAME, "")
TEMPLATE = None

PAGE = "index.html"

def open_test_page():
    print("open test page")
    if TEMPLATE is not None or TEMPLATE is not "None":
        new_tab = 2
        template_path = os.path.join(PATH, "Templates")
        template_path = os.path.join(template_path, TEMPLATE)
        html_file = os.path.join(template_path, PAGE)
        print(html_file)
        webbrowser.open(html_file, new_tab)
