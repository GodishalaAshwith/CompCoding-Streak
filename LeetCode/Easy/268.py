from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = int((n*(n+1))*0.5)
        actualSum = sum(nums)
        return expectedSum - actualSum