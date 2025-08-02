# cook your dish here
t = int(input())

while t > 0:
    n = int(input())
    c = int(0)
    m = int(0)
    for i in range(n):
        a,b = map(str,input().split())
        a  = sum(map(int,a))
        b  = sum(map(int,b))
        if a>b:
            c+=1
        elif a<b:
            m+=1
        else:
            c+=1
            m+=1
    if c>m:
        print('0',c)
    elif c<m:
        print('1',m)
    else:
        print('2',c)
    t-=1