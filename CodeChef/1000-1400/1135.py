# cook your dish here
for _ in range(int(input())):
    g = int(input())
    for i in range(g):
        i, n, q = map(int,input().split())
        res = n//2 + abs(i-q)*n%2
        print(res)    
  