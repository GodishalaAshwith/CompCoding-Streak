# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    oddCount = 0
    for i in a:
        if i%2==1:
            oddCount+=1
    if oddCount>0 and sum(a)%2==0 :
        print("YES")
    else:
        print("NO")