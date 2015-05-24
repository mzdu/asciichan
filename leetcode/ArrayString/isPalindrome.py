class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        
        if len(s) < 2:
            return True
            
        characterList = 'abcdefghijklmnopqrstuvwxyz1234567890'
        s = s.lower()
        temp = []
        for element in s:
            if element in characterList:
                temp.append(element)
        
        i, j = 0, len(temp) - 1
        while i < j:
            if temp[i] == temp[j]:
                i += 1
                j -= 1
            else:
                return False
                
        return True