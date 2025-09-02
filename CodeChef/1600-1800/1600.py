# cook your dish here
test = int(input())
while(test>0):
    n =int(input())
    if n==1 or n==2:
        print(1)
    else:
       print(((n-2)*(n-1))+1)
    test-=1