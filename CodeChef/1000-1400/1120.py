import sys
from math import ceil
for _ in range(int(sys.stdin.readline())):
    n,b,m=map(int,sys.stdin.readline().split())
    r,i=0,0
    while n!=0:
        r+=ceil(n/2)*m*(2**i)
        n//=2
        i+=1
    r+=b*(i-1)
    sys.stdout.write(str(r)+'\n')