weights = list(map(int,input().split()))
i = 0
while i >= 0:
    if (weights[0]>weights[1]):
        break
    else:
        weights[0]*=3
        weights[1]*=2
        i+=1
print(i)