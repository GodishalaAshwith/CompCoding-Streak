# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    lt = len([x for x in a if x < 0])
    gt = len([x for x in a if x > 0])
    print(lt*(lt-1)//2 + gt*(gt-1)//2)