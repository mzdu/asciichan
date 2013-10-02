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
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
#        if len(self.items) == 0:
#            return True
#        else:
#            return False
    
    def size(self):
        return len(self.items)
    

st1 = Stack()
st1.push('12')
st1.push('a')
print st1.peek()