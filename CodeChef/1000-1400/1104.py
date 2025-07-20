t = int(input())

while t > 0:
    n = int(input())
    a = [int(p) for p in input().split()]
    g = [int(q) for q in input().split()]
    
    res_1 = all(a[i]<=g[i] for i in range(n))
    res_2 = all(a[i]<=g[n-(i+1)] for i in range(n))
    if res_1 and res_2 :
        print('both')
    elif res_1:
        print('front')
    elif res_2:
        print('back')
    else:
        print('none')
    t-=1