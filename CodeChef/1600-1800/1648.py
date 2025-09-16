# cook your dish here
import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    v = list(map(int, data[index:index + n]))
    index += n

    if v[0] == v[-1]:
        results.append("YES")
        continue

    found = False
    for i in range(n - 1):
        if v[i] == v[0] and v[i + 1] == v[-1]:
            results.append("YES")
            found = True
            break

    if not found:
        results.append("NO")

sys.stdout.write("\n".join(results) + "\n")