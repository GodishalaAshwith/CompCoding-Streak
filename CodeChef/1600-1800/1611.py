# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))

    needed = m - 1
    ls.sort()
    donuts_used = 0
    for i in range(m):
        if (ls[i] < needed):
            # adding this donut to the used count
            donuts_used += ls[i]
            # bcz we completely used this donut
            needed -= 1
            needed -= ls[i]

        if (needed == 0):
            print(donuts_used)
            break
    else:
        print(donuts_used + needed)