#Author: Shefali Kulkarni
#Date: June 14, 2020.

import numpy as np;

def calcFibList(flist):
    flist[0] = 0
    flist[1] = 1
    #compute the first 60 fibonacci numbers
    for i in range(2,61):
        flist[i] = flist[i-1] + flist[i-2]
    # save the ones digit or the last digit of every number in the sequence
    #done using modulus vector operation on flist array. Division by 10.
    flist = np.mod(flist,10)
    return flist;

#Calculate the last digit of the nth fibonacci numbers.
def calcLastDigit(n):
    fibList = [0]*61
    fibList = calcFibList(fibList)
    #The last digit of fibonacci numbers has a sequence of 60 numbers.
    # Then the sequence repeats.
    print('Fibonacci sequence number: ',n,'\t Last digit is: ',fibList[n%60])
n = 62
calcLastDigit(n)
n = 80
calcLastDigit(n)
n = 11111
calcLastDigit(n)
n = 100
calcLastDigit(n)
