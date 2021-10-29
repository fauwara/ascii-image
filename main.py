from PIL import Image
import numpy as np

##################################### CONFIG
# image file
image_file = 'lmao.png'
# dimensions
dimensions = (100,100) # (width, height) keep '/2' there. A charector is larger in height and smaller in width this is to compensate for that.
keep_aspect_ratio = False

# testing
testing = False
display_image = False
display_ascii_text = True

##################################### SOME FUNCTIONS
# calculates avg value of rgb of a single pixel.
def compute_avg_rgb(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3

# sets the colour of a specific pixel. not used so far
def set_pixel_colour(pixel,rgb):
    for i in range(3):
        pixel[i] = rgb[i]

##################################### INIT RESULT

# opening the image
if testing:
    print(f'> Opening {image_file}...')

image = Image.open(image_file)

if testing:
    print(f'> Image details:')
    print(f'> Image Dimensions: {image.size}\n')
    print(f'> Resizing image [keep aspect ratio: {keep_aspect_ratio}]... ')

# resizing the image
if keep_aspect_ratio:
    image.thumbnail(dimensions) # image.thumbnail modifies the image and returns nothing so im not storing it in a variable.
    image = image.resize((dimensions[0],int(dimensions[1]/2)))
    if testing:
        print(f'> New dimensions: {image.size}')
else:
    image = image.resize(dimensions) # this does not modify but returns a new object hence I am storing it in a variable.
    if testing:
        print(f'> New dimensions: {image.size}')

# convert image into raw (numpy array) format
image_raw = np.array(image)

ascii_text = []

row_index = 0
for row in image_raw:
    # enter into the row.
    ascii_text.append([])
    for pixel in row:
        # enter into the pixel.
        avg_rgb = compute_avg_rgb(pixel)
        if avg_rgb < 30:
            ascii_text[row_index].append('█')
        elif avg_rgb < 135:
            ascii_text[row_index].append('▓')
        elif avg_rgb < 170:
            ascii_text[row_index].append('▒')
        elif avg_rgb < 200:
            ascii_text[row_index].append('░')
        elif avg_rgb < 240:
            ascii_text[row_index].append('.')
        else:
            ascii_text[row_index].append(' ')
    
    row_index += 1

if display_ascii_text:
    for row in ascii_text:
        for ascii_key in row:
            print(ascii_key,end='')
        print('')

# just for testing
if display_image:
    # convert image into displayable format
    im = Image.fromarray(image_raw)
    # display image
    im.show()
