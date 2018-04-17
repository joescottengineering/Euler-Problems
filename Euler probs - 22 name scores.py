# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 19:55:29 2015

@author: JKandFletch
"""
import csv

def getScore(scores, name):
    score = 0
    for char in name:
        score += scores[char]
    return score

filename = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Eulerprobs - 22 names.txt'

nameList = []
letterScores = {}
totalSum = 0

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, letter in enumerate(letters):
    letterScores[letter] = i + 1
    
print letterScores

with open(filename) as csvfile:
    namesText = csv.reader(csvfile, quotechar = '"')
    for names in namesText:
        for name in names:
            nameList.append(name)

nameList.sort()

for i, name in enumerate(nameList):
    totalSum += (i + 1) * getScore(letterScores, name)
    
print totalSum