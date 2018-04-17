# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 21:34:03 2015

@author: JKandFletch
"""

import math
import itertools

def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

numStr = ''
number = []
flag = False

for i in range(9,1,-1):
    numStr = ''
    for j in range(i, 0, -1):
        numStr = numStr + str(j)
#    print numStr
    number = list(itertools.permutations(numStr))
    for thisSet in number:
        thisPan = ''.join(thisSet)
#        print thisPan
        if isPrime(int(thisPan)):
            print thisPan
            flag = True
            break
    if flag:
        break
