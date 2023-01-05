import os

title = input("Enter title: ")

filename = f"{title}.md"
command = f"nvim ~/obsidian/second-brain/0-inbox/{filename}"

os.system(command)
