# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    skip = 0
    
    for i in range(n-1):
        skip += abs(s[i]-s[i+1])-1
    print(skip)