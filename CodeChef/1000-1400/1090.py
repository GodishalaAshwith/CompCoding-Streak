# cook your dish here
for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    res = [max(i-1,m-i) for i in a]
    print(sum(res))