class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)
    
    
minStack = MinStack()
minStack.push(1)
minStack.push(10)
minStack.push(100)
minStack.push(2)
minStack.push(22)

print minStack.getMin()
print minStack.pop()
