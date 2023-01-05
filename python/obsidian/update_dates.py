# a script to add markdown links to my daily notes

from pathlib import Path, PurePath
import os

day = 12

file_name_prefix = "2022-09-"

for i in range(day, 31):
    file_name = f"{file_name_prefix}{i}.md"
    note_path = PurePath('/home/mischa/obsidian/second-brain/periodic notes/daily notes').joinpath(file_name)

    yesterday = f"[[{file_name_prefix}{i - 1}]]"
    tomorrow = f"[[{file_name_prefix}{i + 1}]]"

    with open(note_path, 'a') as f:
        f.write('\n')
        f.write(yesterday + '\n')
        f.write(tomorrow + '\n')
