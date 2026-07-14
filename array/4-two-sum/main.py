class Solution(object):
    def twoSum(self, nums, target):
        numset = {}
        for i , n in enumerate(nums) :
            diff = target - n
            if diff in numset :
                return [numset[diff] , i]
            numset[n]= i
"""
used enumerate - i-index , n-value

"""            