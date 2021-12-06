import os
import glob
import shutil


class DirectoryCleaner(object):

    def __init__(self):
        self.names = list()

    def file_names(self):
        """
        Adds all file extensions in current path to self.names.
        """
        files = os.listdir()
        exts = {os.path.splitext(i)[1] for i in files if os.path.isfile(i)}
        for i in exts:
            self.names.append(i[1:])

    def create_dir(self):
        """
        Creates new directories with file extension names given in self.names.
        """
        for i in self.names:
            try:
                os.makedirs(i)
                print(f"Created {i} directory.")
            except Exception:
                print(f"Folder name with \'{i}\' already exists.")

    def move_files(self, ext: str):
        """
        Moves files into new directories specified by file extension.
        """
        for i in glob.glob('*.' + ext):
            try:
                if (os.path.isdir(os.getcwd() + f'/{ext}')):
                    shutil.move(i, ext)
            except Exception:
                print(f"Folder \'{ext}\' has not been created yet.")
                break


a = DirectoryCleaner()
a.file_names()
