# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 14:44:27 2015

@author: JKandFletch
"""

#       
def getMatrix(filename):

    currentLine = ''
    currentRow = []
    matrix = []
    
    with open(filename, 'r', 1) as fileIn:
        for line in fileIn.readlines():
            currentLine = line.rstrip()
            currentRow = currentLine.split()
            for (i,value) in enumerate(currentRow):
                currentRow[i] = int(value)
            matrix.append(currentRow)
            
    return matrix
            
def diagUp(m, n):
    result = []
    
    for i in range(4):
        result.append([m - i + 3, n + i])

    return result

def diagDown(m, n):
    result = []
    
    for i in range(4):
        result.append([m + i, n + i])

    return result        

def side(m, n):
    result = []
    
    for i in range(4):
        result.append([m, n + i])
        
    return result

def down(m, n):
    result = []
    
    for i in range(4):
        result.append([m + i, n])
        
    return result
               
            
filename = "C:/Users/JKandFletch/Documents/Joe Play/Code/Euler probs - 11 grid product.txt"
maxResult = 0
currentResult = 1
f = [diagUp, diagDown, side, down]

grid = getMatrix(filename)

for row in range(17):
    for column in range(17):
        for funct in f:        
            currentResult = 1
            for combo in funct(row,column):
                currentResult = currentResult * grid[combo[0]][combo[1]]
            #print currentResult
            if currentResult > maxResult:
                maxResult = currentResult
                
print maxResult