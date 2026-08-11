#solution 1
class Solution(object):
    def majorityElement(self, nums):
        count = {}
        res , maxCount= 0 ,0
        for n in nums:
            count[n] = 1 + count.get(n,0)
            if count[n] > maxCount :
                res = n
            else :
                maxCount= max(count[n], maxCount) 
        return res   

#solution 2 boyer-moore algorithm
class Solution(object):
    def majorityElement(self, nums):
        res , count = 0 , 0
        for i in nums:
            if count == 0 :
                res = i
            count += (1 if i == res else -1)
        return res         
            

            