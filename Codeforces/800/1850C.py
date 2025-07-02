for _ in range(int(input())):
    a = []
    for _ in range(8):
        a.append(list(input()))
        
    res = []
    for i in range(len(a)):
        for j in a[i]:
            if j.isalpha():
                res.append(j)
                
    print("".join(res))
