# generates the ascii art

from PIL import Image

def aqua( gif, size, asciiChars):

    # convert rgb pixel value to single int with gretscale value
    def greyScale(rgb):
        return (rgb[0] + rgb[1] + rgb[2])/3

    # open the gif
    img_file = f'aqua/{gif}.gif'
    img = Image.open(img_file)

    # ascii art will be stored here in an array of ascii arts of single frames from the gifs
    asciiAqua = []

    # frame is an integer that is used to iterate through the different frames in a gif
    print('generating ascii aqua...')
    for frame in range(img.n_frames):
        frameAscii = ''
        img.seek(frame)

        # createing a new image to work on cause gifPlugin SUCKS ig idk
        tempImg = Image.new('RGB', img.size)
        tempImg.paste(img)

        # resize height to width*2 cuz 1 char heght is 2 char width long
        # tempImg = tempImg.resize((int(size.lines/img.size[1] * img.size[0])*2,  size.lines))
        tempImg = tempImg.resize((img.size[0]*2,img.size[1]))
        tempImg.thumbnail(((size[0]*2)-1, size[1]-1))

        for y in range(tempImg.size[1]):
            for x in range(tempImg.size[0]):

                rgb = greyScale(tempImg.getpixel((x,y)))

                for i in range(len(asciiChars)):
                    if rgb <= ((255/len(asciiChars)) * (i+1)):
                        frameAscii += asciiChars[i]
                        # sys.stdout.write(asciiChars[i])
                        break
            frameAscii += '\n'

        asciiAqua.append(frameAscii)

    return asciiAqua