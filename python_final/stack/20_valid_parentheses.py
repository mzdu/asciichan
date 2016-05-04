"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        # use stack to track the parentheses
        leftparts = {"(":")", "{":"}", "[":"]"}
        # if incoming parenthese is not the top of stack return false
        stack = list()
        for element in s:
            if element in leftparts:
                stack.append(leftparts[element])
                
            elif element in leftparts.values():
                if len(stack) < 1:
                    return False
                if stack.pop() != element:
                    return False
            else:
                pass
        
        if len(stack) == 0:
            return True
        else:
            return False