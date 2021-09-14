import glob
import os


def rename(folder, fromExt, toExt):
    fromExt = "*" + fromExt
    for filename in glob.iglob(os.path.join(folder, fromExt)):
        try:
            os.rename(filename, filename[:-4] + toExt)
        except ValueError:
            print("unable to convert " + filename)


rename('/Users/rsdenni/tmp/trainings/markdown/', '.md', '.org')
# rename('/Users/rsdenni/tmp/trainings/markdown/', '.org', '.md')
