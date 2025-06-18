import math
# cook your dish here
for i in range(int(input())):
    x,y = list(map(int,input().split()))
    if math.gcd(x,y)!=1:
        print(0)
    elif math.gcd(x+1,y)>1 or math.gcd(x,y+1) >1:
        print(1)
    else:
        print(2)
    