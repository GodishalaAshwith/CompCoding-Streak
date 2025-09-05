# cook your dish here
import functools

def xor(a,b):
    return a^b
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n%2:
        print('yes')
    else:
        if functools.reduce(xor,l):#if we got other than 0 then answer is no(i.e we cannot make an array elements as equal)
            print('no')
        else:
            print('yes')