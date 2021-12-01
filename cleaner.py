import os
import glob


class DirectoryCleaner(object):
    
    def __init__(self):
        self.names = list()


    def file_names(self) -> set():
        """
        Adds all file extensions in current path excluding directories to self.names.
        """
        exts = {os.path.splitext(i)[1] for i in os.listdir() if os.path.isfile(i)}
        for i in exts:
            self.names.append(i[1:])

    
    def create_dir(self):
        """
        Creates new directories with file extension names given in self.names.
        """
        for i in self.names:
            try:
                os.makedirs(i)
            except:
                print(f"Folder name with \'{i}\' already exists.")

a = DirectoryCleaner()
a.file_names()
a.create_dir()
