#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 1:
    print("0 arguments.")
elif n == 2:
    print('1 argument:')
    print(f'1: {sys.argv[1]}')
else:
    print(f'{n - 1} arguments:')
    for x in range(1, n):
        print(f'{x}: {sys.argv[x]}')
