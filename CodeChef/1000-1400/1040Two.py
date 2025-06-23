for _ in range(int(input())):
    n=int(input())
    s=input()
    if n%2!=0:
        print('NO')
    else:
        c=0
        v=''.join(set(s))
        for x in v:
            if s.count(x)%2==0:
                c+=1
            else:
                f=0
                break
        if c==len(v):
            print("YES")
        elif f==0:
            print('NO')