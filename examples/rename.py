#!/usr/bin/env python

from datetime import datetime
import os
import glob

files = "~/tmp/*.md"
markdown_files = glob.glob(files)

for file_name in sorted(markdown_files):
    old_name_split = file_name.split('_', 1)
    try:
        new_date = datetime.strptime(old_name_split[0], '%y%m%d') \
                .strftime('%Y-%m-%d')
        old_name_split[0] = new_date
        s = "_"
        os.rename(file_name, s.join(old_name_split))
    except ValueError:
        print("unable to convert " + file_name + " (invalid date format)")
