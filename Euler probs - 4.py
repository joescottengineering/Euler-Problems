# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:01:14 2015

@author: JKandFletch
"""

def isPalindrome (numAsString):
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

for i in range(1000,0,-1):
    for j in range(1000,0,-1):
        if isPalindrome(str(i*j)):
            result.append(i*j)
            
            
print max(result)
print result