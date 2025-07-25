n, k = map(int, input().split())
time = 240 - k
res = 0
i = 1
while i <= n and time >= i * 5:
    time -= i * 5
    res += 1
    i += 1
print(res)
