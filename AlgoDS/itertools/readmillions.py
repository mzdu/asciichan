# alist = iter(range(1, 100000000000000)) # Memory Error

# x = iter(alist)
# 
# num = 1
# while num:
#   num = next(x, None)
#   if num:
#     print num


# 
# for num in alist:
#     print num
#     
    
    
def loadMill():
    import itertools
#     alist = xrange(1, 100000000000000)
    iterObj = itertools.cycle(range(1, 100000000000000))
    
    while True:
        num = next(iterObj, None)
        if not num:
            break
        else:
            print num
    
    
#     for num in alist:
#         print num

print 'started'
print loadMill()