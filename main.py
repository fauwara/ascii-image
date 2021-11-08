import random
import os
import getopt
import sys
from aqua import aqua
from run import run

# python3 main.py 1 2

# reading arguments and options
argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, 'g:m:s:', ['gif=', 'map='])
except getopt.GetoptError:
    print('the option does not exist or is mispelled.')
    sys.exit(0)

# random gif, if arg is not passed
gif = random.randrange(1,3)

# mapping ascii chars
asciiChars = ['@#S%?*+;:,. ', ' .:-=+*#%@', ' .,:;+*?%S#@']
mapIndex = 1

# size of ascii art if size argument is not passed
size = os.get_terminal_size()
size = (size[0]-1, size[1])

for opt, arg in opts:
    # gif option
    if opt in ['-g', '--gif']:
        try:
            arg = int(arg)
            if arg > 0 and arg <= len(os.listdir('./aqua')): 
                gif = int(arg)
            else: 
                print(f'gif {arg} does not exist.')
                sys.exit(0)
        
        except ValueError:
            print('gif option must be an integer value')
            sys.exit(0)

    # map option
    elif opt in ['-m', '--map']:
        try:
            arg = int(arg)
            if arg >= 0 and arg < len(asciiChars): 
                mapIndex = int(arg)
            else: 
                print(f'index {arg} out of bounds')
                sys.exit(0)
        
        except ValueError:
            print('map option must be an integer value')
            sys.exit(0)

# generates the ascii art
asciiAqua = aqua(gif, size, asciiChars[mapIndex])
run(asciiAqua)