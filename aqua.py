# generates the ascii art

import os
import sys
import time
from PIL import Image

# Image File
img_file = 'aqua/1.gif'
img = Image.open(img_file)

# terminal size
size = os.get_terminal_size()

# different ascii chars for mapping
asciiChars = '@#S%?*+;:,. '
# asciiChars = " .:-=+*#%@"
# asciiChars = ' .,:;+*?%S#@'

def greyScale(rgb):
    return (rgb[0] + rgb[1] + rgb[2])/3

asciiAqua = []

# frame is an integer that is used to iterate through the different frames in a gif
print('generating ascii aqua...')
for frame in range(img.n_frames):
    asciiAquaFrame = ''
    img.seek(frame)

    # createing a new image to work on cause gifPlugin SUCKS ig idk
    tempImg = Image.new('RGB', img.size)
    tempImg.paste(img)

    # resize height to width*2 cuz 1 char heght is 2 char width long
    # tempImg = tempImg.resize((int(size.lines/img.size[1] * img.size[0])*2,  size.lines))
    tempImg = tempImg.resize((img.size[0]*2,img.size[1]))
    tempImg.thumbnail(((size.columns*2)-1, size.lines-1))

    for y in range(tempImg.size[1]):
        for x in range(tempImg.size[0]):

            rgb = greyScale(tempImg.getpixel((x,y)))

            for i in range(len(asciiChars)):
                if rgb <= ((255/len(asciiChars)) * (i+1)):
                    asciiAquaFrame += asciiChars[i]
                    # sys.stdout.write(asciiChars[i])
                    break
        asciiAquaFrame += '\n'

    asciiAqua.append(asciiAquaFrame)

# clear screen before printing art
sys.stdout.write(chr(27)+'[2j' + '\033c \x1bc')

while 1:
    for i in range(len(asciiAqua)):
        sys.stdout.write(asciiAqua[i])

        # time.sleep(0.1)
        sys.stdout.write(chr(27)+'[2j' + '\033c \x1bc')