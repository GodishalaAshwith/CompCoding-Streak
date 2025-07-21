for _ in range(int(input())):
    n = list(input())
    n.reverse()
    res = []
    for i in range(len(n)):
        if n[i]!="0":
            res.append(n[i]+"0"*i)
    print(len(res))
    print(*res)