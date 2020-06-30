#!/usr/bin/env python
inputFile = "input.txt"
outputFile = "output.txt"
findString = "Orange"
replaceString = "A"

with open(inputFile) as fin:
    with open(outputFile, "wt") as fout:
        for line in fin:
            fout.write(line.replace(findString, replaceString))

