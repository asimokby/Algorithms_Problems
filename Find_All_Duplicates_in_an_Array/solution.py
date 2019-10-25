class Solution(object):
    def findDuplicates(self, nums):
        d = {}
        res = []
        for i in nums: 
            if i in d:
                res.append(i)
            else: 
                d[i] = 1
        return res
