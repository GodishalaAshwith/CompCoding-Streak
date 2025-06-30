# cook your dish here
for _ in range(int(input())):
    n,a = list(map(int,input().split()))
    if a == 0:
        print(0)
    elif n-a > a:
        print(a)
    else:
        print(n-a)