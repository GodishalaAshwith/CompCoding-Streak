import math
for _ in range(int(input())):
    rows,seats = list(map(int,input().split()))
    maxSeats = math.ceil(rows/2) * math.ceil(seats/2)
    print(maxSeats)