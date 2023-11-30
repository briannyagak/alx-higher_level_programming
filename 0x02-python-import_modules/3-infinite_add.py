#!/usr/bin/python3
import sys
a = 0
n = len(sys.argv)
for x in range(1, n):
    a += int(sys.argv[x])
print(a)
