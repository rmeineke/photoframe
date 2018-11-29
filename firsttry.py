from PIL import Image
import os


def get_aspect(im):
    x, y = im.size
    if x > y:
        aspect = 'landscape'
    elif y > x:
        aspect = 'portrait'
    else:
        aspect = 'square'
    return aspect


for f in os.listdir('input'):
    print(f'{f}')
    filename = os.path.join('input', f)
    print(f'{os.path.abspath(filename)}')
    im = Image.open(f'{filename}')

    aspect = get_aspect(im)
    print(f'{aspect}')

# 800x600
# jpg, avi
# ttl 1GB
