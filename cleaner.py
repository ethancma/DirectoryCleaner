import os
import glob

file_name = 'my_file.txt'
file_name2 = 'my_file.py'

exts = set()
_, ext = (os.path.splitext(file_name))
exts.add(ext)
_, ext = (os.path.splitext(file_name2))
exts.add(ext)

for ext in exts:
    print(ext)


def get_extensions() -> set():
    files = 

print(get_extensions())
