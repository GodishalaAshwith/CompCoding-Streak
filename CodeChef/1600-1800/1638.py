from sympy import *

t=int(input())
for i in range(t):
    x=int(input())
    L=[]
    while len(L)<2:
        if isprime(x):
            L.append(x)
        x+=1
    print(L[0]*L[1])