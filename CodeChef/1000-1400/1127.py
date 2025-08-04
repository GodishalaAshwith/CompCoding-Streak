for _ in range(int(input())):
    p = list(map(int,input().split()))
    a = input()
    s = 0
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(l)):
        if(l[i] not in a):
            s += p[i] 
    print(s)