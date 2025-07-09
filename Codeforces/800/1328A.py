t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    remainder = a % b
    moves = (b - remainder) % b
    print(moves)
