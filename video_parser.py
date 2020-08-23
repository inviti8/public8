import html
import subprocess



def ParseFFMpegMetaData():
  result = {}
  props =["major_brand=", "minor_version=", "compatible_brands=", "title=", "date=", "comment=", "encoder="]
  txtFile = open("FFMETADATAFILE.txt", "r")
  title = ""
  body = ""
  Lines = txtFile.readlines()
  # for prop in props:
  #   for line in Lines:
  #     text = ""
  #     if prop == "title=" and "major_brand=" not in line and "minor_version=" not in line and "compatible_brands=" not in line and "comment=" not in line and "encoder=" not in line:
  #       title += line
  #     elif prop == "comment=" and "major_brand=" not in line and "minor_version=" not in line and "compatible_brands=" not in line and "title=" not in line and "encoder=" not in line:
  #       body += line

  for line in Lines:
    if "title=" in line:
      title += line

    result['title'] = title
    result['body'] = body

    return result




def VideoHtmlTag(filelocation):
  subprocess.call(["ffmpeg", "-i", filelocation, "-f", "ffmetadata", "FFMETADATAFILE.txt", "-y"])
  metaData = ParseFFMpegMetaData()
  print("][][][][][][][][][][][][][][][][][][][][][][][]")
  print(metaData['title'])
  print("][][][][][][][][][][][][][][][][][][][][][][][]")
  html = ''
  html += '<div class="outer r4x3">\n'
  html += '  <div class="inner">\n'
  html += '     <video class="video" width="50%" height="auto" controls="true">\n'
  html += '         <source src=' + filelocation + ' type="video/mp4">\n'
  html += '     </video>\n'
  html += '     <h1>' + metaData['title'] + '</h1>\n'
  html += '     <div>' + metaData['body'] + '</div>\n'


  html += '   </div>\n</div>\n'

  return html

def VideoTagList(pathList):
    result = []
    index = 0
    for path in pathList:
        result.insert(index, VideoHtmlTag(path))
        index = index+1

    return result

