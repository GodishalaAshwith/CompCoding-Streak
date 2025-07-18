from collections import Counter
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        frq = Counter(nums)

        frqKeys = list(frq.keys())
        n = len(frq.keys())
        res = 0
        i = 0

        while i < n-1 :
            if abs(frqKeys[i] - frqKeys[i+1]) == 1:
                if res< frq[frqKeys[i]]+frq[frqKeys[i+1]]:
                    res = frq[frqKeys[i]]+frq[frqKeys[i+1]]
            i+=1 

        return res