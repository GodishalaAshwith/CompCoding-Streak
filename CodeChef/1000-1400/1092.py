from collections import Counter

def isHappy(n, p):
    freq = Counter(p)
    for i in freq:
        if freq[i] % i != 0:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    print(isHappy(n, p))