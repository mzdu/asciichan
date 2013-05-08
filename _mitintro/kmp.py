# try to implement KMP algorithm
# Ref: http://blog.jobbole.com/39066/

# Knuth-Morris-Pratt string matching
# David Eppstein, UC Irvine, 1 Mar 2002

from __future__ import generators

def KnuthMorrisPratt(text, pattern):

    '''Yields all starting positions of copies of the pattern in the text.
Calling conventions are similar to string.find, but its arguments can be
lists or iterators, not just strings, it returns all matches, not just
the first one, and it does not need the whole text in memory at once.
Whenever it yields, it will have read the text exactly up to and including
the match that caused the yield.'''

    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos


#
#def preprocess(target):
#    dict1 = {}
#    counter = 0
#    
#    for element in target:
#        if dict1[element] == 0:
#            dict1[element] = 1
#        else:
#            counter = dict1[element]
#            dict1[element] = counter + 1
#
#    print dict1
#            
#print preprocess(target)
#
#
#def kmp1(str1, target):
#    
#    counter1 = 0
#    counter2 = 0
#    letterlist = []
#    for counter1 in range(len(target)):
#        if str1[counter1] == target[counter1]:
#            print 'yes, keep on going'
#            if str1[counter1] == target[counter2]
#            
#            
#        else:
#            print 'damn, searching again.'
#            