from typing import List
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            d = 2
            while d*d<=x:
                if x%d==0:
                    s.add(x)
                    while x5d==0: x//=d
                d+=1 if d==2 else 2
            if x>1: s.add(x)
        return len(s)