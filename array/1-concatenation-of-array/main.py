class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for n in range(2):
            for i in nums:
                ans.append(i)
        return ans