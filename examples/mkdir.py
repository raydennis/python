'''
playing with directories in Python


the inspect module can be used to get information on specific files
but you can also use __file__ if you're only looking for
the current running directory
'''

import os
import unittest
from pathlib import Path
# from inspect import currentframe, getframeinfo


def make_directory(directory):
    os.mkdir(directory)
    if Path(directory).exists():
        # following lines needed if you're using inspect module
        # filename = getframeinfo(currentframe()).filename
        # parent = Path(filename).resolve().parent

        parent = str(Path(__file__).resolve().parent)
        print("directory created: " + parent + "/" + directory)


class TestMakeDirectory(unittest.TestCase):
    def test_make_directory(self):
        directory = "testMakeDirectory"
        make_directory(directory)
        self.assertTrue(Path(directory).exists())
        os.rmdir(directory)

if __name__ == "__main__":
    unittest.main()