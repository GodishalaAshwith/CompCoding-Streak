# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a =  sorted(list(map(int,input().split())))
    ans = []
    for i in range(n):
        if i%2 == 0:
            ans.append(a.pop(0))
        else:
            ans.append(a.pop())
    print(*ans)