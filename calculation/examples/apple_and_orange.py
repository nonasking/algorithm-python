# apple and orange(Hackerrank)
# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    def is_fall_in(standard, distance):
        if s <= standard + distance <= t:
            return True
        return False
    
    apple_count = 0
    for apple_distance in apples:
        if is_fall_in(a, apple_distance):
            apple_count += 1
    orange_count = 0
    for orange_distance in oranges:
        if is_fall_in(b, orange_distance):
            orange_count += 1
    
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
