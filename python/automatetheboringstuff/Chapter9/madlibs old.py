# Mad Libs assignment
# A program that reads a text file and replaces text

from pathlib import Path

# the file is located in a directory 'python' located in my home directory
textfile = open(Path.home() / 'python' / 'grammar.txt')

# read the file and split up into words
source_text = textfile.read().split()
result_text = []

print(textfile)

def period_check(x):
    for letter in x:
        if letter == ".":
            return True

# loop over the array and prompt user

for word in source_text:

    period = False

    if period_check(word):
        word = word.replace(".", "")
        period = True

    if word == 'ADJECTIVE':
        invoer = input('Enter a verb: ')
        if period:
            result_text.append(invoer + ".")
            period = False
        else:
            result_text.append(invoer)
    elif word == 'NOUN':
        invoer = input('Enter a verb: ')
        if period:
            result_text.append(invoer + ".")
            period = False
        else:
            result_text.append(invoer)
    elif word == 'ADVERB':
        invoer = input('Enter a verb: ')
        if period:
            result_text.append(invoer + ".")
            period = False
        else:
            result_text.append(invoer)
    elif word == 'VERB':
        invoer = input('Enter a verb: ')
        if period:
            result_text.append(invoer + ".")
            period = False
        else:
            result_text.append(invoer)
    else:
        result_text.append(word)

a = " "
print(a.join(result_text))


