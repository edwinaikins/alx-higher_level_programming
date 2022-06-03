#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = len(sys.argv) - 1
    if i == 0:
        print("{} argument.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
        for index in range(i):
            print("{}: {}".format(index + 1, sys.argv[index + 1]))
    else:
        print("{} arguments:".format(i))
        for index in range(i):
            print("{}: {}".format(index + 1, sys.argv[index + 1]))
