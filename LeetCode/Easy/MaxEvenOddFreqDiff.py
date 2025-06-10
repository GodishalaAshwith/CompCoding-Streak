from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        
        odd_freqs = [v for v in freq.values() if v % 2 != 0]
        even_freqs = [v for v in freq.values() if v % 2 == 0]

        if not odd_freqs or not even_freqs:
            return -1  # No valid (odd, even) pair

        return max(odd_freqs) - min(even_freqs)

s =Solution()
print(s.maxDifference(input()))