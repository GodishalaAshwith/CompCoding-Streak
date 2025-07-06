# cook your dish here
for _ in range(int(input())):
    n , x , y = list(map(int,input().split()))
    attacks = 2*(n-1) + min(x-1,y-1) + min(x-1,n-y) + min(n-x,y-1) + min(n-x,n-y)
    print(attacks)