__author__ = "MingzheDu"

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
#        return self.items[len(self.items)-1]
# Reverse index runs faster than loading len()
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
#        if len(self.items) == 0:
#            return True
#        else:
#            return False
    
    def size(self):
        return len(self.items)
    
