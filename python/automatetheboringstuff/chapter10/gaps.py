"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, 
and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps into numbered files 
so that a new file can be added.

Solution by Mischa van den Burg
www.mischavandenburg.com

Although this is a working solution, I am well aware that it is full of problems.
As it is now, it only handles the format of a word, 3 digits and file extension. 
I spent a week struggling with this assignment but now I finally solved it, I think I will come back to it later.
And maybe I will do the extra challenge then too. 
"""

from pathlib import Path, PurePath
import os, re, shutil

regex = re.compile(r"(([a-zA-Z])*)(([0-9])+)(\.txt)+$")
source = Path(Path.home() / 'python' / 'automatetheboringstuff' / 'chapter10' / 'textfiles' )

old_filenames = []
new_filenames = []
prefix = None
extension = None

for folder_names, sub_folders, file_names in os.walk(source):
    for file_name in file_names:
        pattern = regex.search(file_name)
        # grab the number and put into list
        old_filenames.append(pattern[3])
        # grap the prefix and file exension
        prefix = pattern[1]
        extension = pattern[5]

# take the list of file numbers, sort them in ascending order and grab the first number
old_filenames = sorted(old_filenames)
first_number = int(old_filenames[0])

# loop over the list and create a list of new numbers
for i in range(len(old_filenames)):
    # take first number and determine the next one, and turn into string 
    x = str(first_number + i)
    # the zfill method is used to add preceding 0
    new_filenames.append(prefix + x.zfill(3) + extension)

# now we have the new_filenames, loop through the directory and rename the files
# after struggling a lot with reading the original filenames, I discovered that os.walk()
# does not walk in a particular order. using sorted(file_names) fixed the problem, but it took a lot of time to figure it out

count = 0
for folder_name, sub_folders, file_names in os.walk(source):
    for file_name in sorted(file_names):
        destination = Path(source) / new_filenames[count]
        original = PurePath(folder_name, file_name)
        shutil.move(original, destination) 
        count += 1
