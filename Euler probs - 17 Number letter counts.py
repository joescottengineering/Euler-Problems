# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 19:58:28 2015

@author: JKandFletch
"""
digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens =  ['', teens, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

filename = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Eulerprobs - 17 Number letter counts.txt'        
f = open(filename, 'w')
 
thisNum = ''   
total = 0
prefix = ''

for hunDigit in digits:
    if hunDigit == '':
        prefix = ''
    else:
        prefix = hunDigit + 'hundred'
    for num in tens:
        if type(num) == list:
            for desc in num:
                if prefix == '':
                    thisNum = prefix + desc
                else:
                    thisNum = prefix + 'and' + desc
                total += len(thisNum)
                print thisNum
                f.write(thisNum + '\n')        
        
        
        else:
            for digit in digits:
                if (num == '' and digit == '') or prefix == '':
                    thisNum = prefix + num + digit
                else:
                    thisNum = prefix + 'and' + num + digit
    
                total += len(thisNum)
                print thisNum
                f.write(thisNum + '\n')

thisNum = 'onethousand'
print thisNum
f.write(thisNum)             
total += len(thisNum)

f.close()

print total

