"""
Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than 100MB.
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.

Solution by Mischa van den burg
www.mischavandenburg.com
"""

from pathlib import Path, PurePath
import os

source = Path(Path.home() / 'Downloads' )
for folder_name, sub_folder, file_names in os.walk(source):
    for file_name in file_names:
        p = PurePath(folder_name, file_name)
        bytes = os.path.getsize(p)
        size = bytes / 1048576
        if size > 100:
            print(file_name + " " + "size: "  + str(round(size)) + "MB")


