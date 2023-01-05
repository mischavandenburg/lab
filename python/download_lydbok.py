# small script to download audio files from a website ( pelsjegerliv bok )
import os
import time
url = 'https://lydbok.to/books_storage/n107/'

for i in range(1, 118):
    a = str(i)
    b = a.zfill(3)
    c = f"curl -O {url}{b}.mp3"
    os.system(c)
    time.sleep(5)


# os.system('curl -O https://lydbok.to/books_storage/n107/001.mp3')
