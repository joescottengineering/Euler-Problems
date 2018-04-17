# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 21:10:17 2015

@author: JKandFletch
"""

                 
def isleapYear(year):
    '''
        returns true if given year is a leap year, False otherwise
    '''
    
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
               

numDays = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31,
                 'June':30, 'July':31, 'August':31, 'September':30, 'October':31,
                 'November':30, 'December':31}

months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
                  'September', 'October', 'November', 'December' ]
year = 1900
yearsToGo = 100
numSundays = 0
remainder = 0

for years in range(yearsToGo+1):
    thisYear = year + years
    thisCalendar = []
    for month in months:
        if month == 'February' and isleapYear(thisYear):
            thisCalendar.append(numDays[month] + 1)
        else:
            thisCalendar.append(numDays[month])
    for i, days in enumerate(thisCalendar):
        #print thisYear, months[i], days
        if remainder == 1:
            numSundays += 1
            #print thisYear, months[i]         
    
        tempdays = days - remainder
        while tempdays > 7:
            tempdays -= 7
#            print months[i], tempdays
        if tempdays > 0:
            remainder = 7 - tempdays
        else:
            remainder == 0
        
#        print thisYear, months[i], remainder
#        
#    print thisYear, numSundays

print thisYear, numSundays - 2