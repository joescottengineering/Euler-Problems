# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 17:36:57 2015

@author: JKandFletch
"""


results = []

for n in range(2, 1001):
    sequence = False
    temp = 1
    dividends = {}
    places = ''

    while not sequence:
        next = int(temp/n)
        while next == 0:
            if temp == 0:
                break
            places += '0'
            temp *= 10
            next = int(temp/n)
        if temp in dividends:
            sequence = True
            length = len(places) - dividends[temp]
            results.append([n, length, places])
        else:
            dividends[temp] = len(places)            
            temp = (temp - (n * next)) * 10

        if temp == 0:
            sequence = True
            places += str(next)
            results.append([n, 0, places])
        else:
            places += str(next)

results.sort(key=lambda results:results[1], reverse=True)

print results[:5]
