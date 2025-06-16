from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [float('-inf')]*n
        for i in range(n):
            for j in range(i,n):
                if nums[j]>nums[i]:
                    if nums[j]-nums[i]>diff[i]:
                        diff[i]=nums[j]-nums[i]
        diff = [i for i in diff if i > 0]
        if diff:
            return max(diff)
        else:
            return -1