#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    copy = a
    newA = []

    for i in range(d-1,len(a)-1):
        newA.insert(0,copy[-1])
        copy.pop()
    
    for numLeft in copy:
        newA.insert(len(newA),numLeft)

    return newA

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
