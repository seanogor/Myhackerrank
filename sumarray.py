#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum=0
    for item in ar:
        if item > 1000:
            print("%s is too large a value".format(item))
        elif item != 0:
            sum=sum+item
            print("The running total is %s".format(sum))
        else:
            print("The array element is not valid, please edit and retry")
    return sum

    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
