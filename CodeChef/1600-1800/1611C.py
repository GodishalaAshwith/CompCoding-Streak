from collections import Counter

for AJDO in range(int(input())):
    n, W, w = map(int, input().split())
    l = list(map(int, input().split()))
    ans = "NO"
    if (W <= w):
        ans = "YES"
    d = Counter(l)
    arr = list(d.items())
    for i in range(len(arr)):
        arr[i] = (arr[i][0], (arr[i][1] // 2) * 2)
    for x, y in arr:
        w += (x * y)
    if (W <= w):
        ans = "YES"
    print(ans)



