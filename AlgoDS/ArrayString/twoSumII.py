def twoSumII(nums, target):
    # nums is a sorted list
    
    lenOfNums = len(nums)
    index1, index2 = 0, 0
    for i in range(lenOfNums):
        index2 = lenOfNums - i - 1
        
        if nums[index2] + nums[index1] <= target:
            break
        
    # print index1, index2    
    # get the value of index1 and index2
    for index1 in range(index2 + 1):
        if nums[index1] + nums[index2] == target:
            print 'found, and the result is:'
            return index1, index2
            
        else:
            print 'not found'
            
            
nums = [2,3,4,5,7,9,11]
target = 11

print twoSumII(nums, target)
            