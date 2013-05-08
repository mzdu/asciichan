# search a number from sorted list
# target = x, List1 = [1,2,3,4,5,6,7,8,9,10,11,12]
# Use divide and conquer strategy

import math

# # def search1(target, List1):
# #     middle_index = int(math.ceil(len(List1)/2)) - 1
# #     print middle_index
# #     if target == List1[middle_index]:
# #         print 'Find it! The index is:', middle_index, "."
# #     elif target > List1[middle_index]:
# #         print 'elifa'
# #         search1(target, List1[middle_index+1:])
# #     else:
# #         print 'ela'
# #         search1(target, List1[:middle_index])
# #     
# # search1(4,[1,2,3,4])

def bsearch(s, e, first, last):
    print first, last
    if (last-first) < 2:
        return s[first] == e or s[last] == e 
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid-1)
    return bsearch(s, e, mid+1, last)

def search1(s, e):
    print bsearch(s, e, 0, len(s)-1)
    print 'search complete'
    
search1([1,2,3,4], 4)            