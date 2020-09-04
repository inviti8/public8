import os
import file_action
import mammoth
import html_parser
import psd_parser
import video_parser
import media_action
import re
import inspect

SCRIPT_PATH = os.path.dirname(os.path.realpath(inspect.stack()[0][1]))
TEMPLATE_DIR = None
ARWEAVE_APP_TYPE = None
ARWEAVE_APP_TITLE = None
CSS = None
CONTENT_TYPE = None
CONTENT_PATH = None
THEME = None
SIGN_APP = False

def docx_to_html(docx):
    print("Convert: " + docx + " to html." )
    result = None

    templatePath = os.path.join("templates", TEMPLATE_DIR)
    localVideoPath = os.path.join(SCRIPT_PATH, templatePath)
    localVideoPath = os.path.join(localVideoPath, "videos")

    media_action.ClearFolder(localVideoPath)

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

    templatePath = os.path.join("templates", TEMPLATE_DIR)
    localVideoPath = os.path.join(SCRIPT_PATH, templatePath)
    localVideoPath = os.path.join(localVideoPath, "videos")

    media_action.ClearFolder(localVideoPath)

    for f in sorted(os.listdir(directory)):
        filename = os.fsdecode(f)
        chapterSplit = filename.split('_')
        chapterName = None

        if len(chapterSplit) > 1:
            chapterName = chapterSplit[0]

        if filename.endswith(".psd"):
            psdFile = os.path.join(directory, filename)
            content = psd_parser.PSDHtmlAndCssParser(psdFile)
            html = content[0]
            css = content[1]
            htmlList.insert(index, html)
            cssList.insert(index, css)
            indexList.insert(index, index)
            chapterList.insert(index, index)
            index=index+1

    result['html'] = htmlList
    result['css'] = cssList
    result['index'] = indexList
    result['chapter'] = chapterList
            
    return result

def video_to_html(directory):
    result = {}
    pathList = []
    indexList = []
    chapterList = []
    index = 0

    templatePath = os.path.join("templates", TEMPLATE_DIR)
    localVideoPath = os.path.join(SCRIPT_PATH, templatePath)
    localVideoPath = os.path.join(localVideoPath, "videos")
    video_parser.TEMPLATE_PATH = os.path.join(SCRIPT_PATH, templatePath)

    media_action.ClearFolder(localVideoPath)

    for f in sorted(os.listdir(directory)):
        filename = os.fsdecode(f)
        if filename.endswith(".mp4"):
            srcPath = os.path.join(directory, filename)
            destPath = os.path.join(localVideoPath, filename)
            appVideoPath = os.path.join("videos", filename)

            media_action.CopyVideoFile(srcPath, destPath)
            pathList.insert(index, appVideoPath)
            chapterList.insert(index, index)
            index = index+1
            print(srcPath)
            
            result['html'] = video_parser.VideoTagList(pathList)
            result['chapter'] = chapterList
            result['index'] = indexList
            indexList.insert(index, index)

    return result


def build_app(template):
    print("build app: " + template)