class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s: str, first: str, second: str, score: int) -> (str, int):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return ''.join(stack), total
        
        if x > y:
            # Remove "ab" first, then "ba"
            s, gain1 = remove_pattern(s, 'a', 'b', x)
            _, gain2 = remove_pattern(s, 'b', 'a', y)
        else:
            # Remove "ba" first, then "ab"
            s, gain1 = remove_pattern(s, 'b', 'a', y)
            _, gain2 = remove_pattern(s, 'a', 'b', x)
        
        return gain1 + gain2