import glob
# glob supports Unix style pathname extensions

python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print('    ------' + file_name)

    with open(file_name) as f:
        for line in f:
            # rstrip removes [arg] from the end of the string
            print('    ' + line.rstrip())

    print
