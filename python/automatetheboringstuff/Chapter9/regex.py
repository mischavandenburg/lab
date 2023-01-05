from pathlib import Path
import re

# list all the textfiles in the ~/python/automatetheboringstuff/Chapter9 directory
p = Path(Path.home() / 'python' / 'automatetheboringstuff' / 'Chapter9' )
files_list = list(p.glob('*.txt'))

# compile the regex from user prompt
user_regex = re.compile(input('Enter your regex query: '))

# iterate over the files, match the regex, and print the matches in each file
for file in files_list:
    file_open = open(file)
    search_text = file_open.read()
    match_regex = user_regex.findall(search_text)
    for match in match_regex:
        print(match)
    file_open.close()
