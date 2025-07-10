n = int(input())
p = list(input().upper())

def isPangram(n,p):
    chars = [chr(i) for i in range(65,91)]
    for i in chars:
        if i not in p:
            return "NO"
    return "YES"

print(isPangram(n,p))