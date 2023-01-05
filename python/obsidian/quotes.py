from pathlib import Path
import frontmatter
import random
import smtplib
import ssl
from secrets import mail_password
path = Path('/home/mischa/obsidian/second-brain/kindle-highlights')

# A script that scans my Kindle highlights located in my
# Obsidian vault and sends me an email with the highlight.
# I run this every day in a cronjob to get inspiration from my past reading.

def get_author(input_file):
    post = frontmatter.load(input_file)
    try:
        return post['kindle-sync']['author']
    except Exception:
        return "Unknown author"


def get_title(input_file):
    post = frontmatter.load(input_file)
    try:
        return post['kindle-sync']['title']
    except Exception:
        return "Unknown title"

# get all the files and make a list


file_list = []


for file in path.iterdir():
    if file.is_file():
        file_list.append(file)

# choose a random file
chosen_file = random.choice(file_list)

# get all quotes from file
quote_list = []
with open(chosen_file, "r") as f:
    for line in f:
        if line.startswith("\""):
            quote_list.append(line)

# prepare data to be sent
chosen_quote = random.choice(quote_list).replace("\"", '')
author_title = f"{get_author(chosen_file)}, {get_title(chosen_file)}"

# set up mail server
port = 465
from_email = ""
to_email = ""
context = ssl.create_default_context()
message = f"""\
From: {from_email}
Subject: Your Daily Quote
{chosen_quote}
{author_title}

With love from Python.
"""

with smtplib.SMTP_SSL("email", port, context=context) as server:
    server.login(from_email, mail_password)
    server.sendmail(from_email, to_email, message.encode('utf-8'))
