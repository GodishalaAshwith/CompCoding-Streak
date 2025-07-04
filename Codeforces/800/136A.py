n = int(input())
p = list(map(int, input().split()))
res = [0] * n

for giver in range(n):
    receiver = p[giver]
    res[receiver - 1] = giver + 1

print(' '.join(map(str, res)))
