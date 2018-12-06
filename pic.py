import os


class Pic:
    def __init__(self, f):
        self.__filename = f

        self.__file_base_name = None
        self.__file_base_name, _ = os.path.splitext(self.__filename)

        self.__input_filename = os.path.join('input', f)
        self.__output_file = os.path.join('output', self.__file_base_name + '.jpg')

    @property
    def input_filename(self):
        return self.__input_filename

    @property
    def output_file(self):
        return self.__output_file
