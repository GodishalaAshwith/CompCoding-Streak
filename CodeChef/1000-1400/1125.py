for _ in range(int(input())):
    st=input()
    s=0
    for i in st:
        if i in '123456789': s+=int(i)
    print(s)