x1, x2, x3 = map(int, input().split())
positions = sorted([x1, x2, x3])
total_distance = positions[2] - positions[0]
print(total_distance)
