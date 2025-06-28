t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    pos1 = p.index(1)
    posN = p.index(n)
    
    if pos1 < posN:
        print(pos1 + (n - 1 - posN))
    else:
        print(pos1 + (n - 1 - posN) - 1)
