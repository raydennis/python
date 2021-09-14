#! /usr/bin/python

try:
    f = open("/etc/hosts")
    # go ahead and read the file
except FileNotFoundError:
    print("no hosts file")
