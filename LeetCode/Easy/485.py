class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0
        for i in nums:
            if i == 1:
                curr+=1
            else:
                res = max(curr,res)
                curr = 0
        return max(res,curr)