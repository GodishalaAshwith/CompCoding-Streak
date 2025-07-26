n = int(input())
pts = list(map(int, input().split()))
mx = mn = pts[0]
asm = 0

for i in pts[1:]:  # Skip the first contest
    if i > mx:
        mx = i
        asm += 1
    elif i < mn:
        mn = i
        asm += 1

print(asm)
