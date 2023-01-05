"""
Automate the Boring Stuff Chapter 10
Selective Copy assignment solution

Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.

Solution by Mischa van den Burg
www.mischavandenburg.com
04-02-2022
"""

from pathlib import Path, PurePath
import os, re, shutil

# set the desired directories here
source = Path(Path.home() / 'python' / 'automatetheboringstuff' / 'test_tree')
destination = Path(Path.home() / 'python' / 'automatetheboringstuff' / 'chapter10' / 'copiedfiles')

# compile the type of file extension. change to txt or pdf etc. if desired
regex = re.compile(r"\.txt$")

# walk the folder
for folder_name, sub_folder, file_names in os.walk(source):
    for filename in file_names:
        if regex.search(filename):
            p = PurePath(folder_name, filename)
            print('Copying file: ' + filename)
            shutil.copy(p, destination)

print('Finished.')
