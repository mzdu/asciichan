class Node:
    def __init__(self,initdata):
        self.data = initdata
#It is always a good idea to explicitly assign None to your initial next reference values.
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
        
    def setNext(self,newnext):
        self.next = newnext
        
class UnorderedList:
    def __init__(self):
        self.head = None

        
temp = Node(93)
print temp.getData()
