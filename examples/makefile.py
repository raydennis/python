# OLD way
# import os

# for x in range(0, 5):
#     os.system("touch test" + str(x) + ".txt")


# updated way
from pathlib import Path
from posix import listdir

# create the file
Path('file.txt').touch()

# call list directory
# exec(open("listdir.py").read())
