__author__ = "MingzheDu"

"""
 A palindrome is a string that reads the same forward and backward, 
 for example, radar, toot, and madam. 
"""

import Deque

def palChecker(aString):
    
    chardeque = Deque.Deque()
    
    for ch in aString:
        chardeque.addRear(ch)
        
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        
        if last != first:
            stillEqual = False
    
    return stillEqual

print palChecker('radar')        