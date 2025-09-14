for l in range(int(input())):
    n,k=list(map(int,input().split()))
    s=list(input())
    a=list(map(int,input().split()))
    if n==1:
        print("0\n"*k)
    else:
        d=0
        for l in range(1,n):
            if s[l]==s[l-1]:
                d+=2
            else:
                d+=1
        for l in a:
            if l==1:
                if s[0]==s[1]:
                    d-=1
                else:
                    d+=1
            elif l==n:
                if s[-1]==s[-2]:
                    d-=1
                else:
                    d+=1
            else:
                if s[l]==s[l-2]:
                    if s[l-1]==s[l]:
                        d-=2
                    else:
                        d+=2
            print(d)
            if s[l-1] == "0":
              s[l-1] = "1"
            else:
              s[l-1] = "0"