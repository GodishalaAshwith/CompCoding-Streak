import math
for _ in range(int(input())):
    n = int(input())
    fn = (0.143*n)**n 
    if fn - math.floor(fn)<0.5:
        print(math.floor(fn))
    else:
        print(math.floor(fn)+1)