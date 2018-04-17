# -*- coding: utf-8 -*-
"""
Created on Thu Feb 05 20:53:51 2015

@author: JKandFletch
"""

import itertools


def isPandigit(a):
    check = ''

    thisNum = ''.join(sorted(str(a)))

    for i in range(1, len(thisNum)+1):
        check = check + str(i)

    if thisNum == check:
        return True
    else:
        return False


def stitches(tupe):
    result = ''
    for i in tupe:
        result += str(i)
    return int(result)


triangles = {}
tri = 1
tempList = [1]

for i in range(2, 10):
    tri += i
    tempList.append(i)
    triangles[tri] = tempList[:]

solution = {}
maxPan = 0

for i in range(10000, 0, -1):
    tempResult = ''
    for j in range(1, 10):
        tempResult += str(i * j)
        if len(tempResult) < 9:
            continue
        elif len(tempResult) == 9:
            # print tempResult
            if isPandigit(tempResult):
                solution[int(tempResult)] = ([i, j])
        else:
            break

for answer in solution.keys():
    if answer > maxPan:
        maxPan = answer

print maxPan
print solution[maxPan]
