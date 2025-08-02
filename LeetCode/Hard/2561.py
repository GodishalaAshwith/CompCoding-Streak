class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter1 = Counter(basket1)
        counter2 = Counter(basket2)
        the_smallest = min(basket1 + basket2)

        for k in counter1.keys():
            while counter1[k] > 0 and counter2[k] > 0:
                to_remove = min(counter1[k], counter2[k])
                counter1[k] -= to_remove
                counter2[k] -= to_remove
        
        for v in list(counter1.values()) + list(counter2.values()):
            if v % 2 == 1:
                return -1
        
        to_move1 = []
        for k in counter1.keys():
            to_move1.extend([k] * (counter1[k]//2))
        to_move2 = []
        for k in counter2.keys():
            to_move2.extend([k] * (counter2[k]//2))
        to_move1, to_move2 = sorted(to_move1), sorted(to_move2)[::-1]

        ans = 0
        for i in range(len(to_move1)):
            ans += min(to_move1[i], to_move2[i], the_smallest*2)
        
        return ans
        