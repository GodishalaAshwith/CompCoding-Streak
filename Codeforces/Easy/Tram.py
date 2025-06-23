n = int(input())
max_capacity = 0
current_passengers = 0

for _ in range(n):
    a, b = map(int, input().split())
    current_passengers -= a  # passengers exiting
    current_passengers += b  # passengers entering
    max_capacity = max(max_capacity, current_passengers)

print(max_capacity)
