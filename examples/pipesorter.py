#!/usr/bin/python3

# Demonstrate piping into and out of a child process

from subprocess import Popen, PIPE
import random

sorter = Popen(["sort", "-nr"], stdin=PIPE, stdout=PIPE)

# Write 10 random integers to the sorter's input
for i in range(10):
    sorter.stdin.write(("%d\n" % random.randrange(9000)).encode())

# Without the close() below, this will hang because
# the sorter will never see EOF on it's standard input
sorter.stdin.close()

for line in sorter.stdout:
    print(line.decode(), end='')
