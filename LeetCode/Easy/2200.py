from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i, val in enumerate(nums) if val == key]
        res = set()

        for j in key_indices:
            # Include all indices i where |i - j| <= k
            start = max(0, j - k)
            end = min(len(nums) - 1, j + k)
            for i in range(start, end + 1):
                res.add(i)

        return sorted(res)
