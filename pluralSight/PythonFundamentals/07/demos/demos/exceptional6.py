def convert(s):
    '''Convert a string to an integer.'''
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except (ValueError, TypeError):
        print("Conversion failed!")
    return x
