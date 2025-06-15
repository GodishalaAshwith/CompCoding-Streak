class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        max_val = 0
        min_val = float('inf')
        
        for x in '0123456789':
            for y in '0123456789':
                # Skip if replacing x by y causes leading zero
                if x == y:
                    continue
                temp = num_str.replace(x, y)
                if temp[0] == '0':
                    continue
                temp_num = int(temp)
                max_val = max(max_val, temp_num)
                if temp_num != 0:
                    min_val = min(min_val, temp_num)
        
        return max_val - min_val
