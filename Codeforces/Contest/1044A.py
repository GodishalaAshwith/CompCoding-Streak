from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    frq = Counter(a)

    if any(i > 1 for i in frq.values()):
        print("Yes")
    else:
        print("No")