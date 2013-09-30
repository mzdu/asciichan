import time

"""
One string is an anagram of another if the second is simply a rearrangement of the first. 
For example, 'heart' and 'earth' are anagrams. 
The strings 'python' and 'typhon' are anagrams as well. 
"""

"""Assume that two strings are of equal length."""

__author__ = "MingzheDu"

"""Solution1: Checking Off"""
def anagramDetection1(str1,str2):
    # O(n2)
    # convert str2 to a list, from immutable to mutable
    alist = list(str2)
    pos1 = 0
    
    while pos1 < len(str1):
        pos2 = 0
        while pos2 < len(alist): 
            if str1[pos1] == alist[pos2]:
                print "found one"
                alist.pop(pos2)
                
            else:
                pos2 = pos2 + 1
        pos1 = pos1 + 1
    
    if len(alist) == 0:
        return True
    else:
        return False

"""Solution2: Sort and Compare"""
"""Another solution to the anagram problem will make use of the fact that even though s1 and s2 are different, 
they are anagrams only if they consist of exactly the same characters. 
So, if we begin by sorting each string alphabetically, from a to z, 
we will end up with the same string if the original two strings are anagrams."""

def anagramDetection2(str1,str2):
    # from the running time, we may see func1 and func2 are consuming the same time
    # Thus, the time complexity is O(n2)
    alist1 = sorted(list(str1))
    alist2 = sorted(list(str2))
    
    if alist1 == alist2:
        return True
    else:
        return False
    

"""Solution 4: Count and Compare"""
"""
In order to decide whether two strings are anagrams, 
we will first count the number of times each character occurs.
"""
def anagramDetection4(str1,str2):
    # time complexity is O(n)
    alist1 = [0]*26
    alist2 = [0]*26
    
    for i in range(len(str1)):
        pos = ord(str1[i]) - ord('a')
        alist1[pos] = alist1[pos] + 1
    
    for i in range(len(str2)):
        pos = ord(str2[i]) - ord('a')
        alist2[pos] = alist2[pos] + 1
        
    j = 0
    stillOK = True
    while j<26 and stillOK:
        if alist1[j] == alist2[j]:
            j = j + 1
        else:
            stillOK = False
    return stillOK





str1 = 'printOK'*100
str2 = 'OKprint'*100


start1 = time.time()
print anagramDetection1(str1,str2)
end1 = time.time()
print "The time of Detection1 is %10.7f" %(end1-start1)

start2 = time.time()
print anagramDetection2(str1,str2)
end2 = time.time()
print "The time of Detection2 is %10.7f" %(end2-start2)

start3 = time.time()
print anagramDetection4(str1,str2)
end3 = time.time()
print "The time of Detection1 is %10.7f" %(end3-start3)