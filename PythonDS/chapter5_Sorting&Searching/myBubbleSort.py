def myBubbleSort(alist):
    i = 0
    j = 1
    sol = len(alist)
    
    while i < sol:
        print 'outloop'
        while j < sol:
            print 'insideloop'
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
                j = j + 1
                print 'swap here'
                print alist
                
            else:
                j = j + 1
                print 'no swap needed'
                
        print 'done with a loop'
        
        # reset j =1 for the next inside loop, I made a mistake here
        j = 1
        # cut the size of alist, and rearrange the n-1 elements
        sol = sol - 1
        
list1 = [12,3,5,6,2,88,9,0,45]
myBubbleSort(list1)
print list1