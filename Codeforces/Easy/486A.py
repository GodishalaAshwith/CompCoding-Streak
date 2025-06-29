import math
n = int(input())
oddN = math.ceil(n/2)
evenN = math.floor(n/2)
res = evenN*(evenN+1) - oddN**2
print(res)