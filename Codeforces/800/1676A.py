t = int(input())
for _ in range(t):
    ticket = input().strip()
    first_half = sum(int(ticket[i]) for i in range(3))
    second_half = sum(int(ticket[i]) for i in range(3, 6))
    if first_half == second_half:
        print("YES")
    else:
        print("NO")
