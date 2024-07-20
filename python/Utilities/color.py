# script that prints out 256 color codes
# from https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")
