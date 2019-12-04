import pdb


def main():
    list = [1, 2, 3]
    pdb.set_trace()
    list = [2, 3, 4]
    pdb.set_trace()
    print(list)


if __name__ == '__main__':
    main()
