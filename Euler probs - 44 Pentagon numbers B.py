# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 16:13:15 2015

@author: JKandFletch
"""


import time

start = time.time()

def genPent():
    pent = 0
    n = 1

    while True:
        pent = n * (3 * n - 1)/2
        yield pent
        n += 1

pentNum = genPent()

pentNums = [pentNum.next()]
pentSet = set()
addSet = pentSet.add
addSet(pentNums[0])
addList = pentNums.append

for i in range(2):
    temp = pentNum.next()
    addList(temp)
    addSet(temp)

solved = False
thisMax = len(pentNums)-1
minNum = 100000000
minPair = [0, 0]

while not solved:
    for i in range(thisMax):
        value1 = pentNums[thisMax - 1]
        value2 = pentNums[i]
        diff = value1 - value2
        if diff in pentSet:
            total = value1 + value2
            target = max(pentNums)
            while total >= target:
                target = pentNum.next()
                addList(target)
                addSet(target)
            if total in pentSet:
                print value1, value2,
                print 'DONE'
                print value1 - value2
                if diff < minNum:
                    minNum = diff
                    minPair = [value1, value2]
                solved = True
            elif total > 100000000:
                solved = True
                break
    thisMax += 1
    while thisMax > len(pentNums):
        temp = pentNum.next()
        addList(temp)
        addSet(temp)

print time.time() - start
