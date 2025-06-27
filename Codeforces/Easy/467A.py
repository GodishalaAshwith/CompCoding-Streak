available = 0
for _ in range(int(input())):
    p , q = list(map(int,input().split()))
    if p<=q-2:
        available +=1
    else:
        continue
print(available)