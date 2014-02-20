# This is my wrong insertion sort version, for the next step, please reference insertionSort.py
alist = [2,4,5,1,7,12,6,32]

def insertionsort(alist):
    """idx is used to indicate the index of key
       subidx is used to indicate the index of target
    """
    idx = 1
    
    while idx < len(alist):
        key = alist[idx]
        print "key values is", key
        
        
        for subidx in range(len(alist[:idx])):
            if key > alist[subidx]:
                print "skip it"
                pass
            else:
                """
                rearrange alist[subidx:idx+1]
                """
                print "rearranging alist[subidx:idx+1]"
                idx2 = idx
                
                print "at this time, subidx is",subidx,"and idx is",idx
                while idx2 > subidx:
                    print "move alist[",idx2-1,"] to alist[",idx2,"]"
                    alist[idx2] = alist[idx2-1]
                    
                    idx2 -= 1
                    
                alist[subidx] = key
                print "one sort is done and alist is", alist
                
        idx += 1
        print "alist is ", alist
    print alist

insertionsort(alist)