import Stacks

def divideBy2(decimalNumber):
    s = Stacks.Stack()
    
    while decimalNumber > 0:
        rem = decimalNumber % 2
        s.push(rem)
        decimalNumber = decimalNumber / 2

    binaryString = ""    
    while not s.isEmpty():
        binaryString = binaryString + str(s.pop())
    
    return binaryString



print divideBy2(13)