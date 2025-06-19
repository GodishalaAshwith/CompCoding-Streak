class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        
        partitions = 0
        start = 0 
        for end in range(len(nums)):

            if nums[end] - nums[start] > k:
                partitions += 1
                start = end  
            
        return partitions + 1