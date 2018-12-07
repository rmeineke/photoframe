# chk for the various directories...

import os

from pic import Pic
from PIL import Image


def resize_image(filename):
    size = (800, 600)
    try:
        im = Image.open(filename)
        im.thumbnail(size, Image.ANTIALIAS)
        print(f'resizing . . . ')
        return im
    except IOError:
        print("cannot create thumbnail for " + {filename})


def composite_image(infile):
    bg = Image.open('background.png')
    in_x, in_y = infile.size
    bg.paste(infile, ( int((800 - in_x) / 2) , int((600 - in_y) / 2)) )
    print(f'compositing . . . ')
    return bg


def main():
    for f in os.listdir('input'):
        pic = Pic(f)
        resized = resize_image(pic.input_filename)
        resized.convert('RGB')
        composited = composite_image(resized)
        composited.save(pic.output_file, 'JPEG')


if __name__ == '__main__':
    main()
