__author__ = 'MingzheDu'
"""
Self Check
Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. O(n2). 
The second function should be linear O(n).
"""
import time
import random

start = time.time()

def findMin1(list1):
# complextiy of O(n)    
    minNum = list1[0]
    for i in range(0,len(list1)):
        if list1[i] <= minNum:
            minNum = list1[i]
        else:
            continue
    
    return minNum

def findMin2(list1):
# complexity of O(n2)
    minNum = list1[0]
    for i in range(0,len(list1)):
        for j in range(0,len(list1)):
            if (list1[j]<=list1[i]) and (list1[j]<=minNum):
                minNum = list1[j]
            else:
                continue
    return minNum

def generateList(listlen):
    list1 = []
    while listlen > 0:
        num1 = random.randint(1,100)
        list1.append(num1)
        listlen = listlen - 1
        print list1
        
    return list1
    
tempList = generateList(10)

print findMin1(tempList)
print findMin2(tempList)        
end = time.time()

print end-start   