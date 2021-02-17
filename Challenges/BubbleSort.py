#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for i in range(len(a)):    
        for j in range(len(a)-1):    
        # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]): 
                swap = a[j]
                a[j] = a[j + 1]
                a[j + 1] = swap
                swaps += 1
    print('Array is sorted in ' + str(swaps) + ' swaps.')
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a.pop()))
        
    
    


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
