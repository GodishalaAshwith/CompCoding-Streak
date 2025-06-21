from collections import Counter
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    card = max(set(a), key=a.count)
    a = [i for i in a if i!=card]
    print(len(a))