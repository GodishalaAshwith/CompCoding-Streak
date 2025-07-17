# cook your dish here
for _ in range( int(input())):
    n,x,c = map(int, input().split())
    a = list(map(int, input().split()))
    counter = 0
    for i in range(n):
        if a[i]<x and (x-a[i] >c):
            a[i]=x
            counter+=1
    print(sum(a)-(counter*c))