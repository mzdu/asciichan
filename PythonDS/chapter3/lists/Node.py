class Node:
    def __init__(self,initdata):
        self.data = initdata
#It is always a good idea to explicitly assign None to your initial next reference values.
        self.next = None
        
    def getData(self):
        return self.data
    
    # getNext is to get the next NODE, not the data
    # which means via getNext(), you get the next Node.
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
    
    # set your POINTER to the next NODE
    def setNext(self,newnext):
        self.next = newnext
        