from collections import Counter
x,y,z = map(int,input().split())

l1 = [int(input()) for _ in range(x)]
l2 = [int(input()) for _ in range(y)]
l3 = [int(input()) for _ in range(z)]

combinedList = l1+l2+l3

frq = Counter(combinedList)
finalList = [i for i,j in frq.items() if j>1]