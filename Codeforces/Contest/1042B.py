for _ in range(int(input())):
    n = int(input())
    res = []
    for i in range(n):
        if i%2==1 and i==n-1:
            res.append(2)
        elif i%2==0:
            res.append(-1)
        else:
            res.append(3)
    print(*res)  