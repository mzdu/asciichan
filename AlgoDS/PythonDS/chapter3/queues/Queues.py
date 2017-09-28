__author__ = "MingzheDu"

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        # Please reference insertVSconcatenate.py
#        self.items = [item] + self.items
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    
    
#testQ = Queue()
#testQ.enqueue(12)
#testQ.enqueue(23)
#print testQ.dequeue()
#print testQ.isEmpty()
#print testQ.size()