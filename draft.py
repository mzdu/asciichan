def singleNumber(A):
    while A:
        number = A.pop()
        if number in A:
            A.pop(A.index(number))
        else:
            return number
        
alist = [1,0,1]
print singleNumber(alist)