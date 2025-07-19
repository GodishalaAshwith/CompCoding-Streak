from collections import Counter

def canDivide(n,s):    
    frq = Counter(s)
    for i in frq.values():
        if i%2==1:
            return "NO"
    return "YES"
    
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    print(canDivide(n,s))
    