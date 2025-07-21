from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    frq = Counter(a)
    maxFrq = max(frq.values())
    mostRecommended = [i for i,j in frq.items() if j==maxFrq]
    if len(mostRecommended) > 1:
        print("CONFUSED")
    else:
        print(*mostRecommended)