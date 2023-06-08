#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    if len(sys.argv) <= 1:
        print("0")
    else:
        i, sum = 1, 0
        while i < (len(sys.argv)):
           sum = sum + int(sys.argv[i])
           i = i + 1
        print("{}".format(sum))
