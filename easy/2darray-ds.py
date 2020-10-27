#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    if len(arr) < 2:
        return 0

    directions = [ # start from top left (0,0)
        (0, 1), (0, 2),
        (1, 1),
        (2, 0), (2, 1), (2, 2)
    ]
    maxSum = -9999999
    startPivot = (0, 0)
    for i in range(len(arr) - 2): # minus 2 to account for the height of hourglass
        row = arr[i]
        print("row: ", row)
        for j in range(len(row) - 2):
            startPivot = (i, j)
            curr = row[j] # elem
            print()
            print("start: ", startPivot, curr, row)
            for dir in directions:
                # print(dir)
                print((startPivot[0] + dir[0], startPivot[1] + dir[1]))
                new = arr[startPivot[0] + dir[0]][startPivot[1] + dir[1]]
                curr += new
                print("total: ", curr, " elem: ", new)
            if curr > maxSum:
                maxSum = curr

    print()
    print(maxSum)
    print(arr)
    return maxSum

hourglassSum([
    [-9, -9, -9, 1, 1, 1], 
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]
])

hourglassSum([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
])
