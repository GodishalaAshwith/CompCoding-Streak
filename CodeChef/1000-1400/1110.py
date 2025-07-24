# cook your dish here
for _ in range(int(input())):
    n, k = map(int,input().split())
    d = list(map(int,input().split()))
    ans = ''
    for i in d:
        ans += str(int(i%k == 0))
    print(ans)
    