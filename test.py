import sys
import time
from PIL import Image

# Image File
img_file = 'aqua/2.gif'
img = Image.open(img_file)

# asciiChars = '@#S%?*+;:,. '
asciiChars = " .:-=+*#%@"
# asciiChars = ' .,:;+*?%S#@'

def greyScale(rgb):
    return (rgb[0] + rgb[1] + rgb[2])/3

while 1:
# frame is an integer that is used to iterate through the different frames in a gif
    print('generating ascii aqua...')
    for frame in range(img.n_frames):
        asciiAquaFrame = ''
        img.seek(frame)

        # createing a new image to work on cause gifPlugin SUCKS ig idk
        tempImg = Image.new('RGB', img.size)
        tempImg.paste(img)

        # resize height to height/2 cuz 1 char heght is 2 char width long
        tempImg = tempImg.resize((img.size[0]//3, img.size[1]//6))

        for y in range(tempImg.size[1]):
            for x in range(tempImg.size[0]):

                rgb = greyScale(tempImg.getpixel((x,y)))

                for i in range(len(asciiChars)):
                    if rgb <= ((255/len(asciiChars)) * (i+1)):
                        sys.stdout.write(asciiChars[i])
                        break
            print()

        time.sleep(0.02)
        sys.stdout.write(chr(27)+'[2j' + '\033c \x1bc')