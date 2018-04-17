# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 17:49:18 2015

@author: JKandFletch
"""

import csv

def getScore(scores, name):
    score = 0
    for char in name:
        score += scores[char]
    return score
    
def genTriangle():
    n = 1
    tri = 0
    
    while True:
        tri = tri + n
        yield tri
        n += 1
        
filename = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Eulerprobs - 42 words.txt'

wordList = []
letterScores = {}
totalSum = 0
genTris = genTriangle()
triList = [genTris.next()]
triCount = 0

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, letter in enumerate(letters):
    letterScores[letter] = i + 1
    
print letterScores

with open(filename) as csvfile:
    wordsText = csv.reader(csvfile, quotechar = '"')
    for words in wordsText:
        for word in words:
            wordList.append(word)
            
for word in wordList:
    score = getScore(letterScores, word)
    while score > max(triList):
        triList.append(genTris.next())
    if score in triList:
        triCount += 1

print triCount