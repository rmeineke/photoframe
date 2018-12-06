import os


class Pic:
    def __init__(self, f):
        self.__filename = f
        self.__file_base_name = None
        self.__file_ext = None

        self.__full_file_name = os.path.abspath(f)
        self.__file_base_name, self.__file_ext = os.path.splitext(self.__filename)

        self.__output_file = os.path.join('output' + self.__file_base_name + '.jpg')


    @property
    def filename(self):
        return self.__full_file_name

    @property
    def ext(self):
        return self.__file_ext

    @property
    def stub(self):
        return self.__file_base_name