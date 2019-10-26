#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    myDict = {}
    
    for i in range(len(s1)):
        letter = s1[i]
        myDict[letter] = "this letter exists"
    
    for j in range(len(s2)):
        letter = s2[j]
        if letter in myDict:
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
