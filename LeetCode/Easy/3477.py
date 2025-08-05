class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:


        for fruit in fruits:
            for idx, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets.pop(idx)
                    break
        
        return len(baskets)
