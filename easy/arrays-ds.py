#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    if len(a) == 0 or len(a) == 1:
        return a
        
    for i in range(len(a) // 2):
        # print(i)
        # print(len(a) - i)
        a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
    return a

reverseArray([1, 4, 3, 2])