# cook your dish here
for _ in range(int(input())):
    s1 = input()
    s2 = input()
    n = len(s1)
    var = 0
    diff = 0
    for i in range(n):
        if s1[i]!=s2[i] or (s1[i]=='?' and s2[i]=='?'):
            if s1[i]=='?' or s2[i]=='?':
                var+=1
            else:
                diff+=1 
    print(diff,var+diff)