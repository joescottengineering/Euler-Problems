# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:50:37 2015

@author: JKandFletch
"""

filename = 'C:/Users/JKandFletch/Documents/Joe Play/Code/'\
    'Eulerprobs - 67 path sum.txt'

triangle = []
nodeCollect = {}

with open(filename, 'r') as file:
    for line in file.readlines():
        templist = []
        for item in line.split():
            templist.append(int(item))
        triangle.append(templist)

totalRows = len(triangle)

for row in range(totalRows-2, -1, -1):
    for col in range(len(triangle[row])):
        tempOne = triangle[row + 1][col] + triangle[row][col]
        tempTwo = triangle[row + 1][col + 1] + triangle[row][col]
        triangle[row][col] = max([tempOne, tempTwo])

print triangle[0][0]
