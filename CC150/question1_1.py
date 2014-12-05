# implement an algorithm to determine if a string has all unique characters. what if you cannot use additional data structures?


s1 = 'abcedfg'

def isUnique(s1):
    for i in range(len(s1)):
      # if s1[i] in s1[i+1:]
      for j in range(i+1, len(s1)):
        if s1[i] == s1[j]:
          return False
      # else
      pass
    
    return True

print isUnique(s1)