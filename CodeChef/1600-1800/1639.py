for _ in range(int(input())):
    # n=int(input())
    n, k = map(int, input().split())
    ans = set()
    for _ in range(n):
        x = int(input(), 2)
        if (x and (not (x & (x - 1)))):
            ans.add(x)
    if len(ans) == k:
        print('Yes')
    else:
        print('No')



