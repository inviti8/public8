
from psd_tools import PSDImage
from PIL import Image
import re, sys, os
import io
import base64
import codecs
import uuid

SCALE = 1.0

elements = []

def layerstoimage(psd, layers):
  global elements
  html, css = '', ''

  for layer in reversed(layers):
    if hasattr(layer, 'layers'):
      site = layerstoimage(psd, layer.layers)
      html += site[0]
      css += site[1]
    else:
      # if layer name is already used for an id append _n, where n is smallest availible number
      def namelayer(checkname, i):
        if(checkname in elements):
          i += 1
          # remove _n if i higher than 1
          if(i>1):
            splitstring = checkname.split('_')
            splitstring.pop()
            checkname = ''.join(splitstring)
          return namelayer(checkname+"_"+str(i), i)
        else:
          return checkname

      # process name to make unique and strip special characters
      name = namelayer(layer.name, 0)
      elements.append(name)
      name = re.sub(',','', name)
      name = re.sub('\.','', name)
      name = re.sub('\s', '-', name)
      name = re.sub('\*', '-', name)
      name = re.sub('©', '', name)
      name = name + str(uuid.uuid4())
      print("Processing Layer: " + name)
      
      # if layer.has_mask():
      #   print("Layer Mask: " + str(layer.mask))

      # get width
      _width = (layer.bbox[2] - layer.bbox[0]) * SCALE
      _height = (layer.bbox[3] - layer.bbox[1]) * SCALE
      _x = layer.bbox[0] * SCALE
      _y = layer.bbox[1] * SCALE

      wPercentage = _width / psd.header.width * 100
      hPercentage = _height / psd.header.height * 100
      xPercentage = _x / psd.header.width * 100
      yPercentage = _y / psd.header.height * 100


      width = str(wPercentage) + '%'
      height = str(hPercentage) + '%'
      x = str(xPercentage) + '%'
      y = str(yPercentage) + '%'

       # save images as images
      layer_image = layer.as_PIL()
      data_img = None

      with io.BytesIO() as output:
        layer_image.save(output, format="PNG")
        data_img = base64.b64encode(output.getvalue())
        data_img = "  data:image/png;base64," + str(data_img, "utf-8")

      css += '#'+name+'{\n'
      css += '  position: absolute;\n'
      css += '  left: ' + x + ';\n'
      css += '  top: ' + y + ';\n'
      css += '  width: ' + width + ';\n'
      css += '  height: ' + height + ';\n'
      # css += '  background-image: url("images/' + name + '.png");\n'
      css += '  background-image: url("' + data_img + '");\n'
      css += '  background-size: cover;\n'
      css += '}\n'

      # create html
      
      html += '   <div id="' + name + '"></div>\n'


  return html, css

def PSDHtmlAndCssParser(filelocation):
  psd = PSDImage.load(filelocation)
  html = ''
  css = ''
  css += '.container {\n'
  css += '  width: calc(' + str(psd.header.width) + 'px * (' + str(psd.header.width) + ' / 100vw ));\n'
  css += '  height: calc(' + str(psd.header.height) + 'px * (' + str(psd.header.height) + ' / 100vh ));\n'
  css += '}\n'

  css += '.outer {\n'
  css += '  position: relative;\n'
  css += '  width: 100%;\n'
  css += '}\n'

  css += '.outer.r4x3 {\n'
  css += '  padding-top: 75%;\n'
  css += '}\n'

  css += '.outer.r2x1 {\n'
  css += '  padding-top: 50%;\n'
  css += '}\n'

  css += '.outer .inner  {\n'
  css += '  position: absolute;\n'
  css += '  top: 0;\n'
  css += '  left: 0;\n'
  css += '  right: 0;\n'
  css += '  bottom: 0;\n'
  css += '  outline: 1px solid grey;\n'
  css += '}\n'

  html += '<div class="outer r4x3">\n'
  html += '  <div class="inner">\n'

  site = layerstoimage(psd, psd.layers)
  html += site[0]
  html += '   </div>\n</div>\n'
  css += site[1]

  return html, css


