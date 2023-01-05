# Automate the Boring Stuff chapter 8
# Mad Libs assignment
# Mischa van den Burg

from pathlib import Path
import re

# ask the user which file to open
file_name = input('Enter the filename. For example, grammar.txt: ')

# my script and .txt file are located in ~/python/automatetheboringstuff/Chapter9
text_file = open(Path.home() / 'python' / 'automatetheboringstuff' / 'Chapter9' / file_name )

# read the file and store in variable & close
source_text = text_file.read()
text_file.close()

# set up and match the regex
grammar_regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
match_regex = grammar_regex.findall(source_text)

# replace the matches with user input
for i in match_regex:
    ask_user = input('Enter ' + i + ': ')
    source_text = source_text.replace(i, ask_user, 1)

# write to the new file and print the result
new_file = open('new_' + file_name, 'w')
new_file.write(source_text)
new_file.close()

print(source_text)





