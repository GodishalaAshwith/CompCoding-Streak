# cook your dish here
for _ in range(int(input())):
    n = int(input())
    best = [0]*8
    for _ in range(n):
        p, s = map(int,input().split())
        if p > 8 :
            continue
        if best[p-1] < s:
            best[p-1] = s 
    print(sum(best))