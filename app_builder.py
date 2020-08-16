import os
import file_action
import mammoth
import html_parser
import psd_parser
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

def psd_to_html(directory):
    result = {}
    htmlList = []
    cssList = []
    indexList = []
    chapterList = []
    index = 0

    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)
        chapterSplit = filename.split('_')
        chapterName = None

        if len(chapterSplit) > 1:
            chapterName = chapterSplit[0]

        if filename.endswith(".psd"):
            psdFile = os.path.join(directory, filename)
            content = psd_parser.PSDHtmlAndCssParser(psdFile)
            html = content[0]
            css = content[1]
            print(psdFile)
            htmlList.insert(index, html)
            cssList.insert(index, css)
            indexList.insert(index, index)

    result['html'] = htmlList
    result['css'] = cssList
    result['index'] = indexList
            
    return result


def build_app(template):
    print("build app: " + template)