class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        max = 0
        for i in range(-1,len(nums)-1):
            if nums[i]-nums[i+1]>max:
                max = nums[i]-nums[i+1]
            elif nums[i+1]-nums[i]>max:
                max = nums[i+1]-nums[i]
        return max