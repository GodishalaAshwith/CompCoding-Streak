def marks(s):
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '0':
            i+=1
            continue
        j = i
        while j<n and s[j]=='1':
            j+=1
        l = j - i
        if l<3:
            return False
        i = j
    return True

for _ in range(int(input())):
    n = int(input())
    s = input()
    print("Yes" if marks(s) else "No")