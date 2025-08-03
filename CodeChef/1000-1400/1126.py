from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    def solve(a):
        frq = Counter(a)
        for i in frq.keys():
            if frq[i]%2==1:
                return "NO"
        return "YES"
    print(solve(a))