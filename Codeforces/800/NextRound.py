n,k = map(int,input().split())
a = list(map(int,input().split()))
kth = a[k-1]
qual = len([i for i in a if i>=kth and i>0])
print(qual)