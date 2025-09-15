# cook your dish here
from collections import Counter

dp = [[0] * 55 for _ in range(55)]
dp[0][0] = 1

for i in range(1, 51):
    dp[i][0] = 1
    for j in range(1, 51):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

# Input test cases
t = int(input())

while t > 0:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = Counter(a)

    a.sort()

    ptr = k - 1
    val = 0
    while ptr >= 0 and a[ptr] == a[k-1]:
        ptr -= 1
        val += 1
    res = dp[freq[a[k-1]]][val]
    print(res)

    t -= 1