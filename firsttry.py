from PIL import Image
import os


def get_aspect(im):
    x, y = im.size
    if x > y:
        return 'landscape'
    elif y > x:
        return 'portrait'
    else:
        return 'square'


def get_longest_side(aspect):
    if aspect == 'portrait':
        return 'y'
    elif aspect == 'landscape':
        return 'x'
    else:
        return 'x'


for f in os.listdir('input'):
    print(f'{f}')
    filename = os.path.join('input', f)
    print(f'{os.path.abspath(filename)}')
    im = Image.open(f'{filename}')

    aspect = get_aspect(im)
    print(f'{aspect}')

    longest_side = get_longest_side(aspect)
    print(f'longest_side: {longest_side}')


# 800x600
# jpg, avi
# ttl 1GB
