class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data 
    
    def setData(self, newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def setNext(self,newNode):
        self.next = newNode
        
class UnorderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.next == None
    
    def add(self,data):
        tempNode = Node(data)
        tempNode.setNext(self.head)
        self.head = tempNode
        
    def search(self,data):
        # current is a pointer indicates the current node.
        current = self.head
        found = False
        
        while current!= None and not found:
            if current.getData() == data:
                found = True
                
            else:
                current = current.getNext()
                
        return found
    
    def remove(self,data):
        
        current = self.head
        previous = None
        found = False
        
#        while current!= None and not found:
#            if current.getData() == data:
#                previous.setNext(current.getNext())
#                found = True
#                
#            else:
#                previous = current
#                current = current.getNext()
#                
#        return found

        while current!= None and not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
            
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
    
    def size(self):
        current = self.head
        counter = 0
        while current!=None:
            counter = counter + 1
            
            current = current.getNext()
            
        return counter
    
#append, insert, index, and pop


    
            