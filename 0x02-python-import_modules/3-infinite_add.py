#!/usr/bin/python3
import sys
if __name__ == '__main__':
    a = 0
    n = len(sys.argv)
    for x in range(1, n):
        a += int(sys.argv[x])
    print(a)
