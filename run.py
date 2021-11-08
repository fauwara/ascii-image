import sys
import time

# a is the array of ascii art of each frame  
def run(a):
    # clear screen before printing art
    sys.stdout.write(chr(27)+'[2j' + '\033c \x1bc')

    while 1:
        for i in range(len(a)):
            try:
                sys.stdout.write(a[i])

                time.sleep(0.1)
                sys.stdout.write(chr(27)+'[2j' + '\033c \x1bc')
            except KeyboardInterrupt:
                print('*aqua crying noises*')
                sys.exit(0)