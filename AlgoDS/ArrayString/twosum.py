class Solution:
    def twoSum(self, nums, target):
        lookup = dict()
        for i, number in enumerate(nums):
            if target - number in lookup:
                return [lookup[target-number] + 1, i + 1]
                
            else:
                lookup[number] = i