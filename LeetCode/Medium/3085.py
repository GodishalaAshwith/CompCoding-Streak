from collections import Counter

class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        freq = Counter(word)
        freq_values = list(freq.values())
        unique_freqs = sorted(set(freq_values))
        
        min_deletions = float('inf')

        for base in unique_freqs:
            deletions = 0
            for val in freq_values:
                if val < base:
                    deletions += val  # delete all
                elif val > base + k:
                    deletions += val - (base + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
