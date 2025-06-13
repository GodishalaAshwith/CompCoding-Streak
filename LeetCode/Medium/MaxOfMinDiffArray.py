from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_form_pairs(max_diff):
            i = 0
            count = 0
            while i < len(nums) - 1:
                if abs(nums[i+1] - nums[i]) <= max_diff:
                    count += 1
                    i += 2  # skip both elements (non-overlapping pair)
                else:
                    i += 1
            return count >= p

        left = 0
        right = nums[-1] - nums[0]
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
