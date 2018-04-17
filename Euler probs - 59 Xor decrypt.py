# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 10:29:37 2015

@author: JKandFletch
"""


import string
import csv
import collections


def decrypt(num, key):
    result = int(num) ^ key
    return result


keys = []
characters = string.ascii_lowercase
validChars = string.printable
validStart = string.ascii_letters + '"' + "'"
filename = 'Eulerprobs - 59 XOR cipher.txt'
wordFile = 'words.txt'

decryptList = []
wordList = []
firstPass = []
badChars = []
count = 0
sumAscii = 0
passage = ''

for i in characters:
    for j in characters:
        for k in characters:
            keys.append((ord(i), ord(j), ord(k)))


inFile = open(wordFile, 'r')
wordList = inFile.read().split()

with open(filename, 'r') as csvfile2:
    decryptText = list(csv.reader(csvfile2))
    decryptText = decryptText[0]
    decryptFreq = collections.Counter(decryptText)

print len(decryptText)

#modes = decryptFreq.most_common(5)
#
#for mode in modes:
#    char = chr(int(mode[0]))
#    for letter in characters:
#        print char + " = " + str(ord(char)),
#        print chr((ord(letter) ^ ord(char)))

for key in keys:
    testLine = ''
    match = True
    count = 0
    for num in range(400):
        keyNum = num % 3
        decChar = decrypt(decryptText[num], key[keyNum])
        newChar = chr(decChar)        
        if newChar not in string.letters:
            count += 1
        else:
            testLine = testLine + newChar
    firstPass.append((key, count, testLine))

firstPass.sort(key=lambda tup: tup[1])

#print firstPass[:9]

newKey = firstPass[0][0]

for i, char2 in enumerate(decryptText):
    keyNum2 = i % 3
    decChar2 = decrypt(char2,newKey[keyNum2])
    sumAscii += decChar2
    passage += chr(decChar2)

print passage
print sumAscii

#
#result = {}
#
#for key2 in firstPass:
#    decoded = ''
#    for num, char in enumerate(decryptText):
#        keyNum = num % 3
#        newChar = decrypt(decryptText[num], key2[keyNum])  
#        decoded = decoded + newChar
#        if (num == 20):
##            print decoded
#            break
#    result[key2] = decoded
#        
#print result