#!/usr/bin/python
def reverse(x):
    xToStr = str(abs(x))
    reverseString = ""
    for i in range(0, len(xToStr)):
        reverseString = reverseString + xToStr[len(xToStr) - (i + 1)]
        strToInt = int(reverseString)
    print(strToInt)

reverse(2341)

