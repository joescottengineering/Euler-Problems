# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 21:20:40 2015

@author: JKandFletch
"""


def mirror(num):
    temp = str(num)
    tempR = ''

    for i in range(1, len(temp) + 1):
        tempR = tempR + temp[-1 * i]

    return(int(tempR))


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

result = []

for i in range(1, 10000):
    n = 0
    candidate = i
    match = False
    while n < 50 and not match:
        n += 1
        candidate = candidate + mirror(candidate)
        if isPalindrome(str(candidate)):
            match = True

    if n == 50:
        result.append(i)

print len(result)
