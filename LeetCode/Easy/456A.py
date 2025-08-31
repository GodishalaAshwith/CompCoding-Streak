class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        frnds = set(friends)
        res = []
        for i in order:
            if i in frnds:
                res.append(i)
        return res