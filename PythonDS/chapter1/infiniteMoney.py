# Infinite Monkey Theorem
from __future__ import division
import random


def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res

def score(goal,teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame += 1
    
    return numSame/len(goal)

def main():
    goalstring = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring,newstring)
    while newscore < 1:
        if newscore > best:
            print newscore,newstring
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring,newstring)
        
main()