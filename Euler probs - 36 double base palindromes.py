# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 20:49:39 2015

@author: JKandFletch
"""


def isPalindrome(numAsString):
    '''
    takes a number and determines if it is a palindrome
    '''
    if len(numAsString) == 1 or len(numAsString) == 0:
        return True
    elif (numAsString[0] == numAsString[-1]):
        return isPalindrome(numAsString[1:-1])
    else:
        return False

doublBase = []

for i in range(1, 1000001):
    if isPalindrome(str(i)):
        binStr = str(bin(i))
        if isPalindrome(binStr[2:]):
            doublBase.append(i)

print doublBase
print sum(doublBase)
