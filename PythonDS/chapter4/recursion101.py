    # calculate the sum of list with a recursion method.

listI1 = [1,2,3,4,5,6,7]

def calculateSum(listI):

    if listI != []:
        return listI.pop() + calculateSum(listI)
    else:
        return 0


print calculateSum(listI1)