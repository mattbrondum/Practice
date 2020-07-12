#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

print([i for i in range(2,-1,-1)])

def diagonalDifference(arr):
    # Write your code here
    n = len(arr[0])
    first_list = []
    second_list = []
    first_diag = [arr[i][i] for i in range(n)]
    second_diag = [arr[i][n-i-1] for i in range(n)]
    diff = abs(sum(first_diag) - sum(second_diag))
    return diff
if __name__ == '__main__':
    test_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diagonalDifference(test_array)















