import os
import subprocess

TEMPLATE_PATH = None


def ParseBodyContent(line, fullText):
  result = ""
  if "comment=" in line:
    result = line.replace("comment=", "")
    return result

  elif ";FFMETADATA1" not in line and "major_brand=" not in line and "minor_version=" not in line and "compatible_brands=" not in line and "title=" not in line and "encoder=" not in line and "date=" not in line:
    result = fullText + line
  elif ";FFMETADATA1" in line or "major_brand=" in line or "minor_version=" in line or "compatible_brands=" in line or "title=" in line or "encoder=" in line or "date=" in line:
    return "$NONE$"

  return result


def ParseFFMpegMetaData():
  result = {}
  title = ""
  body = ""
  content = ""
  bodyParsing = False

  with open("FFMETADATAFILE.txt", "r") as fp:
    for cnt, line in enumerate(fp):
      line = line.strip()
      if 'title=' in line:
        title = line.replace('title=', '')
      elif 'comment=' in line or bodyParsing == True:
        bodyParsing = True
        content = ParseBodyContent(line, content)
        if "$NONE$" not in content:
          body += content


  result['title'] = title
  result['body'] = body

  return result

def VideoHtmlTag(filelocation):
  localFileLocation = os.path.join(TEMPLATE_PATH, filelocation)
  subprocess.call(["ffmpeg", "-i", localFileLocation, "-f", "ffmetadata", "FFMETADATAFILE.txt", "-y"])
  metaData = ParseFFMpegMetaData()
  
  html = ''
  html += '<div class="outer r4x3">\n'
  html += '  <div class="inner">\n'
  html += '     <video class="video" controls="true">\n'
  html += '         <source src=' + filelocation + ' type="video/mp4">\n'
  html += '     </video>\n'
  html += '     <h1>' + metaData['title'] + '</h1>\n'
  html += '     <div class="video-body">' + metaData['body'] + '</div>\n'


  html += '   </div>\n</div>\n'

  return html

def VideoTagList(pathList):
    result = []
    index = 0
    for path in pathList:
        result.insert(index, VideoHtmlTag(path))
        index = index+1

    return result

