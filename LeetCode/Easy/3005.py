class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = Counter(nums)
        maxFrq = max(f.values())
        return sum(v for i,v in f.items() if v==maxFrq)