# cook your dish here
def digsum(s):
    count = 0
    for d in s:
        count += int(d)
    return count
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    max = 0
    for i in range(n-1):
        for j in range(i+1,n):
            test = digsum(str(a[i]*a[j]))
            if max < test:
                max = test
    print(max)            
            
    