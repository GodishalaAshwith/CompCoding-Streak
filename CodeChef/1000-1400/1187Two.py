# cook your dish here
for i in range(int(input())):
    n=int(input())
    n2=n%8
    lst=['LB','MB','UB','LB','MB','UB','SU','SL']
    st=lst[n2-1]
    if n2 in [1,2,3]:
        ele=n+3
    elif n2 in [4,5,6]:
        ele=n-3
    elif n2==0:
        ele=n-1
    else:
        ele=n+1
    print(str(ele)+st)