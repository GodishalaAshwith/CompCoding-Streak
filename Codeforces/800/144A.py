n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
min_height = min(a)

# First occurrence of max
max_index = a.index(max_height)
# Last occurrence of min
min_index = len(a) - 1 - a[::-1].index(min_height)

moves = max_index + (n - 1 - min_index)
if max_index > min_index:
    moves -= 1

print(moves)
