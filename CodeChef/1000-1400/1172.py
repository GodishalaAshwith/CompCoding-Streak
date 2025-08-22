# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    temp = set()
    maxID = 0
    for i in a:
        if i not in temp:
            temp.add(i)
            if len(temp)>maxID:
                maxID = len(temp)
        else:
            temp.remove(i)
                
    print(maxID)