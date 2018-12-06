import os

from pic import Pic


def main():
    for f in os.listdir('input'):
        print(f'{f}')
        pic = Pic(f)
        print(f'{pic.filename}')
        print(f'{pic.stub}')
        print(f'{pic.ext}')

#
#
# def get_aspect(im):
#     x, y = im.size
#     if x > y:
#         return 'landscape'
#     elif y > x:
#         return 'portrait'
#     else:
#         return 'square'
#
#
# def get_longest_side(aspect):
#     if aspect == 'portrait':
#         return 'y'
#     elif aspect == 'landscape':
#         return 'x'
#     else:
#         return 'x'
#
#
# def resize_image(filename):
#     print(f'inside resize_image: {filename}')
#     outfile = 'sm_' + filename
#     print(f'outfile: {outfile}')
#     size = (800, 600)
#     try:
#         im = Image.open(os.path.join('input', filename))
#         im.thumbnail(size, Image.ANTIALIAS)
#         return im
#     except IOError:
#         print("cannot create thumbnail for " + {filename})
#
#
# def composite_image(infile):
#     bg = Image.open('background.png')
#     in_x, in_y = infile.size
#     bg.paste(infile, ( int((800 - in_x) / 2) , int((600 - in_y) / 2)) )
#     return bg
#
#
# for f in os.listdir('input'):
#     print(f'{f}')
#     file_stub, file_ext = os.path.splitext(f)
#     filename = os.path.join('input', f)
#     print(f'{os.path.abspath(filename)}')
#     resized = resize_image(f)
#
#     resized = resized.convert('RGB')
#     sm_file = f"{os.path.join('resized', 'sm_' + f)}"
#     resized.save(sm_file, "JPEG")
#
#     composited = composite_image(resized)
#     final_name = os.path.join('output', file_stub + '.jpg')
#     print(f'{final_name}')
#     composited.save(final_name, "JPEG")
# # 800x600
# # jpg, avi
# # ttl 1GB

if __name__ == '__main__':
    main()