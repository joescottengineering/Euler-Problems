# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 21:22:32 2015

@author: JKandFletch
"""

from collections import Counter


cardScores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
handScores = ('High card', 'One pair', 'Two pairs', 'Three of a kind',
              'Straight', 'Flush', 'Full house', 'Four of a kind',
              'Straight flush', 'Royal flush')


class Handerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


class pokerHand(object):

    def __init__(self):
        self.cards = []
        self.values = []
        self.suits = []
        self.type = ''
        self.score = -1

    def getValues(self):
        return self.values

    def getType(self):
        return self.type

    def getScore(self):
        return self.score

    def getCards(self):
        return self.cards

    def addCard(self, string):
        if len(self.cards) > 4:
            raise Handerror("Too Many Cards!")

        self.cards.append(string)

        value = string[0]
        suit = string[1]

        self.values.append(cardScores[value])
        self.suits.append(suit)

    def scoreHand(self):
        if len(self.cards) != 5:
            raise Handerror("Don't have five cards!")

        self.values.sort(reverse=True)
        flush = isFlush(self.suits)
        straight = isConsecutive(self.values)

        if flush or straight:
            if not flush:
                self.type = 'Straight'
            elif not straight:
                self.type = 'Flush'
            elif max(self.values) == 14:
                self.type = 'Royal flush'
            else:
                self.type = 'Straight flush'
        else:
            self.type, self.values = returnMatches(self.values)

        self.score = handScores.index(self.type)


def isConsecutive(listNums):
    tempList = listNums[:]
    tempList.sort()
    consecutive = True
    if tempList == [2, 3, 4, 5, 14]:
        return consecutive

    for i in range(1, len(tempList)):
        if tempList[i] - tempList[i-1] == 1:
            continue
        else:
            consecutive = False

    return consecutive


def isFlush(listSuits):
    flush = True

    for i in range(1, len(listSuits)):
        if listSuits[i] == listSuits[i-1]:
            continue
        else:
            flush = False

    return flush


def returnMatches(listNums):
    thisSet = Counter(listNums)
    freq = thisSet.most_common()
    matchType = ''
    sortedList = []
    tempList = []

    if freq[0][1] == 1:
        matchType = 'High card'
        sortedList = listNums[:]
        sortedList.sort(reverse=True)
        return (matchType, sortedList)
    elif freq[0][1] == 2:
        if freq[1][1] == 2:
            matchType = 'Two pairs'
        else:
            matchType = 'One pair'
    elif freq[0][1] == 3:
        if freq[1][1] == 2:
            matchType = 'Full house'
        else:
            matchType = 'Three of a kind'
    elif freq[0][1] == 4:
        matchType = 'Four of a kind'

    for i in range(len(freq)):
        tempFreq = freq[i][1]
        if tempFreq > 1:
            for j in range(tempFreq):
                sortedList.append(freq[i][0])
        else:
            tempList.append(freq[i][0])

    if len(sortedList) < 5:
        tempList.sort(reverse=True)
        sortedList = sortedList + tempList

    return (matchType, sortedList)


results = []
playerOneWins = 0
numHands = 0
filename = 'Eulerprobs - 54 poker.txt'

with open(filename, 'r') as file:
    for line in file.readlines():
        winner = 'Push'
        playerOne = pokerHand()
        playerTwo = pokerHand()
        numHands += 1

        for i, card in enumerate(line.split()):
            if i < 5:
                playerOne.addCard(card)
            else:
                playerTwo.addCard(card)

        playerOne.scoreHand()
        scoreOne = playerOne.getScore()
        typeOne = playerOne.getType()

        playerTwo.scoreHand()
        scoreTwo = playerTwo.getScore()
        typeTwo = playerTwo.getType()

        if scoreOne > scoreTwo:
            playerOneWins += 1
            winner = 'Player1'
        elif scoreTwo > scoreOne:
            winner = 'Player2'
        else:
            handOne = playerOne.getValues()
            handTwo = playerTwo.getValues()

            for i in range(5):
                if handOne[i] == handTwo[i]:
                    continue
                elif handOne[i] > handTwo[i]:
                    playerOneWins += 1
                    winner = 'Player1'
                    break
                else:
                    winner = 'Player2'
                    break

            print typeOne, handOne, typeTwo, handTwo, winner

        results.append(winner)

print playerOneWins, numHands
