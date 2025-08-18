for _ in range(int(input())):
    a, b = map(int,input().split())
    flag = False
    difference = b-a
    if b%a==0:
        print('YES')
    else:
        if a<=difference:
            print('YES')
        else:
            print('NO')