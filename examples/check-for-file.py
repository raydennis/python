#! /usr/bin/python

try:
    f = open("/etc/hosts")
    # go head and read the file
except FileNotFoundError:
    print("no hosts file")
