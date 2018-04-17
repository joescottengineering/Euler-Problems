# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 20:24:55 2015

@author: JKandFletch
"""


import time

start = time.time()


def compareNumDigits(num1, num2):

    numStr1 = list(str(num1))
    numStr2 = list(str(num2))
    numStr1.sort()
    numStr2.sort()
    numStr1 = str(numStr1)
    numStr2 = str(numStr2)

    if numStr1 == numStr2:
        return True
    else:
        return False


nextUp = 1000
solved = False

while not solved:
    candidate = nextUp
    for i in range(1, 7):
        temp = candidate * i
        if compareNumDigits(candidate, temp):
#            print i, candidate, temp
            solved = True
        else:
            solved = False
            break
    nextUp += 1


print nextUp
print time.time() - start
