#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substringCalculator' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#

def substringCalculator(s):
    # Write your code here
    n = len(s)
    
    if n <= 1:
        return n
        
    cur = s[0] # 'ab'
    cnt = 0
    
    dic = {}
    
    for i in range(n-1):
        for j in range(i+1, n+1):
            sub_str = s[i:j]
            
            if dic.get(sub_str) is None:
                dic[sub_str] = 1
                cnt += 1

    if dic.get(s[-1]) is None:
        dic[sub_str] = 1
        cnt += 1                

    print(dic)
                
    return cnt+1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = substringCalculator(s)

    fptr.write(str(result) + '\n')

    fptr.close()


