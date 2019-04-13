#import numpy as np
import string
from PIL import Image, ImageFont, ImageDraw

# MakeImage function
#    Generate an image of text
#    t:      The text to display in the image
#    f:      The font to use
#    fn:     The file name
#    s:      The image size
#    o:      The offest of the text in the image
#


def MakeImg(textString, f, outputFileName, png_size = (100, 100), offset= (16, 8)):
    img = Image.new('RGB', png_size, "green")
    draw = ImageDraw.Draw(img)
    draw.text(OFS, textString, (255, 255, 255), font = f)
    img.save(outputFileName)
 


 ################## main func

MS = (100, 100)
OFS = (1,1)
font = ImageFont.truetype("/usr/lib/jvm/java-8-oracle/jre/lib/fonts/LucidaSansRegular.ttf", 32)


MakeImg("1", font, "test.png", MS, OFS)


