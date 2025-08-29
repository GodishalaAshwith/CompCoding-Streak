class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = 0
        n = 1
        res = [None]*len(nums)

        for i in nums:
            if i > 0:
                res[p] = i
                p+=2
            else:
                res[n] = i
                n+=2
        return res