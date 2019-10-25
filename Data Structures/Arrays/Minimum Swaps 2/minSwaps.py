#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    counter = 0

    ph = [0]*(len(arr))

    for index,val in enumerate(arr):
        
        ph[val-1] = index


    for i in range(len(arr)):
        if (arr[i]) != i+1:
            l = ph[i] 
            
            arr[i],arr[l] = i+1,arr[i]
            
            ph[i],ph[arr[l]-1] = i,l
            
            counter += 1
        print("Pass #: " + str(counter))
        for j in range(len(arr)):
            print(arr[j])
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    res = minimumSwaps(arr)
    
    fptr.write(str(res) + '\n')

    fptr.close()
