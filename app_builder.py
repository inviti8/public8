import os
import file_action
import mammoth
import html_parser
import re

ARWEAVE_APP_TYPE = None
ARWEAVE_APP_TITLE = None
AUTHOR = None
CSS = None
CONTENT_TYPE = None
CONTENT_PATH = None
THEME = None
SIGN_APP = False

def docx_to_html(docx):
    print("Convert: " + docx + " to html." )
    result = None

    with open(docx, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion
        
    return result

def psd_to_html(psd):
    directory = os.path.dirname(psd)
    print(psd)
    print(directory)
    for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".psd"): 
         print(os.path.join(directory, filename))


def build_app(template):
    print("build app: " + template)