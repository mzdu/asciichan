def binary_to_decimal(number):
    # use stack to keep the left
    stack = []
    res = []
    while number // 2 > 0:
        left = number % 2
        stack.append(left)
        number = number // 2
        
    stack.append(number)
    
    #use pop to reverse the output
    res = ''
    while stack:
        res += str(stack.pop())
        
    return res
    
print binary_to_decimal(8)